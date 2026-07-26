%global source0_hash f746feba57af316b159f0169de5d78b4fd1064c2c0c8017cb5856b2f22e83f20

Name:           ladspa-caps-plugins
Version:        0.9.24
Release:        24%{?dist}
Summary:        The C* Audio Plugin Suite
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://quitte.de/dsp/caps.html
Source0:        http://quitte.de/dsp/caps_%{version}.tar.bz2
Patch0:         caps-0.9.10-nostrip.patch
Patch1:         caps-0.9.24-gcc6.patch
Patch2:         caps-pow-exp.patch
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa
Obsoletes:      caps <= 0.3.0-2
Provides:       caps = %{version}-%{release}

%description
caps, the C* Audio Plugin Suite, is a collection of refined LADSPA
units including instrument amplifier emulation, stomp-box classics,
versatile 'virtual analog' oscillators, fractal oscillation, reverb,
equalization and others.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n caps-%{version}
%patch -P0 -p1 -z .nostrip
%patch -P1 -p1
%patch -P2 -p1
# use the system version of ladspa.h
rm ladspa.h

%build
make %{?_smp_mflags} OPTS="$RPM_OPT_FLAGS -fPIC" LDFLAGS="$RPM_LD_FLAGS -shared"

%install
%make_install DEST=%{_libdir}/ladspa

%files
%doc CHANGES README*
%license COPYING
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*

%changelog
%autochangelog
