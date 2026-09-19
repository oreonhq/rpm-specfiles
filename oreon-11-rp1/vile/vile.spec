%global source0_hash d6239e6b728fa9d0b49f526d8f0998d2db4b7a7dfc317273dbff7aea2a09ea31

Name:		vile
Version:	9.8zb
Release:	8%{?dist}
Summary:	VI Like Emacs
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://invisible-island.net/vile/
Source0:	https://invisible-island.net/archives/vile/current/%{name}-%{version}.tgz
BuildRequires:	make
BuildRequires:	ncurses-devel
BuildRequires:	libxcrypt-devel
BuildRequires:	flex
BuildRequires:	gcc
BuildRequires:	desktop-file-utils
Requires:	%{name}-common = %{version}-%{release}

%package	common
Summary:	The common files needed by any version of the vile editor

%package -n	xvile
Summary:	VI Like Emacs
BuildRequires:	libXpm-devel
BuildRequires:	libXaw-devel
BuildRequires:	libXt-devel
BuildRequires:	perl-generators
Requires:	xorg-x11-fonts-misc
Requires:	%{name}-common = %{version}-%{release}

%description	common
vile is a text editor which is extremely compatible with vi in terms of "finger
feel".  In addition, it has extended capabilities in many areas, notably
multi-file editing and viewing, syntax highlighting, and key rebinding.
vile-common provides the files needed for all versions of vile.

%description -n xvile
xvile is a text editor which is extremely compatible with vi in terms of "finger
feel".  In addition, it has extended capabilities in many areas, notably
multi-file editing and viewing, syntax highlighting, and key rebinding.

%description
vile is a text editor which is extremely compatible with vi in terms of "finger
feel".  In addition, it has extended capabilities in many areas, notably
multi-file editing and viewing, syntax highlighting, and key rebinding.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# loadable filters are mistreated by rpmbuild
#define debug_package #{nil}

%setup -q

%build
%configure --with-loadable-filters \
	   --disable-rpath-hack \
	   --disable-stripping

make %{?_smp_mflags} vile

DESKTOP_FLAGS=--vendor='' \
%configure --with-loadable-filters \
	   --disable-rpath-hack \
	   --disable-stripping \
	   --with-app-defaults=%{_datadir}/X11/app-defaults \
	   --with-screen=Xaw \
	   --with-icon-theme \
	   --with-icondir=%{_datadir}/icons/ \
	   --with-pixmapdir=%{_datadir}/pixmaps/ \
	   --with-xpm

make %{?_smp_mflags} xvile
touch vile

%check
make check

%install
make install DESTDIR=%{buildroot} INSTALL='install -p' TARGET='xvile'
make install DESTDIR=%{buildroot} INSTALL='install -p' TARGET='vile'
make install-desktop DESKTOP_FLAGS=--vendor='' DESKTOP_DIR=%{buildroot}%{_datadir}/applications

rm -v -f %{buildroot}%{_datadir}/applications/lxvile.desktop
rm -v -f %{buildroot}%{_datadir}/applications/uxvile.desktop

pushd %{buildroot}%{_mandir}/man1 
ln -s xvile.1 uxvile.1
ln -s xvile.1 lxvile.1
popd

%files
%{_bindir}/vile
%{_bindir}/vile-pager
%{_bindir}/vile-libdir-path
%{_bindir}/vile-to-html
%{_mandir}/man1/vile*.1.gz

%files common
%doc AUTHORS COPYING CHANGES README doc/*doc
%{_datadir}/vile/
%{_libdir}/vile/

%files -n xvile
%{_bindir}/lxvile
%{_bindir}/lxvile-fonts
%{_bindir}/uxvile
%{_bindir}/xshell.sh
%{_bindir}/xvile
%{_bindir}/xvile-pager
%{_bindir}/xvile-libdir-path
%{_bindir}/xvile-to-html
%{_mandir}/man1/xvile*.1.gz
%{_mandir}/man1/lxvile.1*
%{_mandir}/man1/uxvile.1*
%{_datadir}/pixmaps/vile.xpm
%{_datadir}/icons/hicolor/*/apps/vile.*
%{_datadir}/X11/app-defaults/XVile
%{_datadir}/X11/app-defaults/UXVile
%{_datadir}/applications/xvile.desktop

%changelog
%autochangelog
