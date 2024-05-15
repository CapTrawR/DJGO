function my_scope() {
    const forms = document.querySelectorAll('.form-delete');
    
    for (const form of forms) {
        form.addEventListener('submit', function (e) {
            e.preventDefault(); // previne o usuario de mandar o formulario
            const confirmed = confirm('Are you sure?');
  
            if (confirmed) {
            form.submit();
            }
        });
    }
  }
  my_scope();