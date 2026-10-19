%global source0_hash 1f37d1c4783bb9381ff865a98ed98369b03e280b5629f6bb4a1c5f864bf4becc
Summary:        Multichannel audio level meter
Name:          jmeters
Version:       0.4.5
Release:        1%{?dist}
License:       GPL-2.0-only
URL:           http://kokkinizita.linuxaudio.org/linuxaudio/
Source0:        http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cairo-devel
BuildRequires:  clthreads-devel
BuildRequires:  clxclient-devel
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libpng-devel
BuildRequires:  libsndfile-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
