%global source0_hash 807f909eace684b866fc63b3e962729c120822a6c96e051ff51cf350b3ffb6cd

Summary:    X font list utility
Name:       xlsfonts
Version:    1.0.8
Release:    %autorelease
License:    MIT
URL:        http://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(x11)
Obsoletes: xorg-x11-utils < 7.5-39

%description
xlsfonts lists the fonts available on an X server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%{_bindir}/xlsfonts
%{_mandir}/man1/xlsfonts.1*

%changelog
%autochangelog
