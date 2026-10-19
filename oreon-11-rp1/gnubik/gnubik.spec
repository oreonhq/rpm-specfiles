%global source0_hash 2b3ed36fb5ba9eec80fd86f94eabbe866506f4fe1948a9d7480f225c89488eee
Name:           gnubik
Version:        2.4.3
Release:        24%{?dist}
Summary:        3D interactive graphics puzzle
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/gnubik/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch1:         iconfix.patch
Patch2:         installfix.patch
Patch3:		guile-3.0.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtkglext-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libX11-devel
BuildRequires:  make
BuildRequires:  pkgconfig(guile-3.0)
BuildRequires:  texinfo
# /oreon:deps
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
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/gen-dot-desktop.scm
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
