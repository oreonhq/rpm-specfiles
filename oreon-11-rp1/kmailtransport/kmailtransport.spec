%global source0_hash fea7cd107ddc2199e8c104eba00eb8469ffaaccd67ce4e403917971d23e4c675

Name:    kmailtransport
Version: 26.08.0
Release: 1%{?dist}
Summary: The KMailTransport Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Wallet)

BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6SMTP)
BuildRequires:  cmake(KPim6GAPI)

BuildRequires:  cmake(Qt6Core)

BuildRequires:  cmake(Qt6Keychain)

# /usr/share/config.kcfg/mailtransport.kcfg is co-owned with kf5-kmailtransport
# when it changes here we need to backport changes to the kf5 version and conflict.
Conflicts:      kf5-kmailtransport < 23.08.5-2

%description
%{summary}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Mime)
Requires:       cmake(KPim6AkonadiMime)
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

%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libmailtransport5.po -execdir mv {} libmailtransport6.po \;


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6MailTransport.so.*
%{_kf6_datadir}/config.kcfg/mailtransport.kcfg
%dir %{_kf6_qtplugindir}/pim6
%{_kf6_qtplugindir}/pim6/mailtransport/mailtransport_smtpplugin.so


%files devel
%{_includedir}/KPim6/MailTransport/
%{_kf6_libdir}/libKPim6MailTransport.so
%{_kf6_libdir}/cmake/KPim6MailTransport/

%files doc

%changelog
* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 26.08.0-1
- Latest upstream release

%autochangelog

