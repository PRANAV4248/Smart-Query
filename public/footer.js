console.log("Custom footer loader initialized");

const footerId = 'custom-footer';
const styleId = 'custom-footer-style';

const cssStyles = `
#${footerId} {
    position: fixed;
    bottom: 10px; /* Increased from 1px to be safer */
    right: 20px;
    z-index: 2147483647; /* Max z-index */
    pointer-events: none;
    font-size: 12px;
    color: #6b7280;
    text-align: right;
    font-family: sans-serif;
    background-color: transparent;
    display: block; /* Default visible */
    transition: opacity 0.3s ease-in-out;
}

#${footerId} a {
    pointer-events: auto;
    color: #2563eb;
    font-weight: bold;
    text-decoration: none;
}

#${footerId} a:hover {
    text-decoration: underline;
}

/* Mobile adjustments */
@media (max-width: 640px) {
    #${footerId} {
        bottom: 15px; /* Reduced from 50px to prevent floating too high */
        right: 10px;
        font-size: 10px;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 4px;
        border-radius: 4px;
        backdrop-filter: blur(2px);
    }
}
`;

function injectStyles() {
    if (document.getElementById(styleId)) return;
    const style = document.createElement('style');
    style.id = styleId;
    style.textContent = cssStyles;
    document.head.appendChild(style);
}

function createFooterElement() {
    const div = document.createElement('div');
    div.id = footerId;
    div.innerHTML = `
        Made with 💙 by <a href="https://www.linkedin.com/in/pranavchoubey89/" target="_blank">PRANAV</a>
    `;
    return div;
}

function checkVisibility() {
    const footer = document.getElementById(footerId);
    if (!footer) return;

    // Detect if we are on the "Chat" page vs "Home" page.
    // Strategy: Look for message steps. If messages exist, we are chatting.
    // Common selectors for Chainlit messages (v1/v2): .step, .cl-step, .message-content
    const messages = document.querySelectorAll('.step, .cl-step, .message-content');

    // Also check for the specific "Starters" container which implies Home.
    // But checking for *absence* of messages is usually safer for "Not Chatting".

    if (messages.length > 0) {
        // We are in a chat -> Hide footer
        footer.style.opacity = '0';
        footer.style.pointerEvents = 'none'; // Ensure no interactions
    } else {
        // We are on home (no messages) -> Show footer
        footer.style.opacity = '1';
        // Note: pointer-events is handled by CSS (none on container, auto on link)
    }
}

function ensureFooter() {
    injectStyles();
    const existing = document.getElementById(footerId);
    if (!existing) {
        // console.log("Footer missing, injecting...");
        document.body.appendChild(createFooterElement());
    }
    // Removed logic that forces it to be the last child. 
    // z-index covers visibility. Re-appending causes DOM thrashing.
    // Always check visibility
    checkVisibility();
}

// 1. Initial Injection
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ensureFooter);
} else {
    ensureFooter();
}

// 2. MutationObserver
const observer = new MutationObserver(() => {
    ensureFooter();
});
observer.observe(document.body, { childList: true, subtree: true });

// 3. Fallback Interval (checks visibility frequently)
setInterval(ensureFooter, 200);
