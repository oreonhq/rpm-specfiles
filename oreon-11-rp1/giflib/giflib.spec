%global source0_hash b65b66b99f0424b93525f987386f22fc5efb9da2bfc92ad4a532249aaffbab0e

Name:          giflib
Summary:       A library and utilities for processing GIFs
Version:       6.1.3
Release:       2%{?dist}

License:       MIT
URL:           http://www.sourceforge.net/projects/%{name}/
Source:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Downstream cmake support
Source1:       CMakeLists.txt
# Fix several defects found by Coverity scan
Patch1:        giflib_coverity.patch
# Generate HTML docs with consistent section IDs to avoid multilib difference
Patch2:        giflib_html-docs-consistent-ids.patch
# Rename getarg.h to gif_getarg.h
# https://sourceforge.net/p/giflib/code/merge-requests/18/
Patch3:        getarg.patch
# Proposed fix for CVE-2026-26740
# https://sourceforge.net/p/giflib/bugs/199/
Patch4:        CVE-2026-26740.patch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: xmlto

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc


%description
giflib is a library for reading and writing gif images.


%package devel
Summary:       Development files for programs using the giflib library
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
The giflib-devel package includes header files, libraries necessary for
developing programs which use the giflib library.


%package utils
Summary:       Programs for manipulating GIF format image files
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description utils
The giflib-utils package contains various programs for manipulating GIF
format image files.

%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
Obsoletes:     mingw32-%{name}-static < %{version}-%{release}

%description -n mingw32-%{name}
%{summary}.


%package -n mingw32-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
Requires:      mingw32-%{name} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-%{name}-tools
%{summary}.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
Obsoletes:     mingw64-%{name}-static < %{version}-%{release}

%description -n mingw64-%{name}
%{summary}.


%package -n mingw64-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
Requires:      mingw64-%{name} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-%{name}-tools
%{summary}.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
cp -a %{SOURCE1} .

%build
# Native build
%cmake
%cmake_build

# MinGW build
%mingw_cmake
%mingw_make_build


%install
%cmake_install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}


%mingw_debug_install_post


%files
%doc ChangeLog NEWS README.adoc
%license COPYING
%{_libdir}/libgif.so.7*

%files devel
%doc doc/*
%{_libdir}/libgif.so
%{_includedir}/gif_lib.h
%{_includedir}/gif_getarg.h

%files utils
%{_bindir}/gif*
%{_mandir}/man1/*.1*

%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/libgif-7.dll
%{mingw32_includedir}/gif_lib.h
%{mingw32_includedir}/gif_getarg.h
%{mingw32_libdir}/libgif.dll.a

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/libgif-7.dll
%{mingw64_includedir}/gif_lib.h
%{mingw64_includedir}/gif_getarg.h
%{mingw64_libdir}/libgif.dll.a

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/*.exe


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.1.3-2
- Import
