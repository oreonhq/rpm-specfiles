%global source0_hash 61456c5736a4c8f3df6035c4222df99a7c110fe7f80f5c66b1a8cc10577d176e
%global gap_pkgname automata
%global giturl      https://github.com/gap-packages/automata
Name:           gap-pkg-%{gap_pkgname}
Version:        1.17
Release:        1%{?dist}
Summary:        Finite automata algorithms
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/automata/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst version
BuildOption(check): tst/testall.g
Requires:       gap-core
Recommends:     coreutils
Recommends:     graphviz
Recommends:     xdg-utils
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
This package contains algorithms for working with finite automata in GAP.  It
can do the following:
- compute a rational expression for the language recognized by a finite
  automaton;
- compute an automaton for the language given by a rational expression;
- minimalize a finite automaton;
- visualize automata.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Finite automata documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-automata-doc -f %{oreon_filedir}/gap-pkg-automata-doc.list

%changelog

%autochangelog
