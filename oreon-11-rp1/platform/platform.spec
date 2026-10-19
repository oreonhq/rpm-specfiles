%global source1_hash edaef632cbb643e4e7a221717a6c441a4c1a7c918e6e4d56debc3d8739b233f6
%global source0_hash e1a0669e54793794afb5965d7d35a5456d8dbbda772fe505824c481279887ba0
Name:           platform
Version:        2.2.0
Release:        1%{?dist}
Summary:        Platform support library used by libCEC and binary add-ons for Kodi
License:        GPL-2.0-or-later
URL:            https://github.com/Pulse-Eight/platform/
Source0:        https://github.com/Pulse-Eight/%{name}/archive/p8-%{name}-%{version}.tar.gz
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Patch0:         https://github.com/Pulse-Eight/platform/compare/p8-platform-2.1.0.1..a7cd0d5780ed80a4e70480d1650749f29e8a1fb2.diff
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
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

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n platform-devel -f %{oreon_filedir}/platform-devel.list

%changelog

%autochangelog
