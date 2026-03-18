# {_exec_prefix}/lib/kbd is correct even on x86_64.
# It is traditionally used for kdb data (console fonts, keymaps, ...).
# It is not used for any shared objects/executables.
%global kbd_datadir %{_exec_prefix}/lib/kbd

Name:           kbd
Version:        2.9.0
Release:        2%{?dist}
Summary:        Tools for configuring the console (keyboard, virtual terminals, etc.)
License:        GPL-2.0-or-later
URL:            http://www.kbd-project.org/

Source0:        ftp://ftp.altlinux.org/pub/people/legion/kbd/kbd-%{version}.tar.xz
Source1:        kbd-latsun-fonts.tar.bz2
Source2:        kbd-latarcyrheb-32.tar.bz2
Source3:        xml2lst.pl
Source4:        vlock.pamd
Source5:        kbdinfo.1
Source6:        cz-map.patch
# Patch0: puts additional information into man pages
Patch0:         kbd-1.15-keycodes-man.patch
# Patch1: sparc modifications
Patch1:         kbd-1.15-sparc.patch
# Patch2: adds default unicode font to unicode_start script
Patch2:         kbd-1.15-unicode_start.patch
# Patch3: fixes decimal separator in Swiss German keyboard layout, bz 882529
Patch3:         kbd-1.15.5-sg-decimal-separator.patch
# Patch4: adds xkb and legacy keymaps subdirs to loadkyes search path, bz 1028207
Patch4:         kbd-1.15.5-loadkeys-search-path.patch
# Patch5: don't hardcode font used in unicode_start, take it from vconsole.conf,
#   bz 1101007
Patch5:         kbd-2.0.2-unicode-start-font.patch
# Patch6: fixes issues found by static analysis
Patch6:         kbd-2.4.0-covscan-fixes.patch
# Patch7: adds vlock option to issue prompt before invokation of pam stack
Patch7:         kbd-2.0.4-vlock-add-prompt-option.patch

BuildRequires:  gcc, bison, flex, gettext, pam-devel, check-devel, automake
BuildRequires:  console-setup, xkeyboard-config
BuildRequires: make
Requires:       %{name}-misc = %{version}-%{release}
Requires:       %{name}-legacy = %{version}-%{release}
# Be sure that system is after UsrMove
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
%setup -q -a 1 -a 2
cp -fp %{SOURCE3} .
cp -fp %{SOURCE6} .
%autopatch -p1
aclocal
autoconf

# 7-bit maps are obsolete; so are non-euro maps
pushd data/keymaps/i386
cp qwerty/pt-latin9.map qwerty/pt.map
cp qwerty/sv-latin1.map qwerty/se-latin1.map

mv azerty/fr.map azerty/fr-old.map
cp azerty/fr-latin9.map azerty/fr.map

cp azerty/fr-latin9.map azerty/fr-latin0.map # legacy alias

# Rename conflicting keymaps
mv fgGIod/trf.map fgGIod/trf-fgGIod.map
mv olpc/es.map olpc/es-olpc.map
mv olpc/pt.map olpc/pt-olpc.map
mv qwerty/cz.map qwerty/cz-qwerty.map
popd

# remove obsolete "gr" translation
pushd po
rm -f gr.po gr.gmo
popd

# Convert to utf-8
iconv -f iso-8859-1 -t utf-8 < "ChangeLog" > "ChangeLog_"
mv "ChangeLog_" "ChangeLog"

%build
%configure --prefix=%{_prefix} --datadir=%{kbd_datadir} --mandir=%{_mandir} --localedir=%{_datadir}/locale --enable-nls
%make_build

%install
%make_install

# ro_win.map.gz is useless
rm -f $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/i386/qwerty/ro_win.map.gz

# Create additional name for Serbian latin keyboard
ln -s sr-cy.map.gz $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/i386/qwerty/sr-latin.map.gz

# The rhpl keyboard layout table is indexed by kbd layout names, so we need a
# Korean keyboard
ln -s us.map.gz $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/i386/qwerty/ko.map.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=2015972
# xkb Arabic layout is 'ara', not 'fa', langtable tells us to use 'ara'
ln -s fa.map.gz $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/i386/qwerty/ara.map.gz

# Some microoptimization
sed -i -e 's,\<kbd_mode\>,%{_bindir}/kbd_mode,g;s,\<setfont\>,%{_bindir}/setfont,g' \
        $RPM_BUILD_ROOT%{_bindir}/unicode_start

# install kbdinfo manpage
gzip -c %SOURCE5 > $RPM_BUILD_ROOT/%{_mandir}/man1/kbdinfo.1.gz

# Install PAM configuration for vlock
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/vlock

# Move original keymaps to legacy directory
mkdir -p $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/legacy
mv $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/{amiga,atari,i386,include,mac,ppc,sun} $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/legacy

# Convert X keyboard layouts to console keymaps
mkdir -p $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb
perl xml2lst.pl < /usr/share/X11/xkb/rules/base.xml > layouts-variants.lst
while read line; do
  XKBLAYOUT=`echo "$line" | cut -d " " -f 1`
  echo "$XKBLAYOUT" >> layouts-list.lst
  XKBVARIANT=`echo "$line" | cut -d " " -f 2`
  ckbcomp -rules base "$XKBLAYOUT" "$XKBVARIANT" | gzip > $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/"$XKBLAYOUT"-"$XKBVARIANT".map.gz
done < layouts-variants.lst

# Convert X keyboard layouts (plain, no variant)
cat layouts-list.lst | sort -u >> layouts-list-uniq.lst
while read line; do
  ckbcomp -rules base "$line" | gzip > $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/"$line".map.gz
done < layouts-list-uniq.lst

# wipe converted layouts which cannot input ASCII (#1031848)
zgrep -L "U+0041" $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/* | xargs rm -f
# wipe the xkb-converted georgian layout, it is unusable, see:
# https://bugzilla.redhat.com/show_bug.cgi?id=2336875
# https://src.fedoraproject.org/rpms/kbd/pull-request/2#comment-239318
rm -f $RPM_BUILD_ROOT%{kbd_datadir}/keymaps/xkb/ge.map.gz

# Fix converted cz layout - add compose rules, if exists
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.0-2
- Prepare for Oreon 11 (RP1)
