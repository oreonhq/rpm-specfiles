%global source0_hash 2b3ed36fb5ba9eec80fd86f94eabbe866506f4fe1948a9d7480f225c89488eee

Name:           gnubik
Version:        2.4.3
Release:        24%{?dist}
Summary:        3D interactive graphics puzzle

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/gnubik/
Source0:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# There aren't 24x24 logo icons provided
Patch1:         iconfix.patch
# The install-desktop target is broken
Patch2:         installfix.patch
# Allow guile 3.0 to be found
Patch3:		guile-3.0.patch

BuildRequires:	autoconf automake
BuildRequires:  gcc
BuildRequires:  libX11-devel pkgconfig(guile-3.0) libGL-devel libGLU-devel gtk2-devel gtkglext-devel
BuildRequires:  gettext gettext-devel desktop-file-utils texinfo
BuildRequires:  make
Requires:       hicolor-icon-theme

%description
GNUbik is a GNU package.  It is a 3D interactive graphics puzzle. It renders
an image of a magic cube (similar to a rubik cube) and you attempt to solve it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 0
chmod -x src/{quarternion,txfm}.{c,h}
# Remove pregenerated binaries and let them be gerenerated
rm po/*.pot
rm doc/%{name}.info

%build
autoreconf --install
%configure
%make_build

%install
%make_install
%find_lang %{name}

rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 doc/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 icons/logo16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 icons/logo22.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
install -p -m 644 icons/logo32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 icons/logo48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

# Unless some asks for the scheme file I am going to leave it out. 
# It isn't named for the package and I doubt it would be used.
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/gen-dot-desktop.scm

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}
%{_infodir}/%{name}.info.*
%{_mandir}/man*/%{name}*

%changelog
%autochangelog
