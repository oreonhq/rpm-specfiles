# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2164396d5fe80153fd2af9764fcd991883d06fbf1fdfd96efbc99eed21ed1a2f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           wildmidi
Version:        0.5.0
Release:        1%{?dist}
Summary:        Softsynth midi player
License:        GPL-3.0-or-later
URL:            https://github.com/Mindwerks/wildmidi
Source0:        https://github.com/Mindwerks/%{name}/archive/%{name}-%{version}.tar.gz

Patch0:         293.patch

Patch1:         294.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
WildMidi is a software midi player which has a core softsynth library that can
be used with other applications.

%package libs
Summary:        WildMidi Midi Wavetable Synth Lib
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:       timidity++-patches

%description libs
This package contains the WildMidi core softsynth library. The library is
designed to process a midi file and stream out the stereo audio data
through a buffer which an external program can then process further.

%package        devel
Summary:        Development files for %{name}
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
ln -s ../timidity.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.cfg

%ldconfig_scriptlets libs

%files
%license docs/license/GPLv3.txt
%{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/*

%files libs
%license docs/license/LGPLv3.txt
%{_libdir}/libWildMidi.so.2*
%{_mandir}/man5/*

%files devel
%{_includedir}/*
%{_libdir}/cmake/WildMidi
%{_libdir}/libWildMidi.so
%{_libdir}/pkgconfig/wildmidi.pc
%{_mandir}/man3/*

%changelog
%autochangelog
