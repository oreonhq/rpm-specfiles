%global source0_hash ba342f2515382fa0efc289fa60a848adc157075b6deb26cfcd2cde0a6f90a9f2

Name:          ebumeter
Summary:       Loudness measurement according to EBU-R128
Version:       0.4.2
Release:       18%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://kokkinizita.linuxaudio.org/linuxaudio
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Source1:       %{name}.desktop
Source2:       %{name}.png
# correct FSF address
Patch0:        %{name}-0.4.0-fsf.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libsndfile-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libXft-devel
BuildRequires: libpng-devel
BuildRequires: zita-resampler-devel
BuildRequires: make

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
    
%files
%doc AUTHORS README doc/*pdf
%license COPYING
%{_bindir}/%{name}
%{_bindir}/ebur128
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
