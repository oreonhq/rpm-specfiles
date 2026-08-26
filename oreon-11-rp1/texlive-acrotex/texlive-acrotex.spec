%global source0_hash ec054fde139651b0c3be678b5de3ea9e6d2e586df479c962785f947adc486a0c

%global tl_version 2025
%global revision 330

# The acrotex bundle is part of texlive, but it lives in their archive.
# ... but stuff in texlive still depends on it, so I've packaged it.
# Epoch inherits from texlive for consistency.

Name:           texlive-acrotex
Epoch:          12
Version:        svn%{revision}
Release:        2%{?dist}
Summary:        The AcroTeX education bundle
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlcontrib/archive/acrotex.r330.tar.xz
Source1:	https://ctan.math.illinois.edu/systems/texlive/tlcontrib/archive/acrotex.doc.r330.tar.xz
# License texts
Source2:        texlive-licenses.tar.xz

BuildRequires:  texlive-base
Provides:	tex(aeb-comment.sty) = %{tl_version}
Provides:	tex(dljslib.sty) = %{tl_version}
Provides:	tex(eforms.sty) = %{tl_version}
Provides:	tex(exerquiz.sty) = %{tl_version}
Provides:	tex(insdljs.sty) = %{tl_version}
Provides:	tex(taborder.sty) = %{tl_version}
Provides:	tex(web.sty) = %{tl_version}
Requires:       texlive-base
Requires:	texlive-kpathsea
Requires:	tex(ifpdf.sty)
Requires:	tex(ifxetex.sty)
Requires:	tex(ifluatex.sty)
Requires:	tex(calc.sty)
Requires:	tex(hyperref.sty)
Requires:	tex(array.sty)
Requires:	tex(aeb-comment.sty)
Requires:	tex(verbatim.sty)
Requires:	tex(amssymb.sty)
Requires:	tex(everyshi.sty)
Requires:	tex(xkeyval.sty)
Requires:	tex(xcolor.sty)
Requires:	tex(graphicx.sty)
Requires:	tex(eso-pic.sty)

%description
The bundle contains: the web package to redefine page layout to
web-friendly dimensions; the exerquiz package for defining
on-line exercises and quizzes of various sorts; the eForms
package for support of PDF forms; the insdljs package for
inserting document-level JavaScript in LaTeX documents; the
dljslib library of JavaScript functions for use with exerquiz;
and the eq2db package for converting an exerquiz quiz for
processing by a ASP server-side script.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Extract license files
tar -xf %{SOURCE2}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE1} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

%files
%license lppl.txt
%{_texmf_main}/tex/latex/acrotex/
%doc %{_texmf_main}/doc/latex/acrotex/

%changelog
%autochangelog
