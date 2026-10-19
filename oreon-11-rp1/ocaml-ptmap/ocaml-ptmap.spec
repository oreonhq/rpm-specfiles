%global source0_hash ebd1f8afe8679a226fdcbcdb323788e6f63db57521b151473f2ff8c05c30f3aa
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%global giturl  https://github.com/backtracking/ptmap
Name:           ocaml-ptmap
Version:        2.0.5
Release:        1%{?dist}
Summary:        Maps over integers implemented as Patricia trees
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://backtracking.github.io/ptmap/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/%{version}/ptmap-%{version}.tbz
Patch:          %{name}-compat.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
OCaml implementation of an efficient maps over integers, from a paper by Chris
Okasaki.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ptmap-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ptmap-devel -f %{oreon_filedir}/ocaml-ptmap-devel.list

%changelog

%autochangelog
