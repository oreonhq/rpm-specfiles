%global font_util 1.4.1

# Must be kept in sync with xorg-x11-fonts!
%global _x11fontdir %{_datadir}/X11/fonts

Summary:    X.Org X11 font utilities
Name:       xorg-x11-font-utils
Epoch:      1
Version:    7.5
Release:    63%{?dist}
License:    MIT AND BSD-2-Clause AND MIT-open-group AND Unicode-3.0
URL:        http://www.x.org

Source0:    http://www.x.org/pub/individual/font/font-util-%{font_util}.tar.xz
# helper script used in post for xorg-x11-fonts
Source5:    xorg-x11-fonts-update-dirs
Source6:    xorg-x11-fonts-update-dirs.1
# oreon url source checksums begin
%global source0_sha256 5c9f64123c194b150fee89049991687386e6ff36ef2af7b80ba53efaf368cc95
%global source0_file font-util-1.4.1.tar.xz
# oreon url source checksums end

BuildRequires:  gcc make libtool
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Provides:   font-util = %{font_util}

Provides:   font-utils = %{epoch}:%{version}-%{release}
Provides:   ucs2any = %{font_util}

Obsoletes:  bdftopcf < 1.1-1
Obsoletes:  fonttosfnt < 1.2.1-1
Obsoletes:  mkfontdir < 1.2.1-1
Obsoletes:  mkfontscale < 1.2.1-1

%description
X.Org X11 font utilities required for font installation, conversion, and
generation.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/font-util-1.4.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5c9f64123c194b150fee89049991687386e6ff36ef2af7b80ba53efaf368cc95" || { echo "oreon: Source0 SHA256 mismatch for font-util-1.4.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n font-util-%{font_util}

%build
%configure --with-fontrootdir=%{_x11fontdir}
%make_build

%install
%make_install

install -m 744 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/xorg-x11-fonts-update-dirs
sed -i "s:@DATADIR@:%{_datadir}:" $RPM_BUILD_ROOT%{_bindir}/xorg-x11-fonts-update-dirs

install -m 744 -p -D %{SOURCE6} $RPM_BUILD_ROOT%{_mandir}/man1/xorg-x11-fonts-update-dirs.1

find $RPM_BUILD_ROOT -name bdftruncate\* -print0 | xargs -0 rm -f

%files
%doc README.md
%license COPYING
%{_bindir}/ucs2any
%{_bindir}/xorg-x11-fonts-update-dirs
%{_datadir}/aclocal/fontutil.m4
%{_libdir}/pkgconfig/fontutil.pc
%{_mandir}/man1/ucs2any.1*
%{_mandir}/man1/xorg-x11-fonts-update-dirs.1*
%dir %{_x11fontdir}
%dir %{_x11fontdir}/util
%{_x11fontdir}/util/map-*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.5-63
- Prepare for Oreon 11 (RP1)
