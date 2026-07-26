%global source0_hash a0a87952bac79668b30fedd3d80dffd0cb83c605414b60491f04a56fe861fb36

Name:           sidplayfp
Version:        2.15.0
Release:        2%{?dist}
Summary:        SID chip music module player
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/libsidplayfp
Source0:        https://github.com/libsidplayfp/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libsidplayfp-devel >= 2.0
BuildRequires:  alsa-lib-devel pulseaudio-libs-devel libtool
BuildRequires:  gettext-devel

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

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/sidplayfp
%{_bindir}/stilview
%{_mandir}/man?/sidplayfp.*
%{_mandir}/man1/stilview.1*

%changelog
%autochangelog
