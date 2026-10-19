%global source0_hash ad93ba39acd383696ab6a9ebbed1259ecf2d3cf9f49d6b97038c66f80749e99a
%global _x11fontdir %{_datadir}/X11/fonts
%global aurgiturl    https://git.archlinux.org/svntogit/community.git
Name:           cmatrix
Version:        2.0
Release:        14%{?dist}
Summary:        A scrolling 'Matrix'-like screen
License:        GPL-2.0-or-later
URL:            https://github.com/abishekvashok/%{name}
Source0:        https://github.com/abishekvashok/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-tty
Patch0:         cmatrix-x11-font-path.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  console-setup
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  xorg-x11-fonts-misc
# /oreon:deps
%description
Let's see the cool scrolling lines from the famous movie 'The Matrix'.

%package x11-fonts
Summary:            The font of 'Matrix' for X11
Requires(post):     mkfontdir
Requires(postun):   mkfontdir
%description x11-fonts
The font seen in the famous movie 'The Matrix' to be used in X11.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
cp -p %{SOURCE1} .
# install fonts properly
sed -i -r 's: (%{_prefix}): \$(DESTDIR)\1:' Makefile.am

%build

autoreconf -ivf
%configure
%make_build
help2man -N -o %{name}.1 ./%{name}
%install
install -dm0755 %{buildroot}%{_exec_prefix}/lib/kbd/consolefonts
%make_install
install -Dpm0644 mtx.pcf %{buildroot}%{_x11fontdir}/misc/mtx.pcf
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles cmatrix-x11-fonts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post x11-fonts

mkfontdir %{_x11fontdir}/misc
%postun x11-fonts

if [ "$1" = "0" -a -d %{_x11fontdir}/misc ]; then
  mkfontdir %{_x11fontdir}/misc
fi
%files -f %{oreon_filedir}/main.list
%files -n cmatrix-x11-fonts -f %{oreon_filedir}/cmatrix-x11-fonts.list

%changelog

%autochangelog
