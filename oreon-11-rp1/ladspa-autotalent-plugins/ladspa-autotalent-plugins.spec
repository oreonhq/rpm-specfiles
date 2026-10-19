%global source0_hash 105e98a0d118c0ea78432d055b9afa478a7d541e5e3fe369498104674cc504d8
Name:           ladspa-autotalent-plugins
Version:        0.2
Release:        1%{?dist}
Summary:        A pitch-correcting LADSPA plugin
License:        GPL-2.0-or-later AND BSD-3-Clause
SourceLicense:  %{license} AND LGPL-2.1-or-later
URL:            http://tombaran.info/autotalent.html
Source0:        http://tombaran.info/autotalent-%{version}.tar.gz
ExcludeArch:    %{ix86}
Requires:       ladspa
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ladspa-devel
BuildRequires:  make
# /oreon:deps
%description
Autotalent is a real-time pitch correction plugin. You specify the notes that a
singer is allowed to hit, and Autotalent makes sure that they do. You can also
use Autotalent for more exotic effects, making your voice sound like a
chiptune, adding artificial vibrato, or messing with your formants.  Autotalent
can also be used as a harmonizer that knows how to sing in the scale with you.
Or, you can use Autotalent to change the scale of a melody between major and
minor or to change the musical mode.

A reference card is available at:

http://tombaran.info/autotalent-%{version}_refcard.pdf

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n autotalent-%{version}

# Use the system ladspa.h
rm -v ladspa.h
sed -i 's|ladspa.h||' Makefile

%build

export CFLAGS="-I. ${CFLAGS-} -Wall -ffast-math -c -fPIC -DPIC"
export LDFLAGS="${LDFLAGS-} -nostartfiles -shared -Wl,-Bsymbolic -lm"
%make_build CC="${CC-gcc}" CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}"
%install
%make_install INSTALL_PLUGINS_DIR='%{buildroot}%{_libdir}/ladspa'
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
