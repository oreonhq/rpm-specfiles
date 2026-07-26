%global source0_hash 0d3b84d22d2d85e9c3c152e48871e490dfcaad420f8836333f1323c5a690d55f

Name:       xload
Version:    1.2.0
Release:    5%{?dist}
Summary:    Tool to display system load average

License:    X11
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.gz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
# BuildRequires:  pkgconfig(xt) # no longer needed
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
xload displays a periodically updating histogram of the system load average.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/xload
%{_mandir}/man1/xload.1*
%{_datadir}/X11/app-defaults/XLoad

%changelog
%autochangelog
