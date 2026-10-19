%global source0_hash bc60be5904330faaa3ddd2aed7874bee2f29e4387c245d6787552f067eb0523a
Name:       bdftopcf
Version:    1.1.2
Release:        5%{?dist}
Summary:        Font compiler for the X server and font server
License:    MIT-open-group
URL:        https://www.x.org
Source0:        https://www.x.org/archive/individual/util/%{name}-%{version}.tar.xz
Conflicts:  xorg-x11-font-utils < 7.5-51
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
# /oreon:deps
%description
bdftopcf is a font compiler for the X server and font server.  Fonts
in Portable Compiled Format can be read by any architecture, although
the file is structured to allow one particular architecture to read
them directly without reformatting.  This allows fast reading on the
appropriate machine, but the files are still portable (but read more
slowly) on other machines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.2-5
- Prepare for Oreon 11 (RP1)
