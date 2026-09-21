# Changing a CIS session or persona

Every CIS skill takes overrides without being edited. `bmad-customize`, from `core-tools`, writes them. When it is not installed, say so and offer to install it. The override files are `{project-root}/_bmad/custom/{skill-name}.toml` for the team and `{skill-name}.user.toml` for one person.

## What a session exposes

- Standing facts the session carries from start to finish: the company's brand voice for storytelling, the team's own problem-solving method, a customer research file to ground design thinking. A fact can be text or a file path.
- Steps to run before or after activation, such as loading a document the session should always start from.
- An instruction to follow when the session completes, such as publishing the document somewhere or handing it to another skill.

The steps of a session and its template are not exposed. A user who wants a different session is asking for a new skill.

## What a persona exposes

- Role, identity, communication style, and principles. A team can tone a persona down or point it at their domain.
- Standing facts, and steps before or after activation.
- The icon.
- The menu: add an item that calls a skill or runs a prompt, or replace one by its code.

Name and title are fixed. A user who wants a different name needs a custom agent.

## Party mode follows

A persona's customized name, title, and icon carry into party mode when its skill is installed. Its voice there comes from the module's roster, so a customized style or principles do not.
