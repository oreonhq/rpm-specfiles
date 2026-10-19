%global source0_hash 9e4b1bcf5d4ce3b18a1b120acb4d4483d4f635990b18a97b98174fc51fae5678
%{!?_iconsbasedir: %global _iconsbasedir %{_datadir}/icons/hicolor}
%{?rhel: %global cmake %cmake3}
Name:           freedv
Version:        2.4.0
Release:        1%{?dist}
Summary:        FreeDV Digital Voice
License:        GPL-2.0-or-later
URL:            http://freedv.org
Source0:        https://github.com/drowe67/freedv-gui/archive/v%{version}/%{name}-%{version}.tar.gz
Source100:      freedv.appdata.xml
Source101:      freedv48x48.png
Source102:      freedv64x64.png
Source103:      freedv128x128.png
Source104:      freedv256x256.png
ExcludeArch:    i686
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  codec2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gsm-devel
BuildRequires:  hamlib-devel
BuildRequires:  libao-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  lpcnetfreedv-devel
BuildRequires:  portaudio-devel
BuildRequires:  speex-devel
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
FreeDV is a GUI application for Windows and Linux that allows any SSB radio to
be used for low bit rate digital voice.

Speech is compressed down to 1400 bit/s then modulated onto a 1100 Hz wide QPSK
signal which is sent to the Mic input of a SSB radio. On receive, the signal is
received by the SSB radio, then demodulated and decoded by FreeDV.

FreeDV was built by an international team of Radio Amateurs working together on
coding, design, user interface and testing. FreeDV is open source software,
released under the GNU Public License version 2.1. The FDMDV modem and Codec 2
Speech codec used in FreeDV are also open source.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir freedv-gui-%{version}
%oreon_prep
%build

export CFLAGS="%{optflags} -fPIC -pie -Wl,-z,relro -Wl,-z,now"
export CXXFLAGS="%{optflags} -fPIC -pie -Wl,-z,relro -Wl,-z,now"
export LDFLAGS="-Wl,--as-needed"
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DWXCONFIG="%{_bindir}/wx-config-3.2" \
       -DWXRC="%{_bindir}/wxrc-3.2" \
       -DUSE_STATIC_SPEEXDSP=FALSE \
       ../
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -rf %{buildroot}%{_datadir}/freedv-gui/USER_MANUAL.*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
