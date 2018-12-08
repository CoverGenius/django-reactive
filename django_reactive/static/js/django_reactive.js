function djangoReactiveRenderForm(name, schema, ui_schema, data) {

    var Form = JSONSchemaForm.default, // required by json-react-schema-form
        textarea = document.getElementById('id_' + name),
        save = document.getElementsByName('_save')[0],
        _el = React.createElement;

    function transformErrors(errors) {
        save.disabled = errors.length;

        return errors;
    }

    function Label(props) {
        var id = props.id,
            label = props.label,
            required = props.required;

        if (!label) {
            // See #312: Ensure compatibility with old versions of React.
            return _el('div');
        }

        return _el("label", {className: "control-label", htmlFor: id},
            label,
            required && _el("span",
            {className: "required"},
            '*'
            )
        );
    }

    function TitleField(props) {
        var title = props.title, required = props.required;
        var legend = required ? title + '*' : title;

        return _el('h2', {}, legend);
    }

    function DescriptionField(props) {
        var id = props.id, description = props.description;
        return _el('p', {id: id, className: 'field-description'}, description);
    }

    function FieldTemplate(props) {
        var id = props.id,
            classNames = props.classNames,
            label = props.label,
            children = props.children,
            errors = props.errors,
            help = props.help,
            description = props.description,
            hidden = props.hidden,
            required = props.required,
            displayLabel = props.displayLabel;

        if (hidden) {
            return children;
        }

        return _el(
            "div",
            {className: classNames},
            displayLabel && _el(Label, {label: label, required: required, id: id}),
            displayLabel && description ? description : null,
            _el(
                "div",
                {className: "form-input"},
                children
            ),
            errors,
            help
        );
    }

    ReactDOM.render((
        _el(Form, {
                schema: schema,
                formData: data,
                uiSchema: ui_schema,
                liveValidate: true,
                showErrorList: false,
                onChange: function (form) {
                    textarea.value = JSON.stringify(form.formData);
                },
                transformErrors: transformErrors,
                fields: {
                    TitleField: TitleField,
                    DescriptionField: DescriptionField,
                },
                idPrefix: "id_" + name + "_form",
                FieldTemplate: FieldTemplate,
            }, _el("span") // render an empty span as child in order to avoid displaying submit button
        )
    ), document.getElementById(name + "_editor"));
}
