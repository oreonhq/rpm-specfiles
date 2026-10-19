%global source0_hash d246c57ba380b4fa680b783997ff189c51b9f4dd12edf4b719a1f2d84a2e1d2e
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%define _iconstheme    hicolor
%define _iconsbasedir  %{_datadir}/icons/%{_iconstheme}
%define _iconsscaldir  %{_iconsbasedir}/scalable/apps
Name:		byobu
Version:	7.19
Release:        1%{?dist}
Summary:        Light-weight, configurable window manager built upon GNU screen
License:	GPL-3.0-only
URL:		https://github.com/dustinkirkland/byobu
Source0:        https://github.com/dustinkirkland/byobu/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	fedoracommon
Patch:		0002-byobu-use-dnf.patch
Patch:		0002-byobu-use-dnf5.patch
Patch:		0001-byobu-autostart-with-fish-shell.patch
BuildArch:	noarch
Requires:	gettext-runtime
Requires:	newt
Requires:	python3-newt
Requires:	screen
Requires:	tmux
# oreon:deps
BuildRequires:  /usr/bin/msgfmt
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%Description

Byobu is a Japanese term for decorative, multi-panel screens that serve 
as folding room dividers. As an open source project, Byobu is an 
elegant enhancement of the otherwise functional, plain, 
practical GNU Screen. Byobu includes an enhanced profile 
and configuration utilities for the GNU screen window manager, 
such as toggle-able system status notifications.
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N
%autopatch -p0 0

# remove swap file
if [ -e "usr/bin/.byobu-status-print.swp" ]; then rm usr/bin/.byobu-status-print.swp
fi

# fix path for lib directory in scripts
for i in `find . -type f -exec grep -l {BYOBU_PREFIX}/lib/ {} \;`; do
sed -i "s#{BYOBU_PREFIX}/lib/#{BYOBU_PREFIX}/libexec/#g" $i;
done

# fix path for lib directory #2
for i in `find . -type f -exec grep -l BYOBU_PREFIX/lib {} \;`; do
sed -i "s#BYOBU_PREFIX/lib/#BYOBU_PREFIX/libexec/#g" $i;
done

# fix path for correct directory in /usr/share
sed -i "s#DOC = BYOBU_PREFIX + '/share/doc/' + PKG#DOC='%{_pkgdocdir}'#g" usr/lib/byobu/include/config.py.in

# set default fedora windows
cp -p %{SOURCE1} usr/share/byobu/windows/common

# fix path from lib to libexec by modified Makefile.am and in
sed -i "s#/lib/#/libexec/#g" usr/lib/byobu/Makefile.am
sed -i "s#/lib/#/libexec/#g" usr/lib/byobu/include/Makefile.am

%build

export BYOBU_PYTHON=%{__python3}
sh ./autogen.sh
%configure
%make_build
%install
%make_install
rm -rf %{buildroot}%{_sysconfdir}/profile.d
rm %{buildroot}/%{_libexecdir}/%{name}/apport
sed -i 's#status\[\"apport\"\]=0##g' %{buildroot}%{_bindir}/byobu-config
cp -p COPYING %{buildroot}%{_pkgdocdir}
for po in po/*.po
do
    lang=${po#po/}
    lang=${lang%.po}
    mkdir -p %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/
    msgfmt ${po} -o %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/%{name}.mo
done
cp -a usr/share/%{name}/desktop/%{name}.desktop.old usr/share/%{name}/desktop/%{name}.desktop
desktop-file-install usr/share/%{name}/desktop/%{name}.desktop --dir %{buildroot}%{_datadir}/applications
rm %{buildroot}/usr/bin/vigpg
rm %{buildroot}/usr/share/man/man1/vigpg.1
mkdir -p %{buildroot}%{_iconsscaldir}
cp -p usr/share/byobu/pixmaps/byobu.svg %{buildroot}%{_iconsscaldir}
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
