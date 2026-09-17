%global source0_hash 59c9040e9258a5d0652b04acd0e276a3c662ab43e5718cf8e0cf600df64dc369

%global repo dde-application-manager

Name:           deepin-application-manager
Version:        1.2.39
Release:        %autorelease
Summary:        App manager of Deepin Desktop Environment
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-application-manager
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(TreelandProtocols)
BuildRequires:  cmake(GTest)

BuildRequires:  pkgconfig(libsystemd)

%description
DDE Application Manager is the app manager of Deepin Desktop Environment.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}

%build
%cmake -GNinja -DBUILD_TESTING=ON
%cmake_build

%install
%cmake_install

rm %{buildroot}%{_libexecdir}/deepin/application-manager/app-update-notifier
rm %{buildroot}%{_datadir}/dbus-1/system-services/org.desktopspec.ApplicationUpdateNotifier1.service
rm %{buildroot}%{_datadir}/dbus-1/system.d/org.desktopspec.ApplicationUpdateNotifier1.conf
rm %{buildroot}%{_unitdir}/org.desktopspec.ApplicationUpdateNotifier1.service

%check
%ctest

%files
%doc README.md
%license LICENSES/*
%{_bindir}/app-identifier
%{_bindir}/dde-am
%{_bindir}/dde-application-manager
%{_prefix}/etc/dpkg/dpkg.cfg.d/am-update-hook
%{_userunitdir}/app-DDE-.service.d/override.conf
%{_userunitdir}/dde-session-initialized.target.wants/org.desktopspec.ApplicationManager1.service
%{_userunitdir}/dde-session.target.wants/dde-autostart.service
%{_userunitdir}/*.service
%{_libexecdir}/deepin/application-manager/
%{bash_completions_dir}/dde-am
%{_datadir}/dbus-1/services/org.desktopspec.ApplicationManager1.service
%dir %{_datadir}/dde-application-manager
%{_datadir}/dde-application-manager/*.xml
%{_datadir}/deepin/dde-application-manager/
%{_datadir}/dsg/configs/org.deepin.dde.application-manager/

%files devel
%{_libdir}/cmake/DDEApplicationManager/

%changelog
%autochangelog
