%global source0_hash 3a14cd126a977079de30c866061acf556af81bbb9f95689036e1e54bf2f3de0f
%undefine __cmake_in_source_build
Name: ampache_browser
%global vername %{name}_1
Version: 1.0.9
Release:        1%{?dist}
Summary:        C++ and Qt based client library for Ampache access
License: GPL-3.0-only
URL: http://ampache-browser.org
Source0:        https://github.com/ampache-browser/ampache_browser/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
Ampache Browser is a library that implements desktop client access to
the Ampache service (http://ampache.org). It provides end-user Qt UI and
has a simple C++ interface that allows easy integration into client
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake %{?el8:-D USE_QT6=OFF} .
%cmake_build
%install
%cmake_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles ampache_browser-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ampache_browser-devel -f %{oreon_filedir}/ampache_browser-devel.list

%changelog

%autochangelog
