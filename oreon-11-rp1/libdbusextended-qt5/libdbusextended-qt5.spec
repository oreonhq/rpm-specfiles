%global source0_hash e9342979e32a1997b14e3bb3cd980619e8320c495873342d3b5eb30eb6f16b6a

%global repo qtdbusextended

Name:           libdbusextended-qt5
Summary:        Extended DBus for Qt
Version:        0.0.3
Release:        18%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/nemomobile/qtdbusextended
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires: make

%description
%{summary}.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{repo}-%{version}

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_libdir}/lib*.so.1*

%files devel
%dir %{_qt5_includedir}/DBusExtended/
%{_qt5_includedir}/DBusExtended/DBusExtended
%{_qt5_includedir}/DBusExtended/DBusExtendedAbstractInterface
%{_qt5_includedir}/DBusExtended/dbusextended.h
%{_qt5_includedir}/DBusExtended/dbusextendedabstractinterface.h
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
%autochangelog
