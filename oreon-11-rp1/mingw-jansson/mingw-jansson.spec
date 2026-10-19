%global source0_hash 979210eaffdffbcf54cfc34d047fccde13f21b529a381df26db871d886f729a4
%{?mingw_package_header}
%global pkgname jansson
Name:           mingw-%{pkgname}
Version:        2.14.1
Release:        1%{?dist}
Summary:        C library for encoding, decoding and manipulating JSON data
License:        MIT 
URL:            https://github.com/akheron/jansson
Source0:        https://github.com/akheron/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
Patch0:         jansson-cmakedir.patch
Patch1:         jansson-cmakever.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
Small library for parsing and writing JSON documents.

%package -n mingw32-%{pkgname}
Summary:        C library for encoding, decoding and manipulating JSON data
%description -n mingw32-%{pkgname}
Small library for parsing and writing JSON documents.

%package -n mingw64-%{pkgname}
Summary:        C library for encoding, decoding and manipulating JSON data
%description -n mingw64-%{pkgname}
Small library for parsing and writing JSON documents.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build

%mingw_cmake \
  -DJANSSON_BUILD_SHARED_LIBS=ON -DJANSSON_EXAMPLES=OFF \
  -DJANSSON_WITHOUT_TESTS=ON -DJANSSON_BUILD_DOCS=OFF \
  -DCMAKE_DLL_NAME_WITH_SOVERSION=ON
%mingw_make_build
%install
%mingw_make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-jansson -f %{oreon_filedir}/mingw32-jansson.list
%files -n mingw64-jansson -f %{oreon_filedir}/mingw64-jansson.list

%changelog

%autochangelog
