%global source0_hash a91df2e5038b7d5cc8cccbc2b3fd21fcc5acfffcf4e67792ccb4198c32d18562
Name:           ocaml-intrinsics-kernel
Version:        0.17.2
Release:        1%{?dist}
Summary:        OCaml interface to CPU intrinsics
License:        MIT
URL:            https://github.com/janestreet/ocaml_intrinsics_kernel
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ocaml_intrinsics_kernel/archive/v%{version}/ocaml_intrinsics_kernel-%{version}.tar.gz
Patch:          %{name}-popcnt.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
The ocaml_intrinsics_kernel library provides an OCaml interface to operations
that have dedicated hardware instructions on some micro-architectures.
Currently, it provides the following operations:

- conditional select

See ocaml_intrinsics for details.  Unlike ocaml_intrinsics,
ocaml_intrinsics_kernel can be used by programs compiled to javascript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ocaml_intrinsics_kernel-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-intrinsics-kernel-devel -f %{oreon_filedir}/ocaml-intrinsics-kernel-devel.list

%changelog

%autochangelog
