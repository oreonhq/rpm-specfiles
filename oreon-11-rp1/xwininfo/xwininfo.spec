%global source0_hash bee14d594cc86cc59aae1015c1b452a71bf60c304131e2716ca1cf0df733b4ac
Summary:        X window info utility
Name:       xwininfo
Version:    1.1.7
Release:        1%{?dist}
License:    MIT
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes: xorg-x11-utils < 7.5-39
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
xwininfo prints information about an X11 window.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
