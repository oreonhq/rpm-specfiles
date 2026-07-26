%global source0_hash df7ceabf8f07044a2fde4924d794554996811640a45de40cb12c2cf1f90f742c

Name:       xclock
Version:    1.1.1
Release:    11%{?dist}
Summary:    The classic X Window System clock utility

License:    MIT-open-group AND SMLNJ AND MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
xclock is the classic X Window System clock utility. It displays
the time in analog or digital form, continuously updated at a
frequency which may be specified by the user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
autoreconf -v --install --force
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/xclock
%{_mandir}/man1/xclock.1*
%{_datadir}/X11/app-defaults/XClock
%{_datadir}/X11/app-defaults/XClock-color

%changelog
%autochangelog
