%bcond svn %{undefined flatpak}

%global stable_kf6 stable

Name:           kdevelop
Summary:        Integrated Development Environment for C++/C
Epoch:          9
Version:        25.12.3
Release:        1%{?dist}
License:        GPL-2.0-only
URL:            https://www.kdevelop.org/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
Source10:       macros.kdevelop

# upstreamable patches

# upstream patches

# depends on qt6-qtwebengine, which is only available on some arches
ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  gcc-c++ gcc
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

# top-level library dependencies
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextWidgets)

BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(KDevelop-PG-Qt) >= 2.3.0

BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(shared-mime-info)

# kdevplatform
BuildRequires:  boost-devel
# kdevplatform/documentation
BuildRequires:  cmake(Qt6WebEngineWidgets)

# app/plasma
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KF6Runner)

# plugins/astyle
BuildRequires:  astyle-devel
# plugins/clang
BuildRequires:  cmake(Clang)
BuildRequires:  cmake(LLVM)
# plugins/clazy
BuildRequires:  clazy
# plugins/cppcheck
BuildRequires:  cppcheck
# plugins/gdb (not yet ported to Qt6)
#BuildRequires:  cmake(OktetaGui)
# plugins/heaptrack
BuildRequires:  heaptrack
# plugins/meson
BuildRequires:  meson
# plugins/patchreview
BuildRequires:  cmake(KompareDiff2)
BuildRequires:  cmake(KF6Purpose)
# plugins/qthelp
BuildRequires:  cmake(Qt6Help)
%if %{with svn}
# plugins/subversion
BuildRequires:  subversion-devel
%endif

Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: astyle
Requires: cmake
Requires: cppcheck
Requires: git
Requires: konsole-part
Recommends: clang-tools-extra
Recommends: clazy
Recommends: heaptrack
Recommends: meson

%description
The KDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to programs
like gdb, the C/C++ compiler, and make. KDevelop manages or provides:

All development tools needed for C++ programming like Compiler,
Linker, automake and autoconf; KAppWizard, which generates complete,
ready-to-go sample applications; Classgenerator, for creating new
classes and integrating them into the current project; File management
for sources, headers, documentation etc. to be included in the
project; The creation of User-Handbooks written with SGML and the
automatic generation of HTML-output with the KDE look and feel;
Automatic HTML-based API-documentation for your project's classes with
cross-references to the used libraries; Internationalization support
for your application, allowing translators to easily add their target
language to a project;

KDevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.


%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: cmake(KF6TextEditor)
Requires: cmake(KF6ThreadWeaver)
Requires: cmake(Qt6Core5Compat)
Requires: cmake(Qt6WebEngineWidgets)
Requires: cmake(Qt6Test)
%description devel
%{summary}.

%package libs
Summary: %{name} runtime libraries
%description libs
%{summary}.


%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name

# rpm macros
install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{rpm_macros_dir}/macros.kdevelop
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch}:}%{version}-%{release}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.kdevelop

# drop zsh, using bash as default
rm -f %{buildroot}%{_datadir}/kdevplatform/shellutils/.zshrc

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kdevelop.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.kdevelop.appdata.xml


%files -f %{name}.lang
%doc AUTHORS
%license COPYING.DOC
%{_bindir}/kdevelop
%{_bindir}/kdevelop!
%{_bindir}/kdev_includepathsconverter
%{_bindir}/kdev_dbus_socket_transformer
%{_bindir}/kdevplatform_shell_environment.sh
%{_bindir}/kdev_format_source
%{_datadir}/kdev*/
%{_datadir}/applications/org.kde.kdevelop.desktop
%{_datadir}/applications/org.kde.kdevelop_ps.desktop
%{_datadir}/applications/org.kde.kdevelop_bzr.desktop
%{_datadir}/applications/org.kde.kdevelop_git.desktop
%{_datadir}/applications/org.kde.kdevelop_kdev4.desktop
%if %{with svn}
%{_datadir}/applications/org.kde.kdevelop_svn.desktop
%endif
%{_datadir}/mime/packages/kdevelop.xml
%{_datadir}/mime/packages/kdevclang.xml
%{_datadir}/mime/packages/kdevgit.xml
%{_datadir}/plasma/plasmoids/org.kde.kdevelopsessions/*
%{_datadir}/knotifications6/kdevelop.notifyrc
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/qlogging-categories6/kdevelop.categories
%{_datadir}/qlogging-categories6/kdevplatform.categories
%{_datadir}/bash-completion/completions/kdevelop
%{_datadir}/knsrcfiles/kdev*.knsrc
%{_docdir}/HTML/*/kdevelop/
%{_metainfodir}/org.kde.kdevelop.appdata.xml
%{_qt6_qmldir}/org/kde/plasma/private/kdevelopsessions/libkdevelopsessionsplugin.so
%{_qt6_qmldir}/org/kde/plasma/private/kdevelopsessions/qmldir

%files libs
%{_libdir}/libKDev*.so.{61,62,63,64,6.*}
%{_libdir}/libKDevelopSessionsWatch.so
%{_kf6_qtplugindir}/kdevplatform/
%{_kf6_plugindir}/krunner/kdevelopsessions.so
%{_kf6_plugindir}/ktexttemplate/kdev_filters.so

%files devel
%{_libdir}/cmake/KDevelop/
%{_libdir}/cmake/KDevPlatform
%{_includedir}/kdevelop/
%{_includedir}/kdevplatform/
%exclude %{_libdir}/libKDevelopSessionsWatch.so
%{_libdir}/libKDev*.so
%{rpm_macros_dir}/macros.kdevelop

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
