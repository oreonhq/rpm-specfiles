Name:    khelpcenter
Summary: Show documentation for KDE applications
# Override khelpcenter subpackage from kde-runtime-15.04 (no longer built)
Epoch:   1
Version: 25.12.3
Release:	2%{?dist}

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License: GPL-2.0-only OR GPL-3.0-only
URL:     https://invent.kde.org/system/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6WebEngineWidgets)

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6TextTemplate)

BuildRequires:  libxml2-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  xapian-core-devel

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch: %{qt6_qtwebengine_arches}

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
# Provide khelpcenter service for KDE 3/4/5 applications
install -D -m0644 -t %{buildroot}%{_datadir}/services/ khelpcenter.desktop
install -D -m0644 -t %{buildroot}%{_datadir}/kde4/services/ khelpcenter.desktop
install -D -m0644 -t %{buildroot}%{_datadir}/kservices5/ khelpcenter.desktop

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
## currently fails on all RHEL releases
# RHEL8: https://bugzilla.redhat.com/show_bug.cgi?id=2107277
# RHEL9: https://bugzilla.redhat.com/show_bug.cgi?id=2107278
%if !0%{?rhel}
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
%endif

%files -f %{name}.lang
%doc README.metadata
%license LICENSES/*
%{_bindir}/%{name}
%{_kf6_datadir}/qlogging-categories6/%{name}.*
%{_libexecdir}/khc_mansearch.py
%{_libexecdir}/khc_xapianindexer
%{_libexecdir}/khc_xapiansearch
%{_kf6_datadir}/%{name}/
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/dbus-1/services/org.kde.%{name}.service
%{_datadir}/kservices5/%{name}.desktop
%{_datadir}/services/%{name}.desktop
%{_datadir}/kde4/services/%{name}.desktop


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
