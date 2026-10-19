%global source0_hash 44559bcd0f4f165ed7dbe2f78af0a2e10068e681174f632440264c52608c02d5
%global qt_module qtconfiguration
%undefine __cmake_in_source_build
Summary:        Qt5 - QtConfiguration module
Name:           qt5-%{qt_module}
Version:        0.3.1
Release:        1%{?dist}
License:        LGPL-2.0-or-later WITH FLTK-exception OR LicenseRef-Callaway-GPLv3-with-exceptions
URL:            https://github.com/mauios/qtconfiguration
Source0:        https://github.com/mauios/%{qt_module}/archive/refs/tags/v%{version}/%{qt_module}-%{version}.tar.gz
%global source0_hash 44559bcd0f4f165ed7dbe2f78af0a2e10068e681174f632440264c52608c02d5
Patch1: qtconfiguration-0.3.1-glib2_extern.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(dconf)
# /oreon:deps
%description
Settings API with change notifications.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{qt_module}-%{version} -p1

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtconfiguration-devel -f %{oreon_filedir}/qt5-qtconfiguration-devel.list

%changelog

%autochangelog
