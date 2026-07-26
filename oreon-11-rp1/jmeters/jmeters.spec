%global source0_hash 6879a20acdcaea0f8b3b7d7219562514ce48ab50f5f5da3c530082d71137bcbb

Summary:       Multichannel audio level meter
Name:          jmeters
Version:       0.4.1
Release:       32%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:       GPL-2.0-only
URL:           http://kokkinizita.linuxaudio.org/linuxaudio/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: gcc-c++
#BuildRequires: clalsadrv-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel
BuildRequires: libpng-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: cairo-devel
BuildRequires: make

%description
Jmeters is a Jack multichannel audio level meter app.
It looks very similar to meterbridge since it uses the
same pixmaps.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i -e 's|-O3|%{optflags}|' \
  -e 's|-march=native||' \
  -e 's|-m64||' source/Makefile

%build
cd source
make PREFIX=%{_prefix} LDFLAGS="$RPM_LD_FLAGS -lpthread " CFLAGS="%{optflags}"

%install
cd source
mkdir -p %{buildroot}%{_bindir}
make PREFIX=%{buildroot}%{_prefix} install

%files
%doc README AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
%autochangelog
