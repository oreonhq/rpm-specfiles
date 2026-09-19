%global source0_hash 08721b75b2513f74ad9b5b05b928540e4fb37887e6fa30ff4f8ba8132df47ed1

%global qt_module qtspeech

%if 0%{?rhel} && 0%{?rhel} >= 10
%bcond flite 0
%else
%bcond flite 1
%endif

Summary: Qt5 - Speech component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

## upstream patches
## repo: https://invent.kde.org/qt/qt/qtspeech
## branch: kde/5.15
## git format-patch v5.15.16-lts-lgpl
Patch1:  0001-Reverse-list-of-voices-before-returning-from-Speech-.patch

## downstream patches
# workaround https://bugzilla.redhat.com/show_bug.cgi?id=1538715
#Patch100: qtspeech-speech-dispatcher_includes.patch

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtmultimedia-devel >= %{version}
BuildRequires: speech-dispatcher-devel >= 0.8
BuildRequires: alsa-lib-devel
%if %{with flite}
BuildRequires: flite-devel
%endif

BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

Recommends: %{name}-speechd%{?_isa} = %{version}-%{release}

%description
The module enables a Qt application to support accessibility features such as text-to-speech, which is useful for end-users who are
visually challenged or cannot access the application for whatever reason. The most common use case where text-to-speech comes in handy
is when the end-user is driving and cannot attend the incoming messages on the phone. In such a scenario, the messaging application
can read out the incoming message. Qt Serial Port provides the basic functionality, which includes configuring, I/O operations,
getting and setting the control signals of the RS-232 pinouts.

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

%package speechd
Summary: %{name} speech-dispatcher plugin
Requires: %{name}%{?_isa} = %{version}-%{release}
%description speechd
%{summary}.

%if %{with flite}
%package flite
Summary: %{name} flite plugin
Requires: %{name}%{?_isa} = %{version}-%{release}
%description flite
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{qt_module}-everywhere-src-%{version}

#patch100 -p1 -b .includes

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} .. \
  %{?_qt5_examplesdir:CONFIG+=qt_example_installs}

%make_build

%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

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
%{_qt5_libdir}/libQt5TextToSpeech.so.5*
%dir %{_qt5_plugindir}/texttospeech/
%dir %{_qt5_libdir}/cmake/Qt5TextToSpeech/

%files speechd
%{_qt5_plugindir}/texttospeech/libqtexttospeech_speechd.so
%{_qt5_libdir}/cmake/Qt5TextToSpeech/Qt5TextToSpeech_QTextToSpeechPluginSpeechd.cmake

%if %{with flite}
%files flite
%{_qt5_plugindir}/texttospeech/libqttexttospeech_flite.so
%{_qt5_libdir}/cmake/Qt5TextToSpeech/Qt5TextToSpeech_QTextToSpeechEngineFlite.cmake
%endif

%files devel
%{_qt5_headerdir}/QtTextToSpeech/
%{_qt5_libdir}/libQt5TextToSpeech.so
%{_qt5_libdir}/libQt5TextToSpeech.prl
%{_qt5_libdir}/cmake/Qt5TextToSpeech/Qt5TextToSpeechConfig*.cmake
%{_qt5_libdir}/pkgconfig/Qt5TextToSpeech.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_texttospeech*.pri

%files examples
%license LICENSE.FDL
%{_qt5_examplesdir}/

%changelog
%autochangelog
