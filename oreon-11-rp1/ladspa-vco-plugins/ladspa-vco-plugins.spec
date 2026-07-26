%global source0_hash f4e93c22535fa9309577a322b1a7dbbd257ac6592bf90238ff271fb0c66bf8f7

Name:           ladspa-vco-plugins
Version:        0.3.0
Release:        42%{?dist}
Summary:        Anti-aliased pulse and sawtooth oscillators
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.kokkinizita.net/linuxaudio/
# Upstream site is down was
# http://www.kokkinizita.net/linuxaudio/downloads/...
Source0:        VCO-plugins-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa
Obsoletes:      vco-plugins <= 0.3.0-3
Provides:       vco-plugins = %{version}-%{release}

%description
Pulse-VCO : Anti-aliased dirac pulse oscillator (flat amplitude spectrum)
Saw-VCO   : Anti-aliased sawtooth oscillator (1/F amplitude spectrum)
 
Both oscillators are based on the same principle of using a
precomputed interpolated dirac pulse. For the sawtooth version, the
'edge' is made by integrating the anti-aliased pulse. Aliases should
be below -80dB for fundamental frequencies below Fsamp / 6 (i.e. up to
8 kHz at Fsamp = 48 kHz). This frequency range includes the
fundamental frequencies all known musical instruments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n VCO-plugins-%{version}
sed -i -e "s|/usr/lib/ladspa|\\\$\(DESTDIR\)%{_libdir}/ladspa|g" \
    -e "s|-shared|-shared $RPM_LD_FLAGS|" Makefile

%build
%make_build CPPFLAGS="$RPM_OPT_FLAGS -fPIC -D_REENTRANT"

%install
%{__mkdir} -p %{buildroot}%{_libdir}/ladspa
%make_install

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/ladspa/*.so

%changelog
%autochangelog
