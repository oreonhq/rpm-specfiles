%global source0_hash e08f894ac0f9d78ddc520f701e20ecb319dec5a7f8d444d77edd51d96e16a85d

# For test builds, should be set to 0 for release builds.
%global alpha 0

Name:           fldigi
Version:        4.2.10
Release:        3%{?dist}
Summary:        Digital modem program for Linux

License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND GPL-2.0-only AND BSL-1.0 AND MIT-0 AND LGPL-3.0-only AND GPL-1.0-only AND Apache-2.0

URL:            https://www.w1hkj.org/
%if %{alpha}
Source0:        https://www.w1hkj.org/alpha/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        https://www.w1hkj.org/files/%{name}/%{name}-%{version}.tar.gz
%endif
Source100:      fldigi.appdata.xml

ExcludeArch:    i686

#BuildRequires:  automake autoconf libtool

BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel >= 1.3
BuildRequires:  gettext
BuildRequires:  gcc gcc-c++
BuildRequires:  hamlib-devel
%{?fedora:BuildRequires:  flxmlrpc-devel}
%if 0%{?rhel} < 8
BuildRequires:  fltk-static libXcursor-devel
%endif
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libudev-devel
BuildRequires:  make
BuildRequires:  portaudio-devel >= 19-4
BuildRequires:  pulseaudio-libs-devel
%if 0%{?fedora}
# For appstream-util
BuildRequires:  libappstream-glib
%endif

%{?fedora:Recommends:     trustedqsl}

Provides:       flarq = %{version}-%{release}

Obsoletes:      fldigi-doc < 4.1.14-1

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

%autosetup -p1 -n %{name}-%{version}

%build
%if 0%{?rhel} && 0%{?rhel} < 8
%configure --enable-static
%else
%configure
%endif
make %{?_smp_mflags} CFLAGS="%{optflags}" LIBS="-lm -lX11 -lpthread" V=1

%install
%make_install

# Add keywords to desktop file for gnome-shell and software center.
echo "Keywords=modem;psk;rtty;cw;fsq;fsk;" >> %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/flarq.desktop

# Add fldigi-psk.png as it's in PNG format and higher resolution than the XPM.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
install -pm 0644 data/fldigi-psk.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%find_lang %{name}

%if 0%{?fedora}
# Install and validate appdata file
mkdir -p %{buildroot}%{_datadir}/appdata
install %{SOURCE100} -pm 0644 %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%{_bindir}/*
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm 
%{_datadir}/pixmaps/flarq.xpm 
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/flarq.1.gz
%{?fedora:%{_datadir}/appdata/fldigi.appdata.xml}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/flarq.desktop
%{_datadir}/%{name}/

%changelog
%autochangelog
