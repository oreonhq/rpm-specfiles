%global source0_hash b65b66b99f0424b93525f987386f22fc5efb9da2bfc92ad4a532249aaffbab0e
Name:          giflib
Summary:        A library and utilities for processing GIFs
Version:       6.1.3
Release:        2%{?dist}
License:       MIT
URL:           http://www.sourceforge.net/projects/%{name}/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:       CMakeLists.txt
Patch1:        giflib_coverity.patch
Patch2:        giflib_html-docs-consistent-ids.patch
Patch3:        getarg.patch
Patch4:        CVE-2026-26740.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  xmlto
# /oreon:deps
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

%cmake
%cmake_build
%mingw_cmake
%mingw_make_build
%install
%cmake_install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
%mingw_debug_install_post
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n giflib-devel -f %{oreon_filedir}/giflib-devel.list
%files -n giflib-utils -f %{oreon_filedir}/giflib-utils.list
%files -n mingw32-giflib -f %{oreon_filedir}/mingw32-giflib.list
%files -n mingw32-giflib-tools -f %{oreon_filedir}/mingw32-giflib-tools.list
%files -n mingw64-giflib -f %{oreon_filedir}/mingw64-giflib.list
%files -n mingw64-giflib-tools -f %{oreon_filedir}/mingw64-giflib-tools.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.1.3-2
- Import
