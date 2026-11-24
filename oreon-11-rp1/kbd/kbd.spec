# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6e5ca4f8d76ee9e3a8db700b667f13e12aac9933828a64e1aaad93d26be9b479
%global source1_hash 9eda617f2db0302cb2bcbd3ad40037f961a76f0606dc486d096248c89e1685e5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global kbd_datadir %{_exec_prefix}/lib/kbd

Name:           kbd
Version:        2.10.0
Release:        1%{?dist}
Summary:        Tools for configuring the console (keyboard, virtual terminals, etc.)
License:        GPL-2.0-or-later
URL:            http://www.kbd-project.org/

Source0: https://mirrors.edge.kernel.org/pub/linux/utils/kbd/kbd-%{version}.tar.xz
Source1: https://www.linuxfromscratch.org/~ken/console-fonts/other/kbd-latsun-fonts.tar.bz2
Source3:        xml2lst.pl
Source4:        vlock.pamd
Source5:        kbdinfo.1
Source6:        cz-map.patch
Patch0:         kbd-1.15-keycodes-man.patch
Patch1:         kbd-1.15-sparc.patch
Patch2:         kbd-1.15-unicode_start.patch
Patch3:         kbd-1.15.5-sg-decimal-separator.patch
Patch4:         kbd-1.15.5-loadkeys-search-path.patch
Patch5:         kbd-2.0.2-unicode-start-font.patch
Patch6:         kbd-2.4.0-covscan-fixes.patch
Patch7:         kbd-2.0.4-vlock-add-prompt-option.patch
Patch8:         kbd-2.10.0-vlock-foreground-vt.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  pam-devel
BuildRequires:  check-devel
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  console-setup
BuildRequires:  xkeyboard-config
BuildRequires:  libxkbcommon-devel
Requires:       %{name}-misc = %{version}-%{release}
Requires:       %{name}-legacy = %{version}-%{release}
Conflicts:      filesystem < 3
Provides:       vlock = %{version}
Conflicts:      vlock <= 1.3
Obsoletes:      vlock < 1.3-34

%description
The %{name} package contains tools for managing a Linux
system's console's behavior, including the keyboard, the screen
fonts, the virtual terminals and font files.

%package misc
Summary:        Data for kbd package
BuildArch:      noarch
 
%description misc
The %{name}-misc package contains data for kbd package - console fonts,
keymaps etc. Please note that %{name}-misc is not helpful without kbd.

%package legacy
Summary:        Legacy data for kbd package
BuildArch:      noarch
 
%description legacy
The %{name}-legacy package contains original keymaps for kbd package.
Please note that %{name}-legacy is not helpful without kbd.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%setup -q -a 1
cp -fp %{SOURCE3} .
cp -fp %{SOURCE6} .
%autopatch -p1
aclocal
autoconf

pushd data/keymaps/i386
cp qwerty/pt-latin9.map qwerty/pt.map
cp qwerty/sv-latin1.map qwerty/se-latin1.map

mv azerty/fr.map azerty/fr-old.map
cp azerty/fr-latin9.map azerty/fr.map

cp azerty/fr-latin9.map azerty/fr-latin0.map

mv fgGIod/trf.map fgGIod/trf-fgGIod.map
mv olpc/es.map olpc/es-olpc.map
mv olpc/pt.map olpc/pt-olpc.map
mv qwerty/cz.map qwerty/cz-qwerty.map
popd

pushd po
rm -f gr.po gr.gmo
popd

iconv -f iso-8859-1 -t utf-8 < "ChangeLog" > "ChangeLog_"
mv "ChangeLog_" "ChangeLog"

%build
%configure --prefix=%{_prefix} --datadir=%{kbd_datadir} \
  --mandir=%{_mandir} --localedir=%{_datadir}/locale --enable-nls --enable-xkb
%make_build

%install
%make_install

rm -f $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/i386/qwerty/ro_win.map.gz

ln -s sr-cy.map.gz $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/i386/qwerty/sr-latin.map.gz

ln -s us.map.gz $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/i386/qwerty/ko.map.gz

ln -s fa.map.gz $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/i386/qwerty/ara.map.gz

sed -i -e 's,\<kbd_mode\>,%{_bindir}/kbd_mode,g;s,\<setfont\>,%{_bindir}/setfont,g' \
        $RPM_BUILD_ROOT%{_bindir}/unicode_start

gzip -c %SOURCE5 > $RPM_BUILD_ROOT/%{_mandir}/man1/kbdinfo.1.gz

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/vlock

mkdir -p $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/legacy
mv $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/{amiga,atari,i386,include,mac,ppc,sun} $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/legacy

mkdir -p $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb
perl xml2lst.pl < /usr/share/X11/xkb/rules/base.xml > layouts-variants.lst
while read line; do
  XKBLAYOUT=`echo "$line" | cut -d " " -f 1`
  echo "$XKBLAYOUT" >> layouts-list.lst
  [[ $line == *" "* ]] || continue
  XKBVARIANT=`echo "$line" | cut -d " " -f 2`
  ckbcomp -rules base "$XKBLAYOUT" "$XKBVARIANT" | gzip > $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/"$XKBLAYOUT"-"$XKBVARIANT".map.gz
done < layouts-variants.lst

cat layouts-list.lst | sort -u >> layouts-list-uniq.lst
while read line; do
  ckbcomp -rules base "$line" | gzip > $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/"$line".map.gz
done < layouts-list-uniq.lst

zgrep -L "U+0041" $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/* | xargs rm -f
rm -f $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/ge.map.gz

if [ -f "$RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/cz.map.gz" ]; then
  gunzip $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/cz.map.gz
  patch $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/cz.map < %{SOURCE6}
  gzip $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/cz.map
fi

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc ChangeLog AUTHORS README docs/doc/font-formats/*.html docs/doc/dvorak/*
%{_bindir}/*
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/pam.d/vlock

%files misc
%{kbd_datadir}
%exclude %{kbd_datadir}/keymaps/legacy

%files legacy
%{kbd_datadir}/keymaps/legacy

%changelog
%autochangelog
