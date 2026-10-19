%global source0_hash 35261326680e98bfc280623fac1190baa99c719133bf06207216fb7b85ea9a63
Summary:        Audio autotuner for JACK
Name:          zita-at1
Version:       0.8.2
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           http://kokkinizita.linuxaudio.org/
Source0:        http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Source1:       %{name}.desktop
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  clthreads-devel
BuildRequires:  clxclient-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libXft-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  zita-alsa-pcmi-devel
BuildRequires:  zita-resampler-devel
# /oreon:deps
%description
%{name} is an 'autotuner', normally used to correct the pitch of a voice 
singing (slightly) out of tune.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i -e 's|-march=native|%{optflags}|' -e 's|-ffast-math||' \
    source/Makefile

%build

cd source
make PREFIX=%{_prefix} LDFLAGS="$RPM_LD_FLAGS" %{?_smp_mflags}
%install
cd source
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_lib} install
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install  \
   --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 %{_builddir}/%{name}-%{version}/doc/redzita.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
