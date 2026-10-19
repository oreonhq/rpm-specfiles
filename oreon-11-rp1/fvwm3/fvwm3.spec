%global source0_hash ec35467f01f1a535875284588936de2efa441dac5e9895f6048e1ea7c011b9e8
Name:		fvwm3
Version:	1.1.5
Release:        1%{?dist}
Summary:        Highly configurable multiple virtual desktop window manager
License:	GPL-2.0-or-later AND NTP AND MIT and BSD-2-Clause AND BSD-3-Clause
URL:		https://www.fvwm.org/
Source0:        https://github.com/fvwmorg/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch:		%{name}-0001-Use-mimeopen-instead-of-EDITOR.patch
Patch:		%{name}-0002-build-deps-bump-github.com-sirupsen-logrus-in-bin-Fv.patch
Requires:	xterm
Requires:	%{_bindir}/mimeopen
Requires:	xlockmore
Requires:	python3-pyxdg
# oreon:deps
BuildRequires:  asciidoctor
BuildRequires:  desktop-file-utils
BuildRequires:  fribidi-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  golang
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXt-devel
BuildRequires:  libevent-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  perl-generators
BuildRequires:  readline-devel
BuildRequires:  xorg-x11-xtrans-devel
# /oreon:deps
%description
Fvwm is a window manager for X11. It is designed to minimize memory
consumption, provide a 3D look to window frames, and implement a virtual
desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dmandoc=true
%meson_build
%install
%meson_install
%find_lang %{name}
install -D -m0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/xsessions/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
