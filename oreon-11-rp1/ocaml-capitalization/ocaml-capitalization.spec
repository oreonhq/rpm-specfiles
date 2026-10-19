%global source0_hash f71d45ec929c9fc9b08e07723c15b6663b0143c4465b5d93038f653258cd5c6f
Name:           ocaml-capitalization
Version:        0.17.0
Release:        1%{?dist}
Summary:        Case conventions and functions to rename identifiers
License:        MIT
URL:            https://github.com/janestreet/capitalization
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/capitalization/archive/v%{version}/capitalization-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-base-devel
# /oreon:deps
%description
This library provides helper functions for formatting words using common
naming conventions, such as snake_case, camelCase, and PascalCase.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppx-base-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir capitalization-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-capitalization-devel -f %{oreon_filedir}/ocaml-capitalization-devel.list

%changelog

%autochangelog
