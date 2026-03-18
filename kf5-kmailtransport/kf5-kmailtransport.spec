%global framework kmailtransport

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 23.08.5
Release: 8%{?dist}
Summary: The KMailTransport Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

%if %{undefined flatpak}
# /usr/share/config.kcfg/mailtransport.kcfg is used by both
# kf5-kmailtransport and (kf6-)kmailtransport, only the latter is being updated
Recommends:     kmailtransport >= 24.05.0
%endif

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cyrus-sasl-devel
%global kf5_ver 5.71
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Wallet)

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-ksmtp-devel >= %{majmin_ver}
BuildRequires:  kf5-libkgapi-devel >= %{majmin_ver}
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KPim5SMTP)

BuildRequires:  qt5-qtbase-devel

BuildRequires:  cmake(Qt5Keychain)

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

# http://bugzilla.redhat.com/1292325
Conflicts: kdepimlibs-akonadi < 4.14.10-4
# kio/smtp.so moved here
Conflicts: kf5-akonadi < 16.07

%description
%{summary}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kwallet-devel
Requires:       kf5-kmime-devel
Requires:       kf5-akonadi-mime-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html

%if %{undefined flatpak}
rm -f %{buildroot}%{_kf5_datadir}/config.kcfg/mailtransport.kcfg
%endif


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5MailTransport.so.*
%if %{defined flatpak}
%{_kf5_datadir}/config.kcfg/mailtransport.kcfg
%endif
%dir %{_kf5_qtplugindir}/pim5
%{_kf5_qtplugindir}/pim5/mailtransport/mailtransport_smtpplugin.so


%files devel
%{_includedir}/KPim5/MailTransport/
%{_kf5_libdir}/libKPim5MailTransport.so
%{_kf5_libdir}/cmake/KF5MailTransport/
%{_kf5_libdir}/cmake/KPim5MailTransport/
%{_kf5_archdatadir}/mkspecs/modules/qt_KMailTransport.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-8
- Prepare for Oreon 11 (RP1)
