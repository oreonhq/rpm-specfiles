%global source0_hash ba342f2515382fa0efc289fa60a848adc157075b6deb26cfcd2cde0a6f90a9f2
Name:          ebumeter
Summary:        Loudness measurement according to EBU-R128
Version:       0.5.1
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           http://kokkinizita.linuxaudio.org/linuxaudio
Source0:        http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Source1:       %{name}.desktop
Source2:       %{name}.png
Patch0:        %{name}-0.4.0-fsf.patch
# oreon:deps
BuildRequires:  clthreads-devel
BuildRequires:  clxclient-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libXft-devel
BuildRequires:  libpng-devel
BuildRequires:  libsndfile-devel
BuildRequires:  make
BuildRequires:  zita-resampler-devel
# /oreon:deps
%description
Loudness measurement according to EBU-R128. Presented at LAC 2011 
(thanks to Joern Nettingsmeier!). The only documentation available 
at the moment are the paper, the presentation, slides and the video 
of the LAC 2011 session.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
pushd source
sed -i -e "s|-march=native|%{optflags}|" Makefile

%build

pushd source
make PREFIX=%{_prefix} LDFLAGS="$RPM_LD_FLAGS" %{?_smp_mflags}
popd
%install
pushd source
make DESTDIR=%{buildroot} PREFIX=%{_prefix} %{?_smp_mflags} install
popd
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
  %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -pm 644 %{SOURCE2} \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
