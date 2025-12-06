import { useState } from "react";
import { reviewCode } from "./api";
import "./index.css";

function App() {
  const [language, setLanguage] = useState("javascript");
  const [code, setCode] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [errorMsg, setErrorMsg] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!code.trim()) return;

    setLoading(true);
    setErrorMsg("");
    setResult(null);

    try {
      const data = await reviewCode({ language, code });
      setResult(data);
    } catch (err) {
      console.error(err);
      setErrorMsg("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-root">
      <div className="app-card">
        <header className="app-header">
          <h1>
            Code Review Assistant- <span className="sp">SyntaxSensei</span>{" "}
          </h1>
          <p>Paste your code, choose a language, and get instant feedback.</p>
        </header>

        <form className="app-form" onSubmit={handleSubmit}>
          <div className="form-row">
            <label className="field-label">
              Language
              <select
                value={language}
                onChange={(e) => setLanguage(e.target.value)}
                className="select-input"
              >
                {/* <option value="javascript">JavaScript</option> */}
                <option value="python">Python</option>
              </select>
            </label>
          </div>

          <div className="form-row">
            <label className="field-label">
              Your Code
              <textarea
                value={code}
                onChange={(e) => setCode(e.target.value)}
                rows={10}
                className="code-input"
                placeholder="Paste or type your Python code here..."
              />
            </label>
          </div>

          <button
            type="submit"
            disabled={loading || !code.trim()}
            className={`primary-button ${
              loading || !code.trim() ? "button-disabled" : ""
            }`}
          >
            {loading ? "Reviewing..." : "Review Code"}
          </button>
        </form>

        {errorMsg && <p className="error-text">{errorMsg}</p>}

        {result && (
          <section className="results-section">
            <p className="status-line">
              <strong>Status:</strong>{" "}
              <span className={result.hasErrors ? "status-bad" : "status-good"}>
                {result.hasErrors ? "Errors found" : "No major issues detected"}
              </span>
            </p>

            {result.errors && result.errors.trim() && (
              <div className="panel panel-error">
                <h3>Errors / Issues</h3>
                <pre>{result.errors}</pre>
              </div>
            )}

            {result.improvedCode && result.improvedCode.trim() && (
              <div className="panel panel-code">
                <h3>Improved Code</h3>
                <pre>{result.improvedCode}</pre>
              </div>
            )}

            {/* {result.comments && result.comments.trim() && (
              <div className="panel panel-info">
                <h3>Review Comments</h3>
                <pre>{result.comments}</pre>
              </div>
            )} */}
          </section>
        )}
      </div>
    </div>
  );
}

export default App;
