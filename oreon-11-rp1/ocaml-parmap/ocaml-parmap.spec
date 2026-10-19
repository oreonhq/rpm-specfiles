%global source0_hash 6709356e724436fba0b7a10f96f65a441c2b763832954707d5e30017e78fd285
ExcludeArch: %{ix86}
%global giturl  https://github.com/rdicosmo/parmap
Name:           ocaml-parmap
Version:        1.2.5
Release:        1%{?dist}
Summary:        OCaml library for exploiting multicore architectures
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://rdicosmo.github.io/parmap/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/parmap-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-graphics-devel
# /oreon:deps
%description
Parmap is a minimalistic library for exploiting multicore architectures in
OCaml programs with minimal modifications: if you want to use your many cores
to accelerate an operation which happens to be a map, fold or map/fold
(map-reduce), just use Parmap's parmap, parfold and parmapfold primitives in
place of the standard `List.map` and friends, and specify the number of
subprocesses to use with the optional parameter `~ncores`.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir parmap-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%ifarch %{ocaml_native_compiler}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-parmap-devel -f %{oreon_filedir}/ocaml-parmap-devel.list

%changelog

%autochangelog
