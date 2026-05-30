%global source0_hash 2921cdc344f1acee04bcd6ea1e29565c1308263006e134a9ee38cf9c9d6fe75e

Name:       mkfontscale
Version:    1.2.3
Release:    4%{?dist}
Summary:    Tool to generate legacy X11 font system index files

License:    MIT-open-group AND X11 AND MIT AND HPND-sell-variant
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

Patch0:     mkfontscale-examine-all-encodings.patch

BuildRequires:  gcc make libtool
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  zlib-devel

Conflicts:  xorg-x11-font-utils < 7.5-51

# Used to be a separate upstream repo in xorg-x11-font-utils, now it's part
# of mkfontscale. Keep the Provides alive though.
Provides:   mkfontdir = %{version}

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by the
legacy X11 font system.  It now includes the mkfontdir script previously
distributed separately for compatibility with older X11 versions.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/mkfontdir
%{_bindir}/mkfontscale
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/mkfontscale.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.3-4
- Prepare for Oreon 11 (RP1)
