%global source0_hash 61e1c5e008ac9973aca7cdddf36e9df7410e77083b030eb04f4dc737c51807d7

Summary:    X Event utility
Name:       xev
Version:    1.2.6
Release:    12%{?dist}
License:    MIT
URL:        https://www.x.org

Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr) >= 1.2

Obsoletes: xorg-x11-utils < 7.5-39

%description
xev displays the X11 protocol events sent to a given window.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%{_bindir}/xev
%{_mandir}/man1/xev.1*

%changelog
%autochangelog
