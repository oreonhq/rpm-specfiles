Summary: Old version of libpng, needed to run old binaries
Name: libpng15
Version: 1.5.30
Release: 24%{?dist}
License: zlib
URL: http://www.libpng.org/pub/png/

# Note: non-current tarballs get moved to the history/ subdirectory,
# so look there if you fail to retrieve the version you want
Source0: https://ftp-osl.osuosl.org/pub/libpng/src/libpng15/libpng-%{version}.tar.xz

Source1: pngusr.dfa

Patch0: libpng15-CVE-2013-6954.patch
Patch1: libpng15-CVE-2018-13785.patch

BuildRequires: gcc
BuildRequires: zlib-devel
BuildRequires: make

%description
The libpng15 package provides libpng 1.5, an older version of the libpng.
library for manipulating PNG (Portable Network Graphics) image format files.
This version should be used only if you are unable to use the current
version of libpng.

%prep
%setup -q -n libpng-%{version}

%patch -P0 -p1
%patch -P1 -p1

# Provide pngusr.dfa for build.
cp -p %{SOURCE1} .

%build
%configure --disable-static
%make_build DFA_XTRA=pngusr.dfa

%install
%make_install

# We don't ship .la files.
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/libpng*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libpng.pc
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libpng15.pc
rm -rf $RPM_BUILD_ROOT%{_mandir}/*
rm -rf $RPM_BUILD_ROOT%{_includedir}/*
rm -rf $RPM_BUILD_ROOT%{_bindir}/*

%files
%doc LICENSE
%{_libdir}/libpng15.so.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.30-24
- Prepare for Oreon 11 (RP1)
