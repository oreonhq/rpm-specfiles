%global source0_hash 06eff884b629ce30704d08fb4559e54812e8c234e6086da770ea693613fe9780
ExcludeArch: %{ix86}
%global giturl  https://github.com/ACoquereau/psmt2-frontend
Name:           ocaml-psmt2-frontend
Version:        0.4.0
Release:        1%{?dist}
Summary:        Parser and typechecker for an extension of SMT-LIB 2
License:        Apache-2.0
URL:            https://acoquereau.github.io/psmt2-frontend/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/psmt2-frontend-%{version}.tar.gz
Patch:          %{name}-sphinx6.patch
# oreon:deps
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-menhir
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
# /oreon:deps
%description
This package contains a library to parse and typecheck a conservative
extension of the SMT-LIB 2 standard with prenex polymorphism.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%package        docs
Summary:        Documentation for %{name}
%description    docs
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n psmt2-frontend-%{version} -p1

%conf
# Do not use git to find the version; we don't have a git checkout
sed -i '/^git =/d;/^branch=/d;s/^\(version = \).*/\1"%{version}"/' sphinx/conf.py

%build

%dune_build
make sphinx
%install
%dune_install
cat > %{buildroot}%{ocamldir}/psmt2-frontend_bin/META << EOF
version = "%{version}"
description = "PSMT2 command line tool"
requires = ""
EOF
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-psmt2-frontend-devel -f %{oreon_filedir}/ocaml-psmt2-frontend-devel.list
%files -n ocaml-psmt2-frontend-docs -f %{oreon_filedir}/ocaml-psmt2-frontend-docs.list

%changelog

%autochangelog
