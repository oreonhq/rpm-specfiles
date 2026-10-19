%global source0_hash ab1555fe5adc3f99f1d4a1a0eb1596d329fd6d74f1464a0097c81f53c0cf9e5c
%ifnarch s390x
%bcond_without check
%else
%bcond_with check
%endif
%global _smp_mflags -j1
%global abi 1
Name:           flite
Version:        2.2
Release:        1%{?dist}
Summary:        Small, fast speech synthesis engine (text-to-speech)
License:        MIT
URL:            http://cmuflite.org/
Source0:        https://github.com/festvox/flite/archive/refs/tags/v%{version}.tar.gz#/flite-%{version}.tar.gz
Patch0:         flite-2.2-lto.patch
Patch1:         flite-2.2-texinfo-7.0.patch
Patch2:         flite-2.2-parallel-make.patch
Patch3:         flite-2.2-tests.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ed
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  texinfo
# /oreon:deps
%description
Flite (festival-lite) is a small, fast run-time speech synthesis engine
developed at CMU and primarily designed for small embedded machines and/or
large servers. Flite is designed as an alternative synthesis engine to
Festival for voices built using the FestVox suite of voice building tools.

%package devel
Summary: Development files for flite
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for Flite, a small, fast speech synthesis engine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .lto
%patch -P1 -p1 -b .ti7
%patch -P2 -p1 -b .pmake
%patch -P3 -p1 -b .tst

%build

autoreconf -vif
%configure \
    --enable-shared \
    --with-audio=pulseaudio \
%make_build
cd doc
make flite.html
%install
%make_install
rm %{buildroot}%{_libdir}/libflite*.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} make check
%endif
%files -f %{oreon_filedir}/main.list
%files -n flite-devel -f %{oreon_filedir}/flite-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2-13
- Prepare for Oreon 11 (RP1)
