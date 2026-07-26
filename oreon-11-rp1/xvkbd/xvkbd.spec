%global source0_hash 952d07df0fe1e45286520b7c98b4fd00fd60dbf3e3e8ff61e12c259f76a3bef4

Name:           xvkbd
Version:        4.1
Release:        14%{?dist}
Summary:        Virtual Keyboard for X Window System
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://t-sato.in.coocan.jp/xvkbd
Source0:        %{url}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# The following icon is licensed under CC BY-SA 3.0.
Source2:        http://download.sourceforge.jp/xvkbd-fedora/45742/%{name}.png
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  imake
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXtst-devel
BuildRequires:  Xaw3d-devel

%description
xvkbd is a virtual (graphical) keyboard program for X Window System
which provides facility to enter characters onto other clients
(software) by clicking on a keyboard displayed on the screen. This
may be used for systems without a hardware keyboard such as kiosk
terminals or hand-held devices. This program also has facility to send
characters specified as the command line option to another client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's|<X11/Xaw|<X11/Xaw3d|g' xvkbd.c

%build
xmkmf -a
# Installed "normal" files should have 0644 permission, not 0444 permission.
# So I modify Makefile directly.
sed -i.mode -e 's|-m 0444|-m 0644|' Makefile
%make_build CCOPTIONS="%{optflags}" EXTRA_LDOPTIONS="%{?__global_ldflags}"

%install
# By default this installs some file under /usr/lib/X11/app-defaults,
# even on 64 bit architecture. So I had to add "LIBDIR=%{_libdir}/X11".
make LIBDIR=%{_libdir}/X11 DESTDIR=%{buildroot} INSTALLFLAGS="-c -p" \
          install install.man
rm -frv %{buildroot}%{_libdir}/X11/app-defaults
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:1}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -pDm644 %{S:2} %{buildroot}%{_datadir}/pixmaps

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/X11/app-defaults/XVkbd*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/X11/words.english

%changelog
%autochangelog
