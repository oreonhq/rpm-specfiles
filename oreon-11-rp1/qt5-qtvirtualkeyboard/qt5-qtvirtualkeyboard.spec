%global source0_hash 45dbd864033051dc7cabae365f4855d8fede51ef553c5e66cdf87c439390fc6c

%global qt_module qtvirtualkeyboard

Summary: Qt5 - VirtualKeyboard component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

## upstreamable patches

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel >= %{version}
BuildRequires: qt5-qtsvg-devel >= %{version}
BuildRequires: hunspell-devel

# version unknown
Provides: bundled(libpinyin)

%description
The Qt Virtual Keyboard project provides an input framework and reference keyboard frontend
for Qt 5.  Key features include:
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
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{qt_module}-everywhere-src-%{version} -p1

%build
%{qmake_qt5} \
  CONFIG+=lang-all

%make_build

%install
make install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

%ldconfig_scriptlets

%files
%license LICENSE.*
%{_qt5_libdir}/libQt5HunspellInputMethod.so.5*
%{_qt5_libdir}/libQt5VirtualKeyboard.so.5*
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QVirtualKeyboardPlugin.cmake
%{_qt5_plugindir}/platforminputcontexts/libqtvirtualkeyboardplugin.so
%{_qt5_plugindir}/virtualkeyboard/
%{_qt5_qmldir}/QtQuick/VirtualKeyboard/

%files devel
%{_qt5_headerdir}/QtHunspellInputMethod/
%{_qt5_headerdir}/QtVirtualKeyboard/
%{_qt5_libdir}/libQt5HunspellInputMethod.prl
%{_qt5_libdir}/libQt5HunspellInputMethod.so
%{_qt5_libdir}/libQt5VirtualKeyboard.prl
%{_qt5_libdir}/libQt5VirtualKeyboard.so
%{_qt5_libdir}/cmake/Qt5HunspellInputMethod/
%{_qt5_libdir}/cmake/Qt5VirtualKeyboard/
%{_qt5_libdir}/pkgconfig/Qt5VirtualKeyboard.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_hunspellinputmethod*.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_virtualkeyboard*.pri

%files examples
%{_qt5_examplesdir}/

%changelog
%autochangelog
