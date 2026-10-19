%global source0_hash c80ff280a02f56c30fadc2dfa210fc6979c4ab968afa315278cb97768b64ecab
Name:       rgb
Version:    1.1.1
Release:        1%{?dist}
Summary:        X color name database
License:    MIT-open-group
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes:  xorg-x11-server-utils < 7.7-40
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
# /oreon:deps
%description
This package includes both the list mapping X color names to RGB values
(rgb.txt) and, if configured to use a database for color lookup, the
rgb program to convert the text file into the binary database format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -v --install
%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
