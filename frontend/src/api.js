const API_BASE_URL = "http://localhost:8000";

export async function reviewCode({ language, code }) {
  const res = await fetch(`${API_BASE_URL}/review`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ language, code }),
  });

  if (!res.ok) {
    throw new Error("Failed to review code");
  }

  return res.json(); // { hasErrors, errors, improvedCode, comments }
}
