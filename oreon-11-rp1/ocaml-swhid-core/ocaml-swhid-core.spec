%global source0_hash 8718b4eb97c9f0acd6d9162a9efa2f6af82474a0bd186f622fda3294f773bccf
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%global giturl  https://github.com/OCamlPro/swhid_core
Name:           ocaml-swhid-core
Version:        0.1
Release:        1%{?dist}
Summary:        Library for persistent identifiers used by Software Heritage
License:        ISC
URL:            https://ocamlpro.github.io/swhid_core/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/swhid_core-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
swhid_core is an OCaml library to work with persistent identifiers used by
Software Heritage, also known as swhid.  This is the core library; for most
use cases you should use the swhid library instead.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir swhid_core-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-swhid-core-devel -f %{oreon_filedir}/ocaml-swhid-core-devel.list

%changelog

%autochangelog
