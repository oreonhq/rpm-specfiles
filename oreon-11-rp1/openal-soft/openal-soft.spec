# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9e3f95c7de7f349b8fb85746a3f46f5373326c4e27b3d787e9f4337fc1246fc1
%global source1_hash 01f2fe119be529598f530d8a2d5da8c41b1d62ca5602403565784be24527caed
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           openal-soft
Version:        1.24.2
Release:        %{autorelease}
Summary:        Software implementation of the OpenAL 3D audio API

License:        LGPL-2.0-or-later AND BSD-3-Clause AND GPL-2.0-or-later AND Apache-2.0 AND (LGPL-2.0-or-later AND BSD-3-Clause) AND (MIT WITH fmt-exception) AND NCL AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://openal-soft.org/
VCS:            https://github.com/kcat/openal-soft
Source0:        openal-soft-1.24.2-clean.tar.xz
Source:         make_tarball.sh
Patch:          0001-Unbundle-fmt.diff

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(jack)
%if ! 0%{?oreon}
BuildRequires:  pkgconfig(libavcodec)
%endif
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
%if 0%{?fedora}
%endif
%if 0%{?fedora} || 0%{?oreon}
BuildRequires:  pkgconfig(libmysofa)
BuildRequires:  pkgconfig(portaudio-2.0)
%endif
%if 0%{?fedora} || 0%{?rhel} >= 9 || 0%{?oreon}
BuildRequires:  pkgconfig(libpipewire-0.3)
%endif
%if 0%{?fedora} || 0%{?rhel} <= 9
BuildRequires:  pkgconfig(Qt5Widgets)
%endif

%description
OpenAL Soft is an LGPL-licensed, cross-platform, software implementation of the 
OpenAL 3D audio API. It's forked from the open-sourced Windows version available 
originally from openal.org's SVN repository (now defunct). OpenAL provides 
capabilities for playing audio in a virtual 3D environment. Distance 
attenuation, doppler shift, and directional sound emitters are among the 
features handled by the API. More advanced effects, including air absorption, 
occlusion, and environmental reverb, are available through the EFX extension. It 
also facilitates streaming audio, multi-channel buffers, and audio capture.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel 
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        examples
Summary:        Sample applications for OpenAl Soft
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description	examples
Sample applications for OpenAl Soft.

%if 0%{?fedora} || 0%{?rhel} <= 9
%package        qt
Summary:        Qt frontend for configuring OpenAL Soft
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    qt
The %{name}-qt package contains alsoft-config, a Qt-based tool
for configuring OpenAL features.
%endif

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DALSOFT_CPUEXT_NEON:BOOL=OFF \
    -DALSOFT_EXAMPLES:BOOL=ON \
    -DALSOFT_UTILS:BOOL=ON \
    -DALSOFT_INSTALL_CONFIG:BOOL=ON \
    -DALSOFT_INSTALL_EXAMPLES:BOOL=ON \
    -DALSOFT_INSTALL_HRTF_DATA:BOOL=ON \
    -DALSOFT_INSTALL_UTILS:BOOL=ON
%cmake_build

%install
%cmake_install

install -Dpm644 alsoftrc.sample %{buildroot}%{_sysconfdir}/openal/alsoft.conf
sed -i 's/#allow-moves = false/allow-moves = true/' \
  %{buildroot}%{_sysconfdir}/openal/alsoft.conf

%files
%license BSD-3Clause COPYING LICENSE-pffft
%doc README.md ChangeLog
%dir %{_sysconfdir}/openal
%config(noreplace) %{_sysconfdir}/openal/alsoft.conf
%{_bindir}/openal-info
%{_datadir}/openal
%exclude %{_datadir}/openal/alsoftrc.sample
%exclude %{_datadir}/openal/presets/presets.txt
%{_libdir}/libopenal.so.1*

%files devel
%if 0%{?fedora}
%{_bindir}/makemhr
%endif
%{_includedir}/AL
%{_libdir}/cmake/OpenAL
%{_libdir}/libopenal.so
%{_libdir}/pkgconfig/openal.pc

%files examples
%{_bindir}/aldebug
%{_bindir}/aldirect
%{_bindir}/alhrtf
%{_bindir}/allafplay
%{_bindir}/allatency
%{_bindir}/almultireverb
%{_bindir}/alplay
%{_bindir}/alrecord
%{_bindir}/alreverb
%{_bindir}/alstream
%{_bindir}/altonegen

%if 0%{?fedora} || 0%{?rhel} <= 9
%files qt
%{_bindir}/alsoft-config
%endif

%changelog
%autochangelog
