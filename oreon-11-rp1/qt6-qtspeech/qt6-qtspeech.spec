%global source0_hash 9a60ce5bee54a9343740feab2582bffb996812f43d6c5585aade26dbd04933db
%global qt_module qtspeech
%if 0%{?unstable}
%global prerelease rc
%endif
%global examples 1
%bcond flite 0%{?fedora}
Summary:        Qt6 - Speech component
Name:    qt6-%{qt_module}
Version: 6.12.0
Release:        1%{?dist}
License: (GPL-2.0-only OR LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-3-Clause
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
Source0:        https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%else
%endif
%if %{with flite}
%endif
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
%if %{with flite}
Recommends:    (%{name}-flite%{?_isa} = %{version}-%{release} if flite)
%endif
Recommends:    (%{name}-speechd%{?_isa} = %{version}-%{release} if speech-dispatcher)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  flite-devel
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  speech-dispatcher-devel
# /oreon:deps
%description
The module enables a Qt application to support accessibility features
such as text-to-speech, which is useful for end-users who are visually
challenged or cannot access the application for whatever reason. The
most common use case where text-to-speech comes in handy is when the
end-user is driving and cannot attend the incoming messages on the phone.
In such a scenario, the messaging application can read out the incoming
message. Qt Serial Port provides the basic functionality, which includes
configuring, I/O operations, getting and setting the control signals of
the RS-232 pinouts.

%if %{with flite}
%package flite
Summary: Festival Lite text-to-speech engine for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description flite
%{summary}.
%endif

%package speechd
Summary: Speech Dispatcher text-to-speech engine for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description speechd
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%if %{with flite}
Requires: qt6-qtspeech-flite
%endif
Requires: qt6-qtspeech-speechd
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
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt6-qtspeech-flite -f %{oreon_filedir}/qt6-qtspeech-flite.list
%files -n qt6-qtspeech-speechd -f %{oreon_filedir}/qt6-qtspeech-speechd.list
%files -n qt6-qtspeech-devel -f %{oreon_filedir}/qt6-qtspeech-devel.list
%files -n qt6-qtspeech-examples -f %{oreon_filedir}/qt6-qtspeech-examples.list

%changelog

%autochangelog
