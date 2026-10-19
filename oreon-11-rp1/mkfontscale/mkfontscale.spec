%global source0_hash a01492a17a9b6c0ee3f92ee578850e305315b9f298da5f006a1cd4b51db01a5e
Name:       mkfontscale
Version:    1.2.4
Release:        1%{?dist}
Summary:        Tool to generate legacy X11 font system index files
License:    MIT-open-group AND X11 AND MIT AND HPND-sell-variant
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Patch0:     mkfontscale-examine-all-encodings.patch
Conflicts:  xorg-x11-font-utils < 7.5-51
Provides:   mkfontdir = %{version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  zlib-devel
# /oreon:deps
%description
mkfontscale creates the fonts.scale and fonts.dir index files used by the
legacy X11 font system.  It now includes the mkfontdir script previously
distributed separately for compatibility with older X11 versions.

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

%autochangelog
