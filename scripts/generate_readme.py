#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'portfolio.json'
README = ROOT / 'README.md'


def load_data():
    with DATA.open('r', encoding='utf-8') as f:
        return json.load(f)


def bullet_list(items):
    return '\n'.join(f'- {item}' for item in items)


def link_list(items, url_key='url'):
    return '\n'.join(
        f'- [{item["name"]}]({item.get(url_key, item.get("repo", "#"))}) — {item.get("description", "")}'
        for item in items
    )


def project_links(projects):
    return '\n'.join(
        f'- [{project["name"]}]({project["repo"]}) — {project["description"]} | Demo: [{project["demo"]}]({project["demo"]}) | Status: {project["status"]}'
        for project in projects
    )


def skill_block(skills):
    lines = []
    for category, items in skills.items():
        lines.append(f'**{category}**: {", ".join(items)}')
    return '\n'.join(lines)


def render(data):
    return f'''<a id="desktop"></a>

<img src="assets/os/boot-screen.svg" alt="Pixel-art boot screen for the Personal Portfolio OS" width="100%" />

# PERSONAL PORTFOLIO OS

> USER: {data['name']}  
> STATUS: {data['status']}  
> ROLE: {data['role']}  
> LOCATION: {data['location']}  
> VERSION: {data['version']}

## SYSTEM BOOT SEQUENCE

```text
[ OK ] INITIALIZING PORTFOLIO SYSTEM
[ OK ] LOADING USER PROFILE
[ OK ] LOADING PROJECT DATABASE
[ OK ] LOADING EXPERIENCE
[ OK ] LOADING EDUCATION
[ OK ] LOADING ACHIEVEMENTS
[ OK ] STARTING DESKTOP

SYSTEM READY
```

<div align="center">

[███████████████████████████████████░░░░]

</div>

## DESKTOP

<img src="assets/os/desktop-wallpaper.svg" alt="Retro desktop wallpaper showing a clean creative workspace" width="100%" />

<table>
  <tr>
    <td align="center"><a href="#bio"><img src="assets/icons/bio.svg" alt="Bio application icon" width="56" /><br><strong>BIO</strong></a></td>
    <td align="center"><a href="#resume"><img src="assets/icons/resume.svg" alt="Resume application icon" width="56" /><br><strong>RESUME</strong></a></td>
    <td align="center"><a href="#cv"><img src="assets/icons/cv.svg" alt="Curriculum vitae application icon" width="56" /><br><strong>CV</strong></a></td>
    <td align="center"><a href="#browser"><img src="assets/icons/browser.svg" alt="Web browser application icon" width="56" /><br><strong>BROWSER</strong></a></td>
  </tr>
  <tr>
    <td align="center"><a href="#achievements"><img src="assets/icons/achievements.svg" alt="Achievements application icon" width="56" /><br><strong>ACHIEVEMENTS</strong></a></td>
    <td align="center"><a href="#education"><img src="assets/icons/education.svg" alt="Education application icon" width="56" /><br><strong>EDUCATION</strong></a></td>
    <td align="center"><a href="#experience"><img src="assets/icons/experience.svg" alt="Experience application icon" width="56" /><br><strong>EXPERIENCE</strong></a></td>
    <td align="center"><a href="#other"><img src="assets/icons/other.svg" alt="Other application icon" width="56" /><br><strong>OTHER</strong></a></td>
  </tr>
</table>

### PIXEL TASKBAR

<table border="1" cellpadding="8" cellspacing="0" width="100%">
  <tr>
    <td width="11%" align="center"><strong>START</strong></td>
    <td width="12%" align="center"><a href="#bio">BIO</a></td>
    <td width="12%" align="center"><a href="#resume">RESUME</a></td>
    <td width="11%" align="center"><a href="#cv">CV</a></td>
    <td width="14%" align="center"><a href="#browser">BROWSER</a></td>
    <td width="18%" align="center"><a href="#achievements">ACHIEVEMENTS</a></td>
    <td width="15%" align="center"><a href="#education">EDUCATION</a></td>
    <td width="18%" align="center"><a href="#experience">EXPERIENCE</a></td>
    <td width="12%" align="center"><a href="#other">OTHER</a></td>
    <td align="right"><strong>ONLINE</strong> • <em>PORTFOLIO OS v{data['version']}</em></td>
  </tr>
</table>

<details>
<summary><strong>START MENU</strong></summary>

### USER

**{data['name']}**  
Developer / Creator / Builder

### APPLICATIONS

- [Bio](#bio)
- [Resume](#resume)
- [Curriculum Vitae](#cv)
- [Web Browser](#browser)
- [Achievements](#achievements)
- [Education](#education)
- [Experience](#experience)
- [Other](#other)

### SYSTEM

- [About this Portfolio OS](#system-status)
- [GitHub]({data['github']})
- [LinkedIn]({data['linkedin']})
- [Email]({data['email']})
- [Resume Download]({data['resume']})

</details>

---

<a id="bio"></a>

<table border="1" cellpadding="12" cellspacing="0" width="100%">
  <tr>
    <td bgcolor="#1f1f23"><strong>BIO.EXE</strong> <span style="float:right">[—][□][×]</span></td>
  </tr>
  <tr>
    <td>
      <table>
        <tr>
          <td valign="top">
            <img src="assets/icons/bio.svg" alt="Pixel-art portrait icon for the Bio section" width="120" />
          </td>
          <td valign="top">
            <h3>{data['name']}</h3>
            <p><strong>{data['title']}</strong></p>
            <p>{data['intro']}</p>
            <p>{data['bio']}</p>
          </td>
        </tr>
      </table>

      <h4>INTERESTS</h4>
      {bullet_list(data['interests'])}

      <h4>CURRENT FOCUS</h4>
      {bullet_list(data['focusAreas'])}

      <h4>GOALS</h4>
      {bullet_list(data['goals'])}

      <h4>PERSONAL PHILOSOPHY</h4>
      <p>{data['philosophy']}</p>

      <p><a href="#desktop">← BACK TO DESKTOP</a></p>
    </td>
  </tr>
</table>

---

<a id="resume"></a>

<table border="1" cellpadding="12" cellspacing="0" width="100%">
  <tr>
    <td bgcolor="#1f1f23"><strong>RESUME.EXE</strong> <span style="float:right">[—][□][×]</span></td>
  </tr>
  <tr>
    <td>
      <p><strong>Professional Summary</strong></p>
      <p>{data['bio']}</p>
      <p><a href="{data['resume']}"><strong>[ DOWNLOAD RESUME ]</strong></a></p>
      <p><strong>Highlights</strong></p>
      <ul>
        <li>Product-minded software development</li>
        <li>Clean, maintainable engineering</li>
        <li>Builds across frontend and backend concerns</li>
        <li>Focused on practical user experience</li>
      </ul>
      <p><a href="#desktop">← BACK TO DESKTOP</a></p>
    </td>
  </tr>
</table>

---

<a id="cv"></a>

<table border="1" cellpadding="12" cellspacing="0" width="100%">
  <tr>
    <td bgcolor="#1f1f23"><strong>CURRICULUM_VITAE.EXE</strong> <span style="float:right">[—][□][×]</span></td>
  </tr>
  <tr>
    <td>
      <h4>PERSONAL INFORMATION</h4>
      <p><strong>Name:</strong> {data['name']}<br>
      <strong>Role:</strong> {data['role']}<br>
      <strong>Location:</strong> {data['location']}<br>
      <strong>Portfolio:</strong> <a href="{data['portfolio']}">GitHub Profile</a></p>

      <details>
      <summary><strong>EDUCATION</strong></summary>
      {bullet_list([f"{item['institution']} — {item['program']} ({item['dates']})" for item in data['education']])}
      </details>

      <details>
      <summary><strong>EXPERIENCE</strong></summary>
      {bullet_list([f"{item['organization']} — {item['position']} ({item['dates']})" for item in data['experience']])}
      </details>

      <details>
      <summary><strong>SKILLS</strong></summary>
      {skill_block(data['skills'])}
      </details>

      <details>
      <summary><strong>PROJECTS</strong></summary>
      {project_links(data['projects'])}
      </details>

      <p><a href="#desktop">← BACK TO DESKTOP</a></p>
    </td>
  </tr>
</table>

---

<a id="browser"></a>

<table border="1" cellpadding="12" cellspacing="0" width="100%">
  <tr>
    <td bgcolor="#1f1f23"><strong>WEB-BROWSER.EXE</strong> <span style="float:right">[—][□][×]</span></td>
  </tr>
  <tr>
    <td>
      <p><strong>←  →  ⟳</strong> &nbsp; <strong>ADDRESS:</strong> https://github.com/SIMARSINGHRAYAT</p>
      <h4>PROFESSIONAL</h4>
      {link_list(data['browserLinks'])}

      <h4>BROWSER LINKS</h4>
      <pre>
ICON | NAME | DESCRIPTION | URL
---- | ---- | ----------- | ---
{chr(10).join(f"{item['icon']} | {item['name']} | {item['description']} | {item['url']}" for item in data['browserLinks'])}
      </pre>

      <p><a href="#desktop">← BACK TO DESKTOP</a></p>
    </td>
  </tr>
</table>

---

<a id="achievements"></a>

<table border="1" cellpadding="12" cellspacing="0" width="100%">
  <tr>
    <td bgcolor="#1f1f23"><strong>ACHIEVEMENTS.EXE</strong> <span style="float:right">[—][□][×]</span></td>
  </tr>
  <tr>
    <td>
      {''.join(f'''<p><strong>[ UNLOCKED ]</strong> {item['title']}<br><em>{item['description']}</em><br><strong>DATE:</strong> {item['date']}<br><strong>VERIFICATION:</strong> {item['verified']}</p>''' for item in data['achievements'])}
      <p><a href="#desktop">← BACK TO DESKTOP</a></p>
    </td>
  </tr>
</table>

---

<a id="education"></a>

<table border="1" cellpadding="12" cellspacing="0" width="100%">
  <tr>
    <td bgcolor="#1f1f23"><strong>EDUCATION.EXE</strong> <span style="float:right">[—][□][×]</span></td>
  </tr>
  <tr>
    <td>
      <table border="1" cellpadding="8" cellspacing="0" width="100%">
        <tr><th>Institution</th><th>Program</th><th>Degree</th><th>Dates</th></tr>
        {''.join(f'''<tr><td>{item['institution']}</td><td>{item['program']}</td><td>{item['degree']}</td><td>{item['dates']}</td></tr>''' for item in data['education'])}
      </table>
      <p><strong>Key outcomes:</strong></p>
      {bullet_list(data['education'][0]['highlights'])}
      <p><a href="#desktop">← BACK TO DESKTOP</a></p>
    </td>
  </tr>
</table>

---

<a id="experience"></a>

<table border="1" cellpadding="12" cellspacing="0" width="100%">
  <tr>
    <td bgcolor="#1f1f23"><strong>EXPERIENCE.EXE</strong> <span style="float:right">[—][□][×]</span></td>
  </tr>
  <tr>
    <td>
      {''.join(f'''<p><strong>{item['organization']}</strong> — {item['position']}<br>{item['dates']}</p><ul>{''.join(f'<li>{responsibility}</li>' for responsibility in item['responsibilities'])}</ul><p><strong>Technologies:</strong> {', '.join(item['technologies'])}</p>''' for item in data['experience'])}
      <p><a href="#desktop">← BACK TO DESKTOP</a></p>
    </td>
  </tr>
</table>

---

<a id="other"></a>

<table border="1" cellpadding="12" cellspacing="0" width="100%">
  <tr>
    <td bgcolor="#1f1f23"><strong>OTHER.EXE</strong> <span style="float:right">[—][□][×]</span></td>
  </tr>
  <tr>
    <td>
      <h4>HOBBIES & INTERESTS</h4>
      {bullet_list(data['interests'])}

      <h4>PROJECTS</h4>
      {''.join(f'''<p><strong>{project['name']}</strong><br>{project['description']}<br><strong>Stack:</strong> {project['stack']}<br><a href="{project['repo']}">Repository</a> • <a href="{project['demo']}">Demo</a> • <strong>Status:</strong> {project['status']}</p>''' for project in data['projects'])}

      <h4>CURRENTLY LEARNING</h4>
      <p>Practical systems design, polished web interfaces, and product-minded engineering workflows.</p>

      <p><a href="#desktop">← BACK TO DESKTOP</a></p>
    </td>
  </tr>
</table>

---

<a id="system-status"></a>

<table border="1" cellpadding="12" cellspacing="0" width="100%">
  <tr>
    <td bgcolor="#1f1f23"><strong>SYSTEM_STATUS.EXE</strong> <span style="float:right">[—][□][×]</span></td>
  </tr>
  <tr>
    <td>
      <p><strong>OS:</strong> {data['system']}<br>
      <strong>VERSION:</strong> {data['version']}<br>
      <strong>USER:</strong> {data['name']}<br>
      <strong>STATUS:</strong> {data['status']}<br>
      <strong>MODE:</strong> {data['mode']}<br>
      <strong>CURRENT FOCUS:</strong> {data['focus']}</p>
      <p><a href="{data['github']}">[ VIEW GITHUB ]</a> &nbsp; <a href="{data['linkedin']}">[ LINKEDIN ]</a> &nbsp; <a href="{data['email']}">[ CONTACT ]</a></p>
      <p><a href="#desktop">← BACK TO DESKTOP</a></p>
    </td>
  </tr>
</table>

---

## CONTACT & SOCIAL LINKS

- [GitHub]({data['github']})
- [LinkedIn]({data['linkedin']})
- [Email]({data['email']})
- [Resume Download]({data['resume']})

## UPDATE YOUR PROFILE

This README is designed to be easy to personalize. The source data lives in [portfolio.json](portfolio.json), and the generated README can be refreshed by running:

```bash
python3 scripts/generate_readme.py
```

Update the name, role, links, projects, education, and browser links there to keep the OS experience current.

---

<div align="center">

<strong>SYSTEM STATUS: ONLINE</strong><br>
<strong>THANK YOU FOR VISITING</strong><br>
<strong>END OF SESSION</strong>

</div>

<p align="center"><a href="#desktop">[ RETURN TO DESKTOP ]</a></p>
'''


def main():
    data = load_data()
    README.write_text(render(data), encoding='utf-8')
    print(f'Wrote {README}')


if __name__ == '__main__':
    main()
