import { useState } from "react";

import "./app.css";

function App() {

  /* =========================================
     COUNTER STATE
     Stores current counter value
  ========================================= */
  const [count, setCount] = useState(0);

  /* =========================================
     THEME STATE
     false  -> Light Mode
     true   -> Dark Mode
  ========================================= */
  const [isDarkMode, setIsDarkMode] = useState(false);



  /* =========================================
     HANDLE INCREMENT
     Increase counter by 1
  ========================================= */
  const handleIncrement = () => {
    setCount(count + 1);
  };



  /* =========================================
     HANDLE DECREMENT
     Decrease counter by 1
  ========================================= */
  const handleDecrement = () => {

    /* =========================================
       VALIDATION LOGIC
       Prevent counter from going below 0
    ========================================= */
    if (count > 0) {
      setCount(count - 1);
    }
  };



  /* =========================================
     HANDLE RESET
     Reset counter back to 0
  ========================================= */
  const handleReset = () => {
    setCount(0);
  };



  /* =========================================
     TOGGLE THEME
     Switch between light & dark mode
  ========================================= */
  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };



  return (

    /* =========================================
       TERNARY OPERATOR USED HERE

       If isDarkMode is true:
       -> Dark background & white text

       Else:
       -> White background & dark text
    ========================================= */

    <div
      className="app-container"
      style={{
        backgroundColor: isDarkMode ? "#121212" : "#ffffff",
        color: isDarkMode ? "#ffffff" : "#000000",
      }}
    >

      <div
        className="counter-card"
        style={{
          backgroundColor: isDarkMode ? "#1f1f1f" : "#f4f4f4",
        }}
      >

        <h1 className="app-title">
          Digital Counter 
        </h1>


        {/* COUNTER DISPLAY */}
        <div className="counter-value">
          {count}
        </div>


        {/* BUTTON SECTION */}
       <div className="button-group">

  {/* Increment Button */}
  <button
    className="increment-btn"
    onClick={handleIncrement}
  >
    Increment
  </button>

  {/* Reset Button in Between */}
  <button
    className="reset-btn"
    onClick={handleReset}
  >
    Reset
  </button>

  {/* Decrement Button */}
  <button
    className="decrement-btn"
    onClick={handleDecrement}
  >
    Decrement
  </button>

</div>


        {/* THEME TOGGLE BUTTON */}
        <button
          className="theme-btn"
          onClick={toggleTheme}
        >
          Toggle Theme
        </button>

      </div>

    </div>
  );
}

export default App;