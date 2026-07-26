%global source0_hash 105254a8b04934f0bc84e9c24eb360a591aaf6535c9def5f29d92af107a9bf57

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-pyperclip
Version:        1.8.2
Release:        16%{?dist}
Summary:        A cross-platform clipboard module for Python

License:        BSD-3-Clause
URL:            https://github.com/asweigart/pyperclip
Source0:        %{pypi_source pyperclip}
BuildArch:      noarch

%global common_description %{expand:
Pyperclip is a cross-platform Python module for copy and paste clipboard
functions.}

%description %{common_description}

%package -n     python3-pyperclip
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# While upstream runs tests directly with Python/unittest, using pytest as the
# runner allows us to more easily skip tests.
BuildRequires:  python3dist(pytest)

# Support graphical tests in non-graphical environment
BuildRequires:  xorg-x11-server-Xvfb

# TestGtk (module gtk)
# (not available; this would be the obsolete PyGTK for GTK2, which never
# supported Python 3)

# TestQt (module PyQt5.QtWidgets)
BuildRequires:  python3dist(pyqt5)

# TestXClip (executable xclip)
BuildRequires:  /usr/bin/xclip

# TestXSel (executable xsel)
# These tests *can* pass, but some of them are flaky. It would be nice to
# figure out why.
# BuildRequires:  /usr/bin/xsel

# TestWlClipboard (executable wl-copy)
# These would fail with:
#   Failed to connect to a Wayland server
#   error: XDG_RUNTIME_DIR not set in the environment.
# BuildRequires:  /usr/bin/wl-copy
# BuildRequires:  /usr/bin/wl-paste

# TestKlipper (executables klipper and qdbus)
# These would fail with:
#   Could not connect to D-Bus server:
#   org.freedesktop.DBus.Error.Spawn.ExecFailed: /usr/bin/dbus-launch
#   terminated abnormally without any error message
# and besides, klipper is not present in Fedora 40 and later.
# BuildRequires:  /usr/bin/klipper
# BuildRequires:  /usr/bin/qdbus

%description -n python3-pyperclip %{common_description}

%package -n python-pyperclip-doc
Summary:        Pyperclip documentation

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
%if ! 0%{?el8}
BuildRequires:  python3-sphinx-latex
%else
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(amsthm.sty)
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(article.cls)
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(cmap.sty)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(ctablestack.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(kvoptions.sty)
BuildRequires:  tex(luatex85.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(parskip.sty)
BuildRequires:  tex(polyglossia.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(titlesec.sty)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(utf8x.def)
BuildRequires:  tex(wrapfig.sty)
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-collection-latex
BuildRequires:  texlive-dvipng
BuildRequires:  texlive-dvisvgm
%endif
BuildRequires:  latexmk
%endif

%description -n python-pyperclip-doc
Documentation for pyperclip

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyperclip-%{version}
# Fix ends of line encoding
sed -i 's/\r$//' README.md docs/*

%build
%py3_build

%if %{with doc_pdf}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%py3_install

%check
%global __pytest /usr/bin/xvfb-run -a %{python3} -m pytest
# Explicitly skip backends that we know will fail in the mock environment if
# their dependencies happen to be present. See notes in the BuildRequires.
k="${k-}${k+ and }not TestGtk"
k="${k-}${k+ and }not TestKlipper"
k="${k-}${k+ and }not TestWlCLipboard"
k="${k-}${k+ and }not TestXSel"
%pytest -k "${k-}" -v

%files -n python3-pyperclip
%license LICENSE.txt
%doc AUTHORS.txt
%doc CHANGES.txt
%doc README.md
%{python3_sitelib}/pyperclip
%{python3_sitelib}/pyperclip-%{version}-py%{python3_version}.egg-info

%files -n python-pyperclip-doc
%license LICENSE.txt
%if %{with doc_pdf}
%doc docs/_build/latex/Pyperclip.pdf
%endif

%changelog
%autochangelog
