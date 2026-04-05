%global stable_kf6 stable

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kcachegrind
Summary: GUI to profilers such as Valgrind
Version: 25.12.3
Release:	2%{?dist}

# Automatically converted from old format: GPLv2 and GFDL - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/sdk/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

BuildRequires: desktop-file-utils
BuildRequires: perl-generators
BuildRequires: python3

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6DBusAddons)

BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Widgets)

%description
Browser for data produced by profiling tools (e.g. cachegrind)

%package converters
Summary: Converters for kcachegrind
Requires: %{name} = %{version}-%{release}
%description converters
%{summary}.

%package -n qcachegrind
Summary: QT GUI to profilers such as Valgrind

%description -n qcachegrind
QT-based browser for data produced by profiling tools (e.g. cachegrind).


%prep
%autosetup -p1

# Avoid use of #!/usr/bin/env as interpeter
sed -i.env -e "s|^#!/usr/bin/env python$|#!%{__python3}|g" converters/hotshot2calltree.in
sed -i.env -e "s|^#!/usr/bin/env php$|#!%{_bindir}/php|g"  converters/pprof2calltree


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
# qcachegrind needs manual installation
install -p -m 755 %{__cmake_builddir}/bin/qcachegrind %{buildroot}%{_bindir}/
install -p -m 755 %{__cmake_builddir}/bin/cgview %{buildroot}%{_bindir}/
install -p -m 644 qcachegrind/qcachegrind.desktop %{buildroot}%{_datadir}/applications/


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/qcachegrind.desktop

%find_lang %{name} --all-name --with-html
%find_lang_kf6 kcachegrind_qt
cat kcachegrind_qt.lang >> kcachegrind.lang


%files -f %{name}.lang
%doc README
%license LICENSES/*
%{_kf6_bindir}/kcachegrind
%{_kf6_datadir}/kcachegrind/
%{_kf6_datadir}/applications/org.kde.kcachegrind.desktop
%{_kf6_metainfodir}/org.kde.kcachegrind.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/kcachegrind.*

%files converters
%doc converters/README
# perl
%{_kf6_bindir}/dprof2calltree
%{_kf6_bindir}/memprof2calltree
%{_kf6_bindir}/op2calltree
# python
%{_kf6_bindir}/hotshot2calltree
# php
%{_kf6_bindir}/pprof2calltree

%files -n qcachegrind
%doc README
%license LICENSES/*
%{_bindir}/qcachegrind
%{_bindir}/cgview
%{_datadir}/applications/qcachegrind.desktop
# icons are shared with kcachegrind
%{_datadir}/icons/hicolor/*/apps/kcachegrind.*


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
