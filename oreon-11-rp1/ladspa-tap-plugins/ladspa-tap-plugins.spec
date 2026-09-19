%global source0_hash ea94d8b20d8056e1b9ec6d252846713780fd2a268f3a3a772c362a10950d80cd

Name:           ladspa-tap-plugins
Version:        1.0.0
Release:        1%{?dist}
Summary:        Tom's Audio Processing plugin
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://tomscii.sig7.se/tap-plugins
# Sourceforge project no longer has the tarbals, use Debian's _orig tarbal instead
# Source0:      https://downloads.sourceforge.net/tap-plugins/tap-plugins-%%{version}.tar.gz
Source0:        tap-plugins_%{version}.orig.tar.gz
BuildRequires:  gcc make
BuildRequires:  ladspa-devel
Requires:       ladspa
Obsoletes:      tap-plugins <= 0.7.0-1
Provides:       tap-plugins = %{version}-%{release}

%description
TAP-plugins is short for Tom's Audio Processing plugins. It is a bunch
of LADSPA plugins for digital audio processing, intended for use in a
professional DAW environment such as Ardour.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tap-plugins-%{version}
# use the system version of ladspa.h
%{__rm} ladspa.h
ln -s /usr/include/ladspa.h .

%build
%{__make} %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -ffast-math -c -fPIC -DPIC" \
    LDFLAGS="$RPM_LD_FLAGS -nostartfiles -shared -Wl,-Bsymbolic -lc -lm -lrt"

%install
%{__mkdir} -p %{buildroot}%{_libdir}/ladspa
%{__make} INSTALL_PLUGINS_DIR=%{buildroot}%{_libdir}/ladspa/ \
          INSTALL_LRDF_DIR=%{buildroot}%{_datadir}/ladspa/rdf/ install

%files
%doc CREDITS README
%license COPYING
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*

%changelog
%autochangelog
