%global source0_hash 0f4620e11fa283fedafb474427c8e96bf149511a1804bdc47350963ae5cf54d8
Summary:        Old version of libpng, needed to run old binaries
Name: libpng12
Version: 1.2.57
Release:        1%{?dist}
License: zlib
URL: http://www.libpng.org/pub/png/
Obsoletes: libpng-compat <= 2:1.5.10
Source0:        https://src.fedoraproject.org/repo/pkgs/libpng12/libpng-%{version}.tar.xz/sha512/51338d900690fc2d28ea1b5b364d311d73ce7ad498d000985e0c3926b5df0df97fcd7bb079fc954c6caa532fc6e6cbbc266e671d62fc67eca30e79a5f0e26f31/libpng-%{version}.tar.xz
Patch0: libpng12-multilib.patch
Patch1: libpng12-pngconf.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
# /oreon:deps
%description
The libpng12 package provides libpng 1.2, an older version of the libpng
library for manipulating PNG (Portable Network Graphics) image format files.
This version should be used only if you are unable to use the current
version of libpng.

%package devel
Summary: Development files for libpng 1.2
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: zlib-devel%{?_isa}
%description devel
The libpng12-devel package contains header files and documentation necessary
for developing programs using libpng12.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libpng-%{version}

%patch -P0 -p1
%patch -P1 -p1

%build

%configure \
  --disable-static \
  --without-libpng-compat
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -fv $RPM_BUILD_ROOT%{_libdir}/libpng*.la
rm -fv $RPM_BUILD_ROOT%{_mandir}/man5/*
rm -fv $RPM_BUILD_ROOT%{_bindir}/libpng-config
rm -fv $RPM_BUILD_ROOT%{_includedir}/{png,pngconf}.h
rm -fv $RPM_BUILD_ROOT%{_libdir}/libpng.so
rm -fv $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libpng.pc
rm -fv $RPM_BUILD_ROOT%{_mandir}/man3/{libpng,libpngpf}.3*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libpng12-devel -f %{oreon_filedir}/libpng12-devel.list

%changelog

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.57-25
- Source0: use pnggroup/libpng GitHub tag archive (SourceForge 404 for 1.2.57)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.57-24
- Prepare for Oreon 11 (RP1)
