%global source0_hash c113c5df2119ddf41a38a26db435c63f3224cc2b50b5b1313c4791a085da33ad
%global gap_pkgname typeset
%global giturl      https://github.com/gap-packages/typeset
Name:           gap-pkg-%{gap_pkgname}
Version:        1.2.4
Release:        1%{?dist}
Summary:        Automatic typesetting framework for common GAP objects
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/typeset/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): demo gap tst
BuildOption(check): tst/testall.g
Requires:       dot2tex
Requires:       gap-core
Requires:       graphviz
Recommends:     gap-pkg-digraphs
# oreon:deps
BuildRequires:  dot2tex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-digraphs-doc
BuildRequires:  graphviz
# /oreon:deps
%description
This package implements a framework for automatic typesetting of common GAP
objects, for the purpose of embedding them nicely into research papers.
Currently, an example implementation has been written specifically for LaTeX.

%package doc
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Documentation for the GAP typeset package
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-digraphs-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-typeset-doc -f %{oreon_filedir}/gap-pkg-typeset-doc.list

%changelog

%autochangelog
