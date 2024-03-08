<template>
  <header-bar></header-bar>
  <br/>
  <div class="content">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      items: []
    }
  },
  provide() {
    return {
    }
  },
  methods: {
  }
}
</script>

<style>
#app {
  /*font-family: Avenir, Helvetica, Arial, sans-serif;*/
    font-family: 'Arial', sans-serif;
    color: #333;
}

.content {
  margin-left: 1em;

}

#app a {
    text-decoration: none;
    color: inherit;
}

input, select {
    width: 30%; /* Full width */
    padding: 5px 10px;
    margin: 5px 0; /* Space between form elements */
    border-radius: 10px; /* Rounded corners */
    border: 1px solid #CCC; /* Light border */
    box-sizing: border-box; /* Include padding and border in the element's total width and height */
    font-size: 16px; /* Increased font size for readability */
    outline: none; /* Remove the outline */
    box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1); /* Inner shadow for depth */
    display: inline-block;
}

input:focus, select:focus {
    border-color: #008080; /* Highlight focus with teal color */
}

label {
    display: inline-block; /* Ensure labels are block-level elements for better control */
    width: 10%;
    margin-bottom: 8px; /* Space before the input/select for clarity */
    margin-left: 15px;
    font-size: 16px; /* Readable text size */
    color: #333; /* Dark color for readability */
    font-weight: 500; /* Slightly bolder than normal text for emphasis */
    transition: color 0.3s; /* Smooth transition for any color change */
}

label.focused {
    color: #008080; /* Teal color to match the focused state of inputs/selects */
}

nav button, nav a {
  background-color: initial;
  color: initial;
}

button {
    background-image: linear-gradient(to right, #008080 0%, #26D0CE 100%); /* Teal gradient */
    border: none;
    border-radius: 10px; /* Rounded corners */
    color: white; /* Text color */
    padding: 8px 15px; /* Padding for size */
    font-size: 16px; /* Font size */
    cursor: pointer; /* Cursor indicates button */
    outline: none; /* Remove outline */
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    transition: transform 0.2s ease, box-shadow 0.2s ease; /* Smooth transitions for interaction */
    margin: 10px;
}

button:hover, button:focus {
    transform: translateY(-1px); /* Slight lift */
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2); /* Enhanced shadow on hover/focus */
}

button:active {
    transform: translateY(1px); /* Simulate press */
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15); /* Subtle shadow on press */
}
</style>
