# Latex Setup

> Ref.  
>
>- [LaTeX-Workshop Wiki](https://github.com/James-Yu/LaTeX-Workshop/wiki)
>- [VSCode + Texlive + SumatraPDF](https://zhuanlan.zhihu.com/p/142963562)  
>- [Texlive + VScode](https://zhuanlan.zhihu.com/p/58811994)  
>- [VSCode + SumatraPDF error](https://zhuanlan.zhihu.com/p/434142338)  

## 1. TeX Live  

### Installation  

Download [TeX Live](https://www.tug.org/texlive/) for Windows. Easy install is recommended.  
Installing the full TeX Live package is time consuming (for over 1h).

### Setting PATH environment variable  

No need on Windows.  

## 2. VSCode  

### Install Extensions

Install LaTeX Workshop.  

### Shortcut  

- Ctrl + Alt + B  
Compile the `.tex` file.  
- Ctrl + Alt + J  
Open the `.PDF` file.  

## 3. SumatraPDF  

### Setting  

Go to `Settings -> Advanced Options -> Add command`.
Set the following arguments in `setting.txt`.

```bash
# use '\' instead of '/', or it may cause problems.
InverseSearchCmdLine = "<VSCode path>\Code.exe" "<VSCode path>\resources\app\out\cli.js" --ms-enable-electron-run-as-node -r -g "%f:%l"
EnableTeXEnhancements = true
```  

In VSCode, go to `Management (bottom left) -> Setting -> Open Setting`.  
Add the following arguments in `settings.json`.  Remember to config the path.  

```json
{
    // LaTeX workshop  
    "latex-workshop.latex.recipes": [
        {
            "name": "xe->xe",
            "tools": [
                "xelatex",
                "xelatex"
            ]
        },
        {
            "name": "xe->bib->xe->xe",
            "tools": [
                "xelatex",
                "bibtex",
                "xelatex",
                "xelatex"
            ]
        },
        {
          "name": "pdf->pdf",
          "tools": [
              "pdflatex",
              "pdflatex"
          ]
        },
        {
          "name": "pdf->bib->pdf->pdf",
          "tools": [
              "pdflatex",
              "bibtex",
              "pdflatex",
              "pdflatex"
          ]
        }
    ],
    
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOCFILE%"
            ]
        },
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOCFILE%"
            ]
        },
        {
            "name": "bibtex",
            "command": "bibtex",
            "args": [
                "%DOCFILE%"
            ]
        }
    ],
    
    "latex-workshop.latex.autoClean.run": "onBuilt",
    "latex-workshop.view.pdf.viewer": "external",
    "latex-workshop.view.pdf.external.synctex.command": "<SumatraPDF path>/SumatraPDF.exe",
    "latex-workshop.view.pdf.external.synctex.args": [
        "-forward-search",
        "%TEX%",
        "%LINE%",
        "-reuse-instance",
        "-inverse-search",
        "\"<VSCode path>\\Code.exe\" \"<VSCode path>\\resources\\app\\out\\cli.js\" --ms-enable-electron-run-as-node -r -g \"%f:%l\"",
        "%PDF%"
    ],
}
```
