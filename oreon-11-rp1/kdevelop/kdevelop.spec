%global source0_hash dd77921d7e403bfbb60bfa8a7998a2e2c1eb53ab7b4b1a2f8a52360493c586ab
%global stable_kf6 stable
%bcond svn %{undefined flatpak}
Name:           kdevelop
Summary:        Integrated Development Environment for C++/C
Epoch:          9
Version:        26.08.1
Release:        1%{?dist}
License:        GPL-2.0-only
URL:            https://www.kdevelop.org/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
Source10:       macros.kdevelop
ExclusiveArch:  %{qt6_qtwebengine_arches}
%if %{with svn}
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
# oreon:deps
BuildRequires:  astyle-devel
BuildRequires:  boost-devel
BuildRequires:  clazy
BuildRequires:  cmake(Clang)
BuildRequires:  cmake(KDevelop-PG-Qt)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(KompareDiff2)
BuildRequires:  cmake(LLVM)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cppcheck
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  heaptrack
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  subversion-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
cmake --build "%{_vpath_builddir}" -j${RPM_BUILD_NCPUS} -- -s
%install
%cmake_install
%find_lang %{name} --all-name
install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{rpm_macros_dir}/macros.kdevelop
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch}:}%{version}-%{release}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.kdevelop
rm -f %{buildroot}%{_datadir}/kdevplatform/shellutils/.zshrc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kdevelop.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.kdevelop.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n kdevelop-devel -f %{oreon_filedir}/kdevelop-devel.list
%files -n kdevelop-libs -f %{oreon_filedir}/kdevelop-libs.list

%changelog

%autochangelog
