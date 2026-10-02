%global source0_hash a8afd70059479c712948b895e41c35a4a8bfcede3ba2d5a4b855c88bbb725be1

Name:       xhost
Version:    1.0.10
Release:    1%{?dist}
Summary:    Manage hosts or users allowed to connect to the X server

License:    MIT AND ICU
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz


BuildRequires:  automake libtool
BuildRequires:  gcc make gettext
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
xhost is used to manage the list of host names or user names
allowed to make connections to the X server.

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
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
