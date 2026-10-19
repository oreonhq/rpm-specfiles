%global source0_hash a0662354ce5762e894665a27e59b437cb422bfe738a8cf901665c6ee0d0b9ab8
Name:		fvwm
Version:	2.7.0
Release:        1%{?dist}
Summary:        Highly configurable multiple virtual desktop window manager
License:	GPL-2.0-or-later
URL:		https://www.fvwm.org/
Source0:        https://github.com/fvwmorg/fvwm/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch1:		fvwm-0001-Change-html-viewer-to-xdg-open.patch
Patch2:		fvwm-0002-Use-mimeopen-instead-of-EDITOR.patch
Patch3:		fvwm-0003-FvwmPager-be-more-careful-with-window-labels.patch
Patch4:		fvwm-0004-Skip-install-data-hook-for-default-configs.patch
Patch5:		fvwm-0005-Fix-for-lock-recusion-in-handle_all_expose.patch
Patch6:		fvwm-0006-Fixes-for-C99-compatibility.patch
Patch7:		fvwm-0007-Fixes-for-C99-compatibility.patch
Patch8:		fvwm-0008-Update-FvwmAuto.c.patch
Requires:	xterm
Requires:	%{_bindir}/mimeopen
Requires:	%{_sbindir}/sendmail
Requires:	xdg-utils
Requires:	xlockmore
Requires:	python3-pyxdg
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fribidi-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  readline-devel
# /oreon:deps
%description
Fvwm is a window manager for X11. It is designed to
minimize memory consumption, provide a 3D look to window frames,
and implement a virtual desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

aclocal --force
autoreconf -ivf
%configure --enable-mandoc
%make_build
%install
%make_install
%find_lang %{name}
%find_lang FvwmScript
cat FvwmScript.lang >> %{name}.lang
install -D -m0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/xsessions/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
