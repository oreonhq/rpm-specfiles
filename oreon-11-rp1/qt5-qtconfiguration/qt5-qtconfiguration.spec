%global source0_hash 4c0b4474910b87436c5e680b797f49b5c08a8760b11a9eb0e353a50f57e3d47e

%global qt_module qtconfiguration

%undefine __cmake_in_source_build

Summary:        Qt5 - QtConfiguration module
Name:           qt5-%{qt_module}
Version:        0.3.1
Release:        28%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
# Automatically converted from old format: LGPLv2 with exceptions or GPLv3 with exceptions - review is highly recommended.
License:        LGPL-2.0-or-later WITH FLTK-exception OR LicenseRef-Callaway-GPLv3-with-exceptions
URL:            https://github.com/mauios/qtconfiguration
Source0:        http://downloads.sourceforge.net/project/mauios/hawaii/%{qt_module}/%{qt_module}-%{version}.tar.gz

# Fix FTBFS with newer gcc/glib2 combination, no longer need 'extern "C"' to include related headers
Patch1: qtconfiguration-0.3.1-glib2_extern.patch

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  cmake

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
# TODO: Please submit an issue to upstream (rhbz#2381394)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%{_libdir}/libqtconfiguration.so.0*
%{_libdir}/hawaii
%license LICENSE.FDL
%license LICENSE.GPL
%license LICENSE.LGPL
%doc README.md

%files devel
%{_includedir}/QtConfiguration/
%{_libdir}/libqtconfiguration.so
%{_libdir}/cmake/QtConfiguration/

%changelog
%autochangelog
