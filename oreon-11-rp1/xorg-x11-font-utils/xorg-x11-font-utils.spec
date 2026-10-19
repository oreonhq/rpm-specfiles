%global source0_hash 5c9f64123c194b150fee89049991687386e6ff36ef2af7b80ba53efaf368cc95
%global font_util 1.4.1
%global _x11fontdir %{_datadir}/X11/fonts
Summary:        X.Org X11 font utilities
Name:       xorg-x11-font-utils
Epoch:      1
Version:    7.5
Release:        1%{?dist}
License:    MIT AND BSD-2-Clause AND MIT-open-group AND Unicode-3.0
URL:        http://www.x.org
Source0:        https://www.x.org/pub/individual/font/font-util-1.4.1.tar.xz
Source5:    xorg-x11-fonts-update-dirs
Source6:    xorg-x11-fonts-update-dirs.1
Provides:   font-util = %{font_util}
Provides:   font-utils = %{epoch}:%{version}-%{release}
Provides:   ucs2any = %{font_util}
Obsoletes:  bdftopcf < 1.1-1
Obsoletes:  fonttosfnt < 1.2.1-1
Obsoletes:  mkfontdir < 1.2.1-1
Obsoletes:  mkfontscale < 1.2.1-1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros)
# /oreon:deps
%description
X.Org X11 font utilities required for font installation, conversion, and
generation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.5-63
- Prepare for Oreon 11 (RP1)
