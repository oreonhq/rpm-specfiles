%global source0_hash 064f8d2c358895c7e0bea9ae956f8d46f3f057772cb97f2743a11d478a0f68a0

Name:           platform
Version:        2.1.0.1
Release:        25%{?dist}
Summary:        Platform support library used by libCEC and binary add-ons for Kodi

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/Pulse-Eight/platform/
Source0:        https://github.com/Pulse-Eight/%{name}/archive/p8-%{name}-%{version}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Patch0:         https://github.com/Pulse-Eight/platform/compare/p8-platform-2.1.0.1..a7cd0d5780ed80a4e70480d1650749f29e8a1fb2.diff

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-p8-%{name}-%{version}

cp -p %{SOURCE1} .

%build
# TODO: Please submit an issue to upstream (rhbz#2381364)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README.md
%license gpl-2.0.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/p8-%{name}/
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
