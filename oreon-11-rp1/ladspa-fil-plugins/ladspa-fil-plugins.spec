%global source0_hash 1c0bf271211965f670a15a7783b4167307db77264ac1624a06e5667964da8ee9

Name:           ladspa-fil-plugins
Version:        0.3.0
Release:        36%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        LADSPA Filter plugins
URL:            http://www.kokkinizita.net/linuxaudio/
# Upstream site is down was
# http://www.kokkinizita.net/linuxaudio/downloads/...
Source:         FIL-plugins-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa
Obsoletes:      fil-plugins <= 0.0.1
Provides:       fil-plugins = %{version}-%{release}

%description
There is one plugin in this first release, a four-band parametric
equaliser. Each section has an active/bypass switch, frequency,
bandwidth and gain controls. There is also a global bypass switch and
gain control.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n FIL-plugins-%{version}
sed -i -e "s|/usr/lib/ladspa|\\$\(DESTDIR\)%{_libdir}/ladspa|g" \
    -e "s|-shared|-shared $RPM_LD_FLAGS|" Makefile
# we want to use the system ladspa.h
%{__rm} ladspa.h

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
