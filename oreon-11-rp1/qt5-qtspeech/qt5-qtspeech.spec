%global source0_hash 08721b75b2513f74ad9b5b05b928540e4fb37887e6fa30ff4f8ba8132df47ed1
%global qt_module qtspeech
%bcond flite 1
Summary:        Qt5 - Speech component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Patch1:  0001-Reverse-list-of-voices-before-returning-from-Speech-.patch
%if %{with flite}
%endif
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Recommends: %{name}-speechd%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  flite-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  speech-dispatcher-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtspeech-devel -f %{oreon_filedir}/qt5-qtspeech-devel.list
%files -n qt5-qtspeech-examples -f %{oreon_filedir}/qt5-qtspeech-examples.list
%files -n qt5-qtspeech-speechd -f %{oreon_filedir}/qt5-qtspeech-speechd.list
%files -n qt5-qtspeech-flite -f %{oreon_filedir}/qt5-qtspeech-flite.list

%changelog

%autochangelog
