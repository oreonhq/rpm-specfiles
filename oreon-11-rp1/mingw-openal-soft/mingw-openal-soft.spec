%global source0_hash f671087c9043b1e92cd0b125af6f43663249d3c02bc6d580d774a47a91050e0e

%{?mingw_package_header}

%global pkgname openal-soft

# Disable qtgui by default for now
%bcond_with qtgui

Name:           mingw-%{pkgname}
Version:        1.25.0
Release:        2%{?dist}
Summary:        Open Audio Library

# See native spec
License:        LGPL-2.0-or-later AND BSD-3-Clause AND GPL-2.0-or-later AND Apache-2.0 AND (LGPL-2.0-or-later AND BSD-3-Clause) AND MIT AND NCL AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://openal-soft.org/
Source0:        https://openal-soft.org/openal-releases/openal-soft-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  cmake

# Win32 BRs
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-SDL2_mixer
%if %{with qtgui}
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw32-qt5-qmake
%endif

# Win64 BRs
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-SDL2_mixer
%if %{with qtgui}
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qttools
BuildRequires:  mingw64-qt5-qmake
%endif

%description
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. It's built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

# Win32
%package -n mingw32-%{pkgname}
Summary:        MinGW compiled OpenAL Soft library for Win32 target
Provides:       mingw32-openal = %{version}-%{release}

%description -n mingw32-%{pkgname}
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. It's built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

This package provides the library for the Win32 target.

# Win64
%package -n mingw64-%{pkgname}
Summary:        MinGW compiled OpenAL Soft library for Win64 target
Provides:       mingw64-openal = %{version}-%{release}

%description -n mingw64-%{pkgname}
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. It's built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

This package provides the library for the Win64 target.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version} -p1

%build
%mingw_cmake . -DALSOFT_CPUEXT_NEON:BOOL=OFF -DALSOFT_UTILS=OFF -DALSOFT_EXAMPLES=OFF
%mingw_make_build

%install
%mingw_make_install

install -Dpm644 alsoftrc.sample %{buildroot}%{mingw32_sysconfdir}/openal/alsoft.conf
install -Dpm644 alsoftrc.sample %{buildroot}%{mingw64_sysconfdir}/openal/alsoft.conf

%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/OpenAL32.dll
%if %{with qtgui}
%{mingw32_bindir}/alsoft-config.exe
%endif
%{mingw32_sysconfdir}/openal
%{mingw32_includedir}/AL
%{mingw32_libdir}/libOpenAL32.dll.a
%{mingw32_libdir}/cmake/OpenAL/
%{mingw32_libdir}/pkgconfig/openal.pc
%{mingw32_datadir}/openal

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/OpenAL32.dll
%if %{with qtgui}
%{mingw64_bindir}/alsoft-config.exe
%endif
%{mingw64_sysconfdir}/openal
%{mingw64_includedir}/AL
%{mingw64_libdir}/libOpenAL32.dll.a
%{mingw64_libdir}/cmake/OpenAL/
%{mingw64_libdir}/pkgconfig/openal.pc
%{mingw64_datadir}/openal

%changelog
%autochangelog
