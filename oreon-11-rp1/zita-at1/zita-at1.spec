%global source0_hash 19bb3ddc02b32d6ad15fdd928ee66c2e5bb5e4c7fe465c431e98c2fd83b1ae57

Summary:       Audio autotuner for JACK
Name:          zita-at1
Version:       0.6.2
Release:       17%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# submitted upstream
Source1:       %{name}.desktop

BuildRequires: make
BuildRequires: cairo-devel
BuildRequires: fftw3-devel
BuildRequires: gcc-c++
BuildRequires: zita-resampler-devel
BuildRequires: libpng-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-alsa-pcmi-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel >= 3.9.0
BuildRequires: libXft-devel
BuildRequires: desktop-file-utils

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

# .desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install  \
   --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 %{_builddir}/%{name}-%{version}/doc/redzita.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc AUTHORS doc/*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
