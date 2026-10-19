%global source0_hash 5b0910b5dab8ec63633be5dbf92a3e4863d415d803cad9dddf99dba43ce7498b
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-sexplib0
Version:        0.17.0
Release:        1%{?dist}
Summary:        Definition of S-expressions and some base converters
License:        MIT
URL:            https://github.com/janestreet/sexplib0
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/sexplib0/archive/v%{version}/sexplib0-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This package contains a library with the definition of S-expressions and some
base converters.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sexplib0-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-sexplib0-devel -f %{oreon_filedir}/ocaml-sexplib0-devel.list

%changelog

%autochangelog
