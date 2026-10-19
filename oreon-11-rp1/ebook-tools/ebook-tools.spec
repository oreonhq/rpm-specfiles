%global source0_hash cbc35996e911144fa62925366ad6a6212d6af2588f1e39075954973bbee627ae
%undefine __cmake_in_source_build
Name:           ebook-tools
Version:        0.2.2
Release:        1%{?dist}
Summary:        Tools and library for EPUB and LIT ebooks
License:        MIT
URL:            https://sourceforge.net/projects/ebook-tools/
Source0:        https://downloads.sourceforge.net/ebook-tools/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  libzip-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Utilities for working with common ebook formats plus the libepub shared
library.

%package -n ebook-tools-libs
Summary:        EPUB manipulation library
%description -n ebook-tools-libs
Shared library for ebook-tools.

%package -n ebook-tools-devel
Summary:        Development files for ebook-tools
Requires:       ebook-tools-libs%{?_isa} = %{version}-%{release}
%description -n ebook-tools-devel
Headers and libraries for libepub.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
%oreon_autofiles ebook-tools-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ebook-tools-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ebook-tools-libs -f %{oreon_filedir}/ebook-tools-libs.list
%files -n ebook-tools-devel -f %{oreon_filedir}/ebook-tools-devel.list

%changelog

* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.2-2
- Add ebook-tools for Okular and converters
