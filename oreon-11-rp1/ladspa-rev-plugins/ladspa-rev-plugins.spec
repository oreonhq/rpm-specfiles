%global source0_hash 9264570561966a6b7cd0b1bf6c50737a2cc75c9862af89192ffab2f0e4804a2d

Name:           ladspa-rev-plugins
Version:        0.3.1
Release:        40%{?dist}
Summary:        A reverberation plugin for LADSPA
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.kokkinizita.net/linuxaudio/
# Upstream site is down was
# http://www.kokkinizita.net/linuxaudio/downloads/...
Source:         REV-plugins-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa
Obsoletes:      rev-plugins <= 0.3.1-1
Provides:       rev-plugins = %{version}-%{release}

%description
This reverb is based on gverb by Juhana Sadeharju, but the code
(now C++) is entirely original. I added a second input for stereo
operation, and some code to prevent FP denormalisation.
This is a preliminary release, and this plugin will probably change
a lot in future versions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n REV-plugins-%{version}
sed -i -e "s|/usr/lib/ladspa|\\\$\(DESTDIR\)%{_libdir}/ladspa|g" \
    -e "s|-shared|-shared $RPM_LD_FLAGS|" Makefile
# we want to use the system ladspa.h
rm ladspa.h

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
