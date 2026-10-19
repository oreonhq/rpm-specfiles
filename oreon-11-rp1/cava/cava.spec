%global source0_hash 2866cea11d0bd38406924ab2b47d5577f14909a7321ee928b6836391f375af7e
Name:           cava
Version:        1.0.0
Release:        1%{?dist}
Summary:        Console-based Audio Visualizer for Alsa
License:        MIT
URL:            https://github.com/karlstav/cava
Source0:        https://github.com/karlstav/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  iniparser-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
C.A.V.A. is a bar spectrum analyzer for audio using ALSA for input.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
./autogen.sh

%build

%configure FONT_DIR=/lib/kbd/consolefonts LIBS=-lrt
make %{?_smp_mflags} \
    cava_LDFLAGS=
%install
%make_install
rm -f %{buildroot}%{_libdir}/libiniparser.{a,la,so}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
