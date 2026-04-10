
%global qt_module qtvirtualkeyboard

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - VirtualKeyboard component
Name:    qt6-%{qt_module}
Version: 6.10.2
Release: 5%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

## upstreamable patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: qt6-qtmultimedia-devel >= %{version}
BuildRequires: qt6-qtsvg-devel >= %{version}
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: openssl-devel
BuildRequires: hunspell-devel

# version unknown
Provides: bundled(libpinyin)

%description
The Qt Virtual Keyboard project provides an input framework and reference keyboard frontend
for Qt 6.  Key features include:
* Customizable keyboard layouts and styles with dynamic switching.
* Predictive text input with word selection.
* Character preview and alternative character view.
* Automatic capitalization and space insertion.
* Scalability to different resolutions.
* Support for different character sets (Latin, Simplified/Traditional Chinese, Hindi, Japanese, Arabic, Korean, and others).
* Support for most common input languages, with possibility to easily extend the language support.
* Left-to-right and right-to-left input.
* Hardware key support for 2-way and 5-way navigation.
* Handwriting support, with gestures for fullscreen input.
* Audio feedback.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build


%install
%cmake_install

%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6HunspellInputMethod.so.6*
%{_qt6_libdir}/libQt6VirtualKeyboard.so.6*
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.so.6*
%{_qt6_libdir}/libQt6VirtualKeyboardQml.so.6*
%{_qt6_plugindir}/platforminputcontexts/libqtvirtualkeyboardplugin.so
%{_qt6_qmldir}/QtQuick/VirtualKeyboard/

%files devel
%{_qt6_headerdir}/QtHunspellInputMethod/
%{_qt6_headerdir}/QtVirtualKeyboard/
%{_qt6_headerdir}/QtVirtualKeyboardSettings/
%{_qt6_headerdir}/QtVirtualKeyboardQml/
%{_qt6_libdir}/libQt6HunspellInputMethod.prl
%{_qt6_libdir}/libQt6HunspellInputMethod.so
%{_qt6_libdir}/libQt6VirtualKeyboard.prl
%{_qt6_libdir}/libQt6VirtualKeyboard.so
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.prl
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.so
%{_qt6_libdir}/libQt6VirtualKeyboardQml.prl
%{_qt6_libdir}/libQt6VirtualKeyboardQml.so
%dir %{_qt6_libdir}/cmake/Qt6HunspellInputMethod/
%dir %{_qt6_libdir}/cmake/Qt6HunspellInputMethodPrivate/
%dir %{_qt6_libdir}/cmake/Qt6VirtualKeyboard/
%dir %{_qt6_libdir}/cmake/Qt6VirtualKeyboardPrivate/
%dir %{_qt6_libdir}/cmake/Qt6VirtualKeyboardQml
%dir %{_qt6_libdir}/cmake/Qt6VirtualKeyboardQmlPrivate
%dir %{_qt6_libdir}/cmake/Qt6VirtualKeyboardSettings/
%dir %{_qt6_libdir}/cmake/Qt6VirtualKeyboardSettingsPrivate
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6Gui/*.cmake
%{_qt6_libdir}/cmake/Qt6HunspellInputMethod/*.cmake
%{_qt6_libdir}/cmake/Qt6HunspellInputMethodPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6VirtualKeyboard/*.cmake
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardQml/*.cmake
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardQmlPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardSettings/*.cmake
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardSettingsPrivate/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_hunspellinputmethod*.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_virtualkeyboard*.pri
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-5
- Drop aarch64 and s390x IPO PCH and %%_smp_mflags %%_lto_cflags OOM workarounds

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-1
- Prepare for Oreon 11 (RP1)
