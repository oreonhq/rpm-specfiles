%global source0_hash 8e36013b257e946542810bd66fad815b2c941903ceaafdea9a060b388bd38797
ExcludeArch: %{ix86}
%global giturl  https://github.com/thvnx/mlmpfr
Name:           ocaml-mlmpfr
Version:        4.2.1
Release:        12%{?dist}
Summary:        OCaml bindings for MPFR
License:        LGPL-3.0-only
URL:            https://thvnx.github.io/mlmpfr/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/mlmpfr.%{version}.tar.gz
Patch:          %{name}-internals.patch
Patch:          %{name}-dune.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(mpfr)
# /oreon:deps
%description
This library provides OCaml bindings for MPFR.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mpfr-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mlmpfr-mlmpfr.%{version}
%oreon_prep
%build

cd utils
gcc %{build_cflags} %{build_ldflags} mlmpfr_compatibility_test.c \
    -o mlmpfr_compatibility_test -lmpfr
./mlmpfr_compatibility_test
cd -
%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-mlmpfr-devel -f %{oreon_filedir}/ocaml-mlmpfr-devel.list

%changelog

%autochangelog
