%global source0_hash dc54513af9a4681029a1243fd0c9cdf153d813a1125de6c782926674285bc5ae

Name: xmp
Version: 4.2.0
Release: 7%{?dist}
Summary: A multi-format module player
Source0: https://downloads.sourceforge.net/project/xmp/xmp/%{version}/xmp-%{version}.tar.gz
# use pulseaudio output by default
Patch0: xmp-pulse.patch
License: GPL-2.0-or-later
URL: http://xmp.sourceforge.net/
BuildRequires: make
Buildrequires: alsa-lib-devel
BuildRequires:  gcc
BuildRequires: libxmp-devel >= 4.4.0
BuildRequires: pulseaudio-libs-devel

%description
This is the Extended Module Player, a portable module player that plays
over 90 mainstream and obscure module formats, including Protracker MOD,
Fasttracker II XM, Scream Tracker 3 S3M and Impulse Tracker IT files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure \
  --enable-pulseaudio \

%make_build

%install
%make_install

%files
%license COPYING
%doc Changelog CREDITS README girl_from_mars.xm
%dir %{_sysconfdir}/xmp
%config(noreplace) %{_sysconfdir}/xmp/xmp.conf
%config(noreplace) %{_sysconfdir}/xmp/modules.conf
%{_bindir}/xmp
%{_mandir}/man1/xmp.1*

%changelog
%autochangelog
