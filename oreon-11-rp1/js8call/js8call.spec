%global source0_hash 9c4d65d6699e56d732bec2d250a34be3507b9c915da002707d957bf1920ebb48
%define _lto_cflags %{nil}
%global commit c5236ed22f06
%global project widefido
Name:           js8call
Version:        2.3.1
Release:        1%{?dist}
Summary:        Amateur Radio message passing using FT8 modulation
License:        GPL-3.0-or-later
URL:            http://js8call.com/
Source0:        https://github.com/js8call/js8call/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        com.js8call.JS8Call.metainfo.xml
Patch0:         js8call-hamlib.patch
ExcludeArch:    i686
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  hamlib
BuildRequires:  hamlib-devel
BuildRequires:  libappstream-glib
BuildRequires:  libusbx-devel
BuildRequires:  pkgconfig(hamlib)
BuildRequires:  portaudio-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  systemd-devel
BuildRequires:  tar
# /oreon:deps
%description
JS8Call is software using the JS8 Digital Mode providing weak signal keyboard
to keyboard messaging to Amateur Radio Operators.

JS8Call is an experiment to test the feasibility of a digital mode with the
robustness of FT8, combined with a messaging and network protocol layer for
weak signal communication on HF, using a keyboard messaging style interface. It
is not designed for any specific purpose other than connecting amateur radio
operators who are operating under weak signal conditions. JS8Call is heavily
inspired by WSJT-X, Fldigi, and FSQCall and would not exist without the hard
work and dedication of the many developers in the amateur radio community.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# convert CR + LF to LF
dos2unix *.ui *.rc *.txt

# Don't specify gnu++11 when 14 is the compiler default.

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
%cmake3 -DBoost_NO_SYSTEM_PATHS=FALSE \
        -Dhamlib_STATIC=FALSE
%cmake_build
%install
%cmake_install
install -D -p -m644 icons/Unix/js8call_icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
desktop-file-edit --set-key=Icon --set-value="%{name}" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/
appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/com.js8call.JS8Call.metainfo.xml
desktop-file-edit --set-key=Exec --set-value="js8call --style=fusion" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -f %{buildroot}%{_datadir}/doc/JS8Call/COPYING
rm -f %{buildroot}%{_datadir}/doc/JS8Call/INSTALL*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
