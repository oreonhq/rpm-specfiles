%global source0_hash ff0348266e897cffa4ee99b827b0e654224f955799ae86bb0fc96bf7af64ce5a
Name:           dot2tex
Version:        2.12.0
Release:        1%{?dist}
Summary:        A Graphviz to LaTeX converter
License:        MIT
URL:            http://www.fauskes.net/code/dot2tex/
Source0:        https://github.com/kjellmf/dot2tex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       tex(preview.sty)
Requires:       tex(tikz.sty)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dot2tex = %{version}-%{release}
# /oreon:deps
%description
Dot2tex is a tool for converting graphs rendered by Graphviz to formats
that can be used with LaTeX.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%pyproject_wheel
find docs examples -name "*.tex" -o -name "*.dot" | xargs sed -i -e 's|\r||'
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
