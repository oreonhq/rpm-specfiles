%global source0_hash b8b2d12588cabfe161ce21a5cd898f06bdfd55c0106ecd4a26c8628aafeff990

Name:           waynergy
Version:        0.0.17
Release:        3%{?dist}
Summary:        Synergy client for Wayland compositors
# Most sources are MIT or ISC, uSynergy header is zlib
# KDE Wayland protocol XML files are LGPL-2.1-or-later
SourceLicense:  MIT and ISC and zlib and LGPL-2.1-or-later
License:        MIT
URL:            https://github.com/r-c-f/waynergy
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libtls)
Requires:       wl-clipboard

%description
An implementation of a Synergy client for wayland compositors. Based
on the upstream uSynergy library (heavily modified for more protocol
support and a bit of paranoia).

%package kde
Summary:        KDE Plasma Desktop integration for Waynergy
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description kde
An implementation of a Synergy client for wayland compositors. Based
on the upstream uSynergy library (heavily modified for more protocol
support and a bit of paranoia).

This package provides a waynergy.desktop file to enable usage of
KDE private protocol functionality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/waynergy
%{_bindir}/waynergy-clip-update
%{_bindir}/waynergy-mapper

%files kde
%{_datadir}/applications/waynergy.desktop

%changelog
%autochangelog
