%global source0_hash 1dbaac44e7579d5bc8847ca8db4b2e8b9fd3961041f35ee20def4958301e1089
Name:           openal-soft
Version:        1.25.2
Release:        1%{?dist}
Summary:        Software implementation of the OpenAL 3D audio API
License:        LGPL-2.0-or-later AND BSD-3-Clause AND GPL-2.0-or-later AND Apache-2.0 AND (LGPL-2.0-or-later AND BSD-3-Clause) AND (MIT WITH fmt-exception) AND NCL AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://openal-soft.org/
VCS:            https://github.com/kcat/openal-soft
Source0:        https://openal-soft.org/openal-releases/openal-soft-%{version}.tar.bz2
Patch:          0001-Unbundle-fmt.diff
%if 0%{?fedora} || 0%{?oreon} >= 11 || (0%{?rhel} > 0 && 0%{?rhel} >= 9)
%endif
%if (0%{?fedora} || (0%{?rhel} > 0 && 0%{?rhel} <= 9)) && 0%{?oreon} < 11
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
# /oreon:deps
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

%if (0%{?fedora} || (0%{?rhel} > 0 && 0%{?rhel} <= 9)) && 0%{?oreon} < 11
%package        qt
Summary:        Qt frontend for configuring OpenAL Soft
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description    qt
The %{name}-qt package contains alsoft-config, a Qt-based tool
for configuring OpenAL features.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
rm -rf fmt-*/
rm -f utils/*.def

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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openal-soft-devel -f %{oreon_filedir}/openal-soft-devel.list
%files -n openal-soft-examples -f %{oreon_filedir}/openal-soft-examples.list
%files -n openal-soft-qt -f %{oreon_filedir}/openal-soft-qt.list

%changelog

%autochangelog
