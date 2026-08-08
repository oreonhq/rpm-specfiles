%global source0_hash 089f1b24839a66b234e987f9eb71aca9efe20c2e9d8dd7387f24c14cbff37bf5

Name:    libkdepim
Version: 26.04.3
Release: 1%{?dist}
Summary: Library for common kdepim apps

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Libkdepim.so.6
%{_kf6_libdir}/libKPim6Libkdepim.so.6.*

%files devel
%{_includedir}/KPim6/Libkdepim/
%{_kf6_libdir}/cmake/KPim6Libkdepim/
%{_kf6_libdir}/cmake/KPim6MailTransportDBusService/
%{_kf6_libdir}/libKPim6Libkdepim.so
%{_kf6_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml
%{_kf6_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml
%{_kf6_qtplugindir}/designer/kdepim6widgets.so
 
%files doc

%changelog
%autochangelog

