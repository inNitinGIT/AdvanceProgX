# Assignment 19: Simple Digital Counter & Theme Toggle App

## Objective

Build a single-screen mobile application using React Native. The app functions as a digital counter that allows users to increment, decrement, and reset a number displayed on the screen. To make the app more interactive, it must also include a **Theme Toggle** button that switches the screen's background and text colors between a Light Mode and a Dark Mode.

This assignment focuses on your ability to set up a basic React Native environment, layout components cleanly using Flexbox, and manage UI changes dynamically using React's state management.

---

## Implementation Rules

### Core Layout

The application must use standard React Native components:

- `View`
- `Text`
- `TouchableOpacity` (or `Button`)

The counter UI should be perfectly centered on the screen.

### State Management

Use the `useState` hook to manage two pieces of state:

- The current counter value (integer)
- The active theme mode (boolean or string)

### Counter Logic

- The counter should start at `0`.
- The **Increment** button must increase the count by `1`.
- The **Decrement** button must decrease the count by `1`, but it should never let the counter go below `0` (prevent negative numbers).
- The **Reset** button must bring the count back to `0`.

### Dynamic Styling

#### Light Mode (Default)

- White background
- Dark text

#### Dark Mode

- Dark gray/black background
- White text

Clicking the **Toggle Theme** button should instantly swap these styles across the entire screen.

---

## Requirements

### 1. UI Layout & Component Structure

- Correctly structure the app using a parent container.
- Include a text display for the counter.
- Create a clean arrangement of buttons using Flexbox (e.g., placing the increment/decrement buttons side-by-side).
- Use proper React Native style properties:
  - `flex`
  - `justifyContent`
  - `alignItems`
  - `fontSize`
  - `padding`

### 2. Counter State & Validation Logic

- Successfully implement the `useState` hook to track and dynamically display the counter value.
- Implement the increase, decrease, and reset functions correctly.
- **Constraint Check:** Add an internal conditional check to ensure that clicking decrement at `0` does nothing, keeping the app safe from negative values.

### 3. Dynamic Theme Toggling

- Implement state tracking for the theme (e.g., `isDarkMode`).
- Use conditional styling or ternary operators within your style objects to alter:
  - The `backgroundColor` of the main container
  - The `color` of the text components
- Update styles based on the theme state.

### 4. Code Cleanliness & Best Practices

- Maintain well-organized code with proper component separation or readable inline styling.
- Use meaningful variable and function names (e.g., `handleIncrement`, `toggleTheme`).
- Ensure no obvious runtime crashes occur during interactions.

---

## Running the Application

- Those who are having Android mobile must run it on the mobile in development mode.
- Those having iPhone may run it in the Android Studio emulator.