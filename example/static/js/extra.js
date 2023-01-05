document.addEventListener('DOMContentLoaded', function() {

  /*
    Modify the editor dynamically on page load.

    IMPORTANT: Changes defined here may be overwritten by React component state, so it
               may not be reliable for dynamic schema mutations.
  */

  let todoEditor = document.querySelector('#todos_editor')
  todoEditor.style.backgroundColor = '#f0f0f0'
}, false);
