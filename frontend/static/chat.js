const HUMAN_LABEL = "[Human]: ";
const PITS_LABEL = "[Pits]: ";

const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))

const getChatId = () => {
  const parsedUrl = new URL(window.location.href);
  const path = parsedUrl.pathname.endsWith("/")
    ? parsedUrl.pathname.slice(0, -1)
    : parsedUrl.pathname;
  return path.split("/").pop();
};

const appendMessage = (content, label, container, delay) => {
  const newMessageNode = document.createElement("div");
  const wrapper = document.getElementById("wrapper");
  const typeSpeed = 20;
  container.appendChild(newMessageNode);
  if (delay) {
    for (let i = 0; i < content.length; i++) {
      setTimeout(() => {
        newMessageNode.textContent = label + content.slice(0, i + 1);
        wrapper.scrollTo(0, wrapper.scrollHeight);
      }, i * typeSpeed);
    }
    setTimeout(() => {
      showInputArea();
      wrapper.scrollTo(0, wrapper.scrollHeight);
    }, content.length * typeSpeed);
  } else {
    newMessageNode.textContent = label + content;
  }
  wrapper.scrollTo(0, wrapper.scrollHeight);
};

const fetchJson = async (url, options = {}) => {
  try {
    const response = await fetch(url, options);
    if (!response.ok) throw new Error("Network error");
    return await response.json();
  } catch (error) {
    console.error("Error", error);
  }
};

const getMessages = async (chat_id, container) => {
  const data = await fetchJson(`/chat/${chat_id}/messages/`);
  if (data) {
    data.forEach((message) => {
      appendMessage(
        message.content,
        message.is_human ? HUMAN_LABEL : PITS_LABEL,
        container
      );
    });
  }
};

const sendNewMessage = async (content, chat_id, container) => {
  const postResponse = await fetchJson("/message/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ content, chat: chat_id, is_human: true }),
  });
  if (!postResponse) return;
  const data = await fetchJson(`/ai/${chat_id}/`);
  if (data) {
    appendMessage(data.content, PITS_LABEL, container, true);
  }
};

const hideInputArea = () => {
  document.getElementById("inputArea").style.display = "none";
}

const showInputArea = () => {
  document.getElementById("inputArea").style.display = "";
}

document.addEventListener("DOMContentLoaded", () => {
  const wrapper = document.getElementById("wrapper");
  const textInput = document.getElementById("textInput");
  const messages = document.getElementById("messages");
  const cursor = document.getElementsByClassName("cursor")[0];
  const chat_id = getChatId();
  getMessages(chat_id, messages);
  wrapper.focus();

  let currentText = "";

  wrapper.addEventListener("keydown", (event) => {
    event.preventDefault();
    if (event.key === "Enter") {
      currentText = currentText.trim();
      if (!currentText) return;
      hideInputArea();
      appendMessage(currentText, HUMAN_LABEL, messages);
      sendNewMessage(currentText, chat_id, messages).then(() => {
        currentText = "";
        textInput.textContent = HUMAN_LABEL;
        textInput.appendChild(cursor);
      });
    } else if (event.key === "Backspace") {
      textInput.textContent = textInput.textContent.slice(0, -1);
      currentText = currentText.slice(0, -1);
      textInput.appendChild(cursor);
    } else if (event.key.length === 1) {
      textInput.textContent += event.key;
      currentText += event.key;
      textInput.appendChild(cursor);
    }
    wrapper.scrollTo(0, wrapper.scrollHeight);
  });
});
