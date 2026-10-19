%global source0_hash a1e8d990359ce9c0cce3ceb5116fd0cf72c95528969766898640ca6ca2dba8d4
%global alpha 0
Name:           fldigi
Version:        4.2.13
Release:        1%{?dist}
Summary:        Digital modem program for Linux
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND GPL-2.0-only AND BSL-1.0 AND MIT-0 AND LGPL-3.0-only AND GPL-1.0-only AND Apache-2.0
URL:            https://www.w1hkj.org/
Source0:        https://www.w1hkj.org/files/%{name}/%{name}-%{version}.tar.gz
Source100:      fldigi.appdata.xml
ExcludeArch:    i686
%{?fedora:BuildRequires:  flxmlrpc-devel}
%{?fedora:Recommends:     trustedqsl}
Provides:       flarq = %{version}-%{release}
Obsoletes:      fldigi-doc < 4.1.14-1
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  flxmlrpc-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  hamlib-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libudev-devel
BuildRequires:  make
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
Fldigi is a modem program which supports most of the digital modes used by 
ham radio operators today. You can also use the program for calibrating your 
sound card to WWV or doing a frequency measurement test. The program also comes 
with a CW decoder. fldigi is written with the help of the Fast Light Toolkit X 
GUI. Fldigi is a fast moving project many added features with each update.

Flarq (Fast Light Automatic Repeat Request) is a file transfer application
that is based on the ARQ specification developed by Paul Schmidt, K9PS.
It is capable of transmitting and receiving frames of ARQ data via fldigi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%configure
make %{?_smp_mflags} CFLAGS="%{optflags}" LIBS="-lm -lX11 -lpthread" V=1
%install
%make_install
echo "Keywords=modem;psk;rtty;cw;fsq;fsk;" >> %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/flarq.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
install -pm 0644 data/fldigi-psk.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
