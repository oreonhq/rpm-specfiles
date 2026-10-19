%global source0_hash b6595ee187dea792b31fc54a0e1524ab1e48bc6068d3066c45215a138cc73b95
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ppx-derivers
Version:        1.2.1
Release:        1%{?dist}
Summary:        Deriving plugin registry
License:        BSD-3-Clause
URL:            https://github.com/ocaml-ppx/ppx_derivers
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-ppx/ppx_derivers/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
Ppx_derivers is a tiny package whose sole purpose is to allow
ppx_deriving and ppx_type_conv to inter-operate gracefully when
linked as part of the same ocaml-migrate-parsetree driver.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_derivers-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-derivers-devel -f %{oreon_filedir}/ocaml-ppx-derivers-devel.list

%changelog

%autochangelog
