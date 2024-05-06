const HUMAN_LABEL = "[Human]: ";
const PITS_LABEL = "[Pits]: ";

const getChatId = () => {
  const parsedUrl = new URL(window.location.href);
  const path = parsedUrl.pathname.endsWith("/")
    ? parsedUrl.pathname.slice(0, -1)
    : parsedUrl.pathname;
  return path.split("/").pop();
};

const appendMessage = (content, is_human, container, delay) => {
  const newMessageNode = document.createElement("div");
  const typeSpeed = 20;
  let label = PITS_LABEL;

  if (is_human) {
    label = HUMAN_LABEL;
    newMessageNode.classList.add("human");
  }

  container.appendChild(newMessageNode);
  if (delay) {
    for (let i = 0; i < content.length; i++) {
      setTimeout(() => {
        newMessageNode.textContent = label + content.slice(0, i + 1);
      }, i * typeSpeed);
    }
    setTimeout(() => {
      showInputArea();
    }, content.length * typeSpeed);
  } else {
    newMessageNode.textContent = label + content;
  }
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
      appendMessage(message.content, message.is_human, container);
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
    appendMessage(data.content, false, container, true);
  }
};

const hideInputArea = () => {
  document.getElementById("inputArea").style.display = "none";
};

const showInputArea = () => {
  document.getElementById("inputArea").style.display = "";
};

const scrollToBottom = () => {
  const wrapper = document.getElementById("wrapper");
  wrapper.scrollTo(0, wrapper.scrollHeight);
};

const scrollObserver = (wrapper) => {
  const observer = new MutationObserver((mutations) => {
    scrollToBottom();
  });

  observer.observe(wrapper, {
    childList: true,
    subtree: true,
    attributes: true,
  });
};

document.addEventListener("DOMContentLoaded", () => {
  const wrapper = document.getElementById("wrapper");
  const textInput = document.getElementById("textInput");
  const messages = document.getElementById("messages");
  const cursor = document.getElementsByClassName("cursor")[0];
  const chat_id = getChatId();
  scrollObserver(wrapper);
  getMessages(chat_id, messages);
  wrapper.focus();

  let currentText = "";

  wrapper.addEventListener("keydown", (event) => {
    event.preventDefault();
    if (event.key === "Enter") {
      currentText = currentText.trim();
      if (!currentText) return;
      hideInputArea();
      appendMessage(currentText, true, messages, false);
      sendNewMessage(currentText, chat_id, messages).then(() => {
        currentText = "";
        textInput.textContent = HUMAN_LABEL;
        textInput.appendChild(cursor);
      });
    } else if (event.key === "Backspace") {
      if (textInput.textContent.length <= HUMAN_LABEL.length) return;
      textInput.textContent = textInput.textContent.slice(0, -1);
      currentText = currentText.slice(0, -1);
      textInput.appendChild(cursor);
    } else if (event.key.length === 1) {
      textInput.textContent += event.key;
      currentText += event.key;
      textInput.appendChild(cursor);
    }
  });
});
