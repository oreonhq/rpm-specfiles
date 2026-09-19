%global source0_hash f44a60b782948662537c0cb14befa6678d6dce790c64dc2c9058eab849a58b74

Name:           ladspa-amb-plugins
Version:        0.8.1
Release:        19%{?dist}
Summary:        Ambisonics LADSPA plugins
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.kokkinizita.net/linuxaudio/
# Upstream site is down was
# http://www.kokkinizita.net/linuxaudio/downloads/AMB-plugins-%%{version}.tar.bz2
Source:         AMB-plugins-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa
Obsoletes:      amb-plugins <= 0.0.2
Provides:       amb-plugins = %{version}-%{release}

%description
A set of first order Ambisonics plugins to use with Ardour. Included
are: mono and stereo input panner, horizontal rotation, and square and
hexagon horizontal decoders. See the README for more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n AMB-plugins-%{version}
sed -i -e "s|/usr/lib/ladspa|\\$\(DESTDIR\)%{_libdir}/ladspa|g" \
    -e "s|-shared|-shared $RPM_LD_FLAGS|g" Makefile

# use the system version of ladspa.h
%{__rm} ladspa.h

%build
%make_build CPPFLAGS="-I. -fPIC -D_REENTRANT $RPM_OPT_FLAGS"

%install
%{__mkdir} -p %{buildroot}%{_libdir}/ladspa
%make_install

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/ladspa/*.so

%changelog
%autochangelog
