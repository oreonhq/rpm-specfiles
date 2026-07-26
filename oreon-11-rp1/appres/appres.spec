%global source0_hash 1114b189239fd87a8d1db433edcb4486346d29912132b91eaeee5667f13b819f

Name:       appres
Version:    1.0.7
Release:    5%{?dist}
Summary:    X11 utility to print application resources

# SPDX confirmed
License:    MIT-open-group
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes: xorg-x11-resutils < 7.7-9

%description
The appres program prints the resources seen by an application (or
sub-hierarchy of an application) with the specified class and instance
names. It can be used to determine which resources a particular
program will load.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
autoreconf -v --install

%build
%configure --disable-silent-rules --disable-xprint
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
