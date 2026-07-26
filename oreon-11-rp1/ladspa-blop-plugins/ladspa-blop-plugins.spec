%global source0_hash 7e87134fac428d2c3a44423119e273d189ef08ee35f4873d7d88d64610af3e0a

Name:           ladspa-blop-plugins
Version:        0.2.8
Release:        44%{?dist}
Summary:        Bandlimited LADSPA Oscillator Plugins
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://blop.sourceforge.net/
Source:         http://downloads.sourceforge.net/blop/blop-%{version}.tar.gz
Patch1:         ladspa-blop-plugins-configure-c99.patch
BuildRequires:  gcc make
BuildRequires:  ladspa-devel
Requires:       ladspa
Obsoletes:      blop <= 0.2.8-1
Provides:       blop = %{version}-%{release}

%description
BLOP comprises a set of LADSPA plugins that generate bandlimited
sawtooth, square, variable pulse and slope-variable triangle waves,
for use in LADSPA hosts, principally for use with one of the many
modular software synthesisers available.

They are wavetable based, and are designed to produce output with
harmonic content as high as possible over a wide pitch range.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n blop-%{version}
chmod -x src/lp4pole_filter.c src/include/lp4pole_filter.h
# Enable optimiziation
sed -i 's|-O0||g' src/Makefile.in

%build
export LDADD="$RPM_LD_FLAGS -lm"
%configure
# note, we must pass CFLAGS as for some reason they do not get propagated
# by configure
%{__make} %{?_smp_mflags} ladspa_plugin_dir="%{_libdir}/ladspa" \
  CFLAGS="$RPM_OPT_FLAGS -ffast-math -D_GNU_SOURCE -DNO_DEBUG -DPIC -fPIC"

%install
%{__mkdir} -p %{buildroot}%{_libdir}/ladspa
%{__mkdir} -p %{buildroot}%{_datadir}/ladspa/rdf
%{__make} DESTDIR="%{buildroot}" \
          ladspa_plugin_dir="%{_libdir}/ladspa" install
%find_lang blop

# install the rdf description
%{__install} -p -m 644 doc/blop.rdf %{buildroot}%{_datadir}/ladspa/rdf

%files -f blop.lang
%doc AUTHORS NEWS README THANKS TODO doc/*.txt
%license COPYING
%{_libdir}/ladspa/*.so
%{_libdir}/ladspa/blop_files
%{_datadir}/ladspa/rdf/*.rdf

%changelog
%autochangelog
