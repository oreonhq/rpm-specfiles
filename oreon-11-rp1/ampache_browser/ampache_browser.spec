%global source0_hash 178e1d16a4dfe7cc46289362b46d6f4896b896b7b48e8bf0c06677f07222506d

# Force out of source build
%undefine __cmake_in_source_build

Name: ampache_browser

# Lib and several dirs use this derived name. A change of this name
# is likely to break API users due to not finding files any longer.
%global vername %{name}_1

Version: 1.0.8
Release: 5%{?dist}
Summary: C++ and Qt based client library for Ampache access

License: GPL-3.0-only
URL: http://ampache-browser.org
Source0: https://github.com/ampache-browser/ampache_browser/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: qt6-qtbase-devel
%else
BuildRequires: gcc-toolset-12
BuildRequires: qt5-qtbase-devel
%endif

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

%autosetup -p1

%build
%if 0%{?rhel} == 8
. /opt/rh/gcc-toolset-12/enable
%endif

%cmake %{?el8:-D USE_QT6=OFF} .
%cmake_build

%install
%cmake_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/lib%{vername}.so.*

%files devel
%dir %{_includedir}/%{vername}
%{_includedir}/%{vername}/%{name}/
%{_libdir}/lib%{vername}.so
%{_libdir}/pkgconfig/%{vername}.pc
%{_libdir}/cmake/%{vername}

%changelog
%autochangelog
