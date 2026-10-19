%global source0_hash 9b9644d7351db699e57ddba7c767bb4153e6e988ccf45ead2fb238a3bd75cdc7
ExcludeArch: %{ix86}
%ifarch %{ocaml_native_compiler}
%undefine _debugsource_packages
%else
%global debug_package %{nil}
%endif
Name:           ocaml-compiler-libs-janestreet
Version:        0.17.0
Release:        1%{?dist}
Summary:        OCaml compiler libraries repackaged
License:        MIT
URL:            https://github.com/janestreet/ocaml-compiler-libs
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ocaml-compiler-libs/archive/v%{version}/ocaml-compiler-libs-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This package exposes the OCaml compiler libraries repackaged under the
toplevel names Ocaml_common, Ocaml_bytecomp, Ocaml_optcomp, etc.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ocaml-compiler-libs-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-compiler-libs-janestreet-devel -f %{oreon_filedir}/ocaml-compiler-libs-janestreet-devel.list

%changelog

%autochangelog
