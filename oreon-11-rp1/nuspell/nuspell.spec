%global source0_hash 658a28d2c622b6da5271544043a5b7b3e09881be8516a23efc11c43971b4b046
Name:           nuspell
Version:        5.1.9
Release:        1%{?dist}
Summary:        Fast and safe spellchecking C++ library and command-line tool
License:        LGPL-3.0-or-later
URL:            https://nuspell.github.io
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         nuspell-dllver.patch
Requires:       hunspell-en-US
# oreon:deps
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-icu
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-icu
BuildRequires:  pandoc
# /oreon:deps
%description
Nuspell is a fast and safe spelling checker software program. It is designed \
for languages with rich morphology and complex word compounding. Nuspell is \
written in modern C++ and it supports Hunspell dictionaries.

%package devel
Summary:        Development tools for %{name}
Requires:       libicu-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains the header files and developer docs for \
%{name}.

%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
%description -n mingw64-%{name}
MinGW Windows %{name} library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%mingw_cmake -DBUILD_TESTING=OFF
%mingw_make_build
%install
%cmake_install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_docdir}/%{name}
rm -rf %{buildroot}%{mingw64_docdir}/%{name}
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
%mingw_debug_install_post
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n nuspell-devel -f %{oreon_filedir}/nuspell-devel.list
%files -n mingw32-nuspell -f %{oreon_filedir}/mingw32-nuspell.list
%files -n mingw64-nuspell -f %{oreon_filedir}/mingw64-nuspell.list

%changelog

%autochangelog

