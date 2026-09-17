%global source0_hash 628b4aff272776c81c24908ffcdf38cd651399284381c369a66227a6ae7a53b6

%{!?_iconsbasedir: %global _iconsbasedir %{_datadir}/icons/hicolor}
%{?rhel: %global cmake %cmake3}

Name:           freedv
Version:        1.8.4
Release:        12%{?dist}
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

BuildRequires:  cmake%{?rhel:3} gcc-c++
BuildRequires:  codec2-devel >= 0.8
BuildRequires:  desktop-file-utils 
BuildRequires:  hamlib-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  gsm-devel
BuildRequires:  libao-devel
BuildRequires:  lpcnetfreedv-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  portaudio-devel
%if 0%{?fedora}
BuildRequires:  libappstream-glib
BuildRequires:  speexdsp-devel
%else
BuildRequires:  speex-devel
%endif
BuildRequires:  wxGTK-devel

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

%autosetup -p1 -n freedv-gui-%{version}

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

# Install desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?fedora}
# install appdata file
mkdir -p %{buildroot}%{_datadir}/appdata
install -pm 0644 %{SOURCE100} %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/*.appdata.xml
%endif

# Remove manuals installed by CMake
rm -rf %{buildroot}%{_datadir}/freedv-gui/USER_MANUAL.*

%if 0%{?rhel} && 0%{?rhel} < 8
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%endif

%files
%license COPYING
%doc README.md USER_MANUAL.md
%{_bindir}/%{name}
%{?fedora:%{_datadir}/appdata/*.appdata.xml}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/freedv-gui/wav/
%{_iconsbasedir}/*/apps/%{name}.png

%changelog
%autochangelog
