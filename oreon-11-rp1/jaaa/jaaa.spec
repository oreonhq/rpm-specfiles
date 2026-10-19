%global source0_hash 6cf55a3924694179d83e9d49f557896fcebdc1a7f89477e601caa2277ad7f3b3
Summary:        JACK and ALSA Audio Analyzer
Name:          jaaa
Version:       0.9.2
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           https://kokkinizita.linuxaudio.org/
Source0:        https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Source1:       %{name}.desktop
Source2:       %{name}.png
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  clthreads-devel
BuildRequires:  clxclient-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  zita-alsa-pcmi-devel
# /oreon:deps
%description
%{name} (JACK and ALSA Audio Analyzer, is an audio signal generator and
spectrum analyzer designed to make accurate measurements.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cd source
sed -i -e "s|-march=native|%{optflags}|" Makefile

%build

cd source
make "PREFIX=%{_prefix}" %{?_smp_mflags}
%install
cd source
make "DESTDIR=%{buildroot}" "PREFIX=%{_prefix}" install
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
  %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
