%global source0_hash 0a26e98719b1ff1e83b9ceeaa76ba6bc7adf3275545798e5c84df4440cf3b1a2
Name:           sidplayfp
Version:        3.2.0
Release:        1%{?dist}
Summary:        SID chip music module player
License:        GPL-2.0-or-later
URL:            https://github.com/libsidplayfp
Source0:        https://github.com/libsidplayfp/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libsidplayfp-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
A player for playing SID music modules originally created on the Commodore 64
and compatibles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Regenerate autofoo stuff, it is better to always build this from source
#the following does't work because rpm can't cope with the exclamation mark:
# rm aclocal.m4 build-aux/!(config.rpath)
rm aclocal.m4 build-aux/*
#so recreate fake config.rpath - see https://lists.gnu.org/archive/html/bug-gettext/2011-10/msg00012.html
touch build-aux/config.rpath
autoreconf -ivf

%build

%configure
make %{?_smp_mflags}
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
