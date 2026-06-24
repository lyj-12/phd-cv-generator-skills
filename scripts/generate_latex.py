"""generate_latex.py — Very simple LaTeX CV generator.

The AI generates the complete .tex content. This script just:
1. Copies template scaffolding (.cls, .sty, fonts, images) to output
2. Writes the AI-generated .tex content as the main file

Usage:
    python generate_latex.py --template <name> --output <dir> --content <data.json>
"""

import argparse, json, os, shutil

TEMPLATES = {
    "blue": {
        "dir": "latex/cv_resume-blue",
        "main": "template_cn_blue.tex",
        "label": "蓝色 (moderncv)",
    },
    "dark-blue-zh": {
        "dir": "latex/resume-Dark_blue-zh-en",
        "main": "resume-zh.tex",
        "label": "深蓝色 (中文)",
    },
    "dark-blue-en": {
        "dir": "latex/resume-Dark_blue-zh-en",
        "main": "resume-en.tex",
        "label": "深蓝色 (英文)",
    },
    "black-simple": {
        "dir": "latex/resume-zh_CN-black-simple",
        "main": "resume-zh_CN.tex",
        "label": "黑白简约 (中文)",
    },
}


def main():
    import argparse, json, os, shutil
    ap = argparse.ArgumentParser(description="Generate PhD CV LaTeX")
    ap.add_argument("--template", required=True, choices=list(TEMPLATES.keys()))
    ap.add_argument("--output", required=False, default=".")
    ap.add_argument("--content", required=True)
    args = ap.parse_args()

    with open(args.content, "r", encoding="utf-8") as f:
        data = json.load(f)

    tmpl = TEMPLATES[args.template]
    sd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(sd, tmpl["dir"])

    name = data.get("name", "CV").strip()
    advisor = data.get("advisor", "").strip()
    suffix = "-定向" + advisor if advisor else ""
    default_out = (name + suffix).replace(" ", "")

    if args.output == ".":
        args.output = os.path.join(os.getcwd(), default_out)
    output_dir = os.path.abspath(args.output)

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    shutil.copytree(src, output_dir)

    main_name = tmpl["main"]
    main_path = os.path.join(output_dir, main_name)
    tex_content = data.get("tex_content", "")
    if tex_content:
        with open(main_path, "w", encoding="utf-8") as f:
            f.write(tex_content)

    # Write Chinese sub-files
    for ek, fn in [["sections_cn","sections.tex"],["header_cn","header.tex"],
                   ["sections_content","sections.tex"],["header_content","header.tex"]]:
        ec = data.get(ek, "")
        if ec:
            p = os.path.join(output_dir, "texs", fn)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(ec)

    # Write English sub-files
    for ek, fn in [["sections_en","sections-en.tex"],["header_en","header-en.tex"]]:
        ec = data.get(ek, "")
        if ec:
            p = os.path.join(output_dir, "texs", fn)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(ec)

    # Handle English main
    tex_en = data.get("tex_main_en", "")
    if tex_en:
        en_path = os.path.join(output_dir, "resume-en.tex")
        with open(en_path, "w", encoding="utf-8") as f:
            f.write(tex_en)

    # Copy photo
    photo = data.get("photo", "")
    if photo and os.path.exists(photo):
        shutil.copy2(photo, os.path.join(output_dir, os.path.basename(photo)))

    print("Template: " + tmpl["label"])
    print("Output  : " + main_path)
    print("Compile : cd \"" + output_dir + "\" && xelatex resume-zh_CN.tex")
    print("Done.")

if __name__ == "__main__":
    main()