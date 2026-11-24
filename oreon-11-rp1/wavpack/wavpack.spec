# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b0038f515d322042aaa6bd352d437729c6f5f904363cc85bbc9b0d8bd4a81927
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?fedora}
%bcond_without mingw
%else
%bcond_with mingw
%endif

%global common_description %{expand:
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.}

Name:		wavpack
Summary:	A completely open audiocodec
Version:	5.9.0
Release:        %{autorelease}
License:	BSD-3-Clause AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain
Url:		https://www.wavpack.com/
Source0:        https://www.wavpack.com/%{name}-%{version}.tar.bz2
Patch1:		wavpack-0001-fix-for-MinGW.patch
Patch2:		wavpack-0002-We-compile-only-ANSI-C-sources.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cmake
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make

%if %{with mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
%endif

%description
%{common_description}

%package devel
Summary:	WavPack - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Files needed for developing apps using wavpack

%if %{with mingw}
%package -n mingw32-%{name}
Summary:        %{summary}
BuildArch:      noarch

%description -n mingw32-%{name}
%{common_description}

This package is MinGW compiled wavpack library for the Win32 target.

%package -n mingw32-%{name}-tools
Summary:        %{summary} tools
BuildArch:      noarch
Requires:       mingw32-%{name} = %{version}-%{release}

%description -n mingw32-%{name}-tools
%{common_description}

This package is MinGW compiled wavpack tools for the Win32 target.

%package -n mingw64-%{name}
Summary:        %{summary}
BuildArch:      noarch

%description -n mingw64-%{name}
%{common_description}

This package is MinGW compiled wavpack library for the Win64 target.

%package -n mingw64-%{name}-tools
Summary:        %{summary} tools
BuildArch:      noarch
Requires:       mingw64-%{name} = %{version}-%{release}

%description -n mingw64-%{name}-tools
%{common_description}

This package is MinGW compiled wavpack tools for the Win64 target.

%endif

%{?mingw_debug_package}

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake -DWAVPACK_ENABLE_ASM=OFF
%cmake_build

%if %{with mingw}
%mingw_cmake -DWAVPACK_ENABLE_ASM=OFF
%mingw_make_build
%endif

%install
%cmake_install
rm -f %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_docdir}/

%if %{with mingw}
%mingw_make_install
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{mingw64_mandir}
%endif

%{?mingw_debug_install_post}

%files
%{_bindir}/*
%{_libdir}/libwavpack.so.*
%{_mandir}/man1/wavpack.1*
%{_mandir}/man1/wvgain.1*
%{_mandir}/man1/wvunpack.1*
%{_mandir}/man1/wvtag.1*
%doc AUTHORS doc/wavpack_doc.html doc/style.css
%license COPYING

%files devel
%{_includedir}/*
%{_libdir}/cmake/WavPack/
%{_libdir}/pkgconfig/*
%{_libdir}/libwavpack.so
%doc ChangeLog doc/WavPack5PortingGuide.pdf doc/WavPack5LibraryDoc.pdf doc/WavPack5FileFormat.pdf

%if %{with mingw}
%files -n mingw32-wavpack
%doc AUTHORS
%license COPYING
%dir %{mingw32_includedir}/wavpack
%{mingw32_bindir}/libwavpack-1.dll
%{mingw32_includedir}/wavpack/*.h
%{mingw32_libdir}/cmake/WavPack/
%{mingw32_libdir}/libwavpack.dll.a
%{mingw32_libdir}/pkgconfig/*

%files -n mingw32-wavpack-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-wavpack
%doc AUTHORS
%license COPYING
%dir %{mingw64_includedir}/wavpack
%{mingw64_bindir}/libwavpack-1.dll
%{mingw64_includedir}/wavpack/*.h
%{mingw64_libdir}/cmake/WavPack/
%{mingw64_libdir}/libwavpack.dll.a
%{mingw64_libdir}/pkgconfig/*

%files -n mingw64-wavpack-tools
%{mingw64_bindir}/*.exe
%endif

%changelog
%autochangelog
