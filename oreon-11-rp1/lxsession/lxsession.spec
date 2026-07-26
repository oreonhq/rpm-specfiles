%global source0_hash 6b2dc40eadc73049898e71314b3e8243016619a8c182b001d88f4a71362514f1

# review https://bugzilla.redhat.com/show_bug.cgi?id=502404
# renamed from lxsession-lite. Original review at
# https://bugzilla.redhat.com/show_bug.cgi?id=442268

%global		use_release	0
%global		use_gitbare	1

%if 0%{?use_gitbare} < 1
# force
%global		use_release	1
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%if 0%{?use_gitbare}
%global		gittardate		20250403
%global		gittartime		1600
%define		use_gitcommit_as_rel		0

%global		gitbaredate	20250330
%global		git_rev		886b9ad90f98b12c775313331431769295138f69
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}

%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif
%endif

%global		main_version	0.5.6

Name:			lxsession
Version:		%{main_version}%{git_ver_rpm}
Release:		4%{?dist}
Summary:		Lightweight X11 session manager
Summary(de):	Leichtgewichtiger X11 Sitzungsverwalter

# LGPL-3.0-or-later	lxsession-logout/lxsession-logout-dbus-interface.c
# HPND	lxsettings-daemon/xsettings-common.c and some files under lxsettings-daemon/
# GPL-2.0-or-later	Others
# SPDX confirmed
License:		GPL-2.0-or-later AND HPND AND LGPL-3.0-or-later

URL:			http://lxde.sourceforge.net/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
%endif
#http://sourceforge.net/p/lxde/bugs/760/
Patch1000:		lxsession-0.5.2-git9f8d6133-reload.patch
Patch1002:		lxsession-0.5.2-notify-daemon-default.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1801071
# race condition when calling "lxsession -r" from imsettings-lxde and when daemon is not configured yet
# explicitly do nullptr check
Patch1005:		lxsession-0.5.4-load-settings-nullcheck.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1830588
# add custom directory to XDG_CONFIG_DIRS
Patch2001:		lxsession-0.5.5-add-custom-xdg-config-dir.patch
# Split out appindicator support and kill it for now:
# libappindicator 12.10.1 kills GTK2 vapi support
Patch2002:		lxsession-0.5.5-split-indicator-support.patch
# Workaround for explicitly setting ally bus
# ref: https://bugzilla.redhat.com/show_bug.cgi?id=2209584#c6
# ref: https://forums.gentoo.org/viewtopic-t-1172784-start-75-postdays-0-postorder-asc-highlight-.html
Patch2003:		lxsession-0.5.6-lxsession-workaround-for-setting-ally-bus.patch

BuildRequires:	pkgconfig(gtk+-2.0)
#BuildRequires:	pkgconfig(indicator-0.4)
#BuildRequires:	pkgconfig(appindicator-0.1)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	make
BuildRequires:	vala
BuildRequires:	docbook-utils
BuildRequires:	intltool
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-style-xsl
BuildRequires:	/usr/bin/xsltproc

BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	/usr/bin/git

# name changed back from lxsession-lite to lxsession
Obsoletes:		lxsession-lite <= 0.3.6-6
Provides:		lxsession-lite = %{version}-%{release}
# lxde-settings-daemon was merged into lxsession
Obsoletes:		lxde-settings-daemon <= 0.4.1-2
Provides:		lxde-settings-daemon = 0.4.1-3
# required for suspend and hibernate
Requires:		upower

%description
LXSession is a standard-compliant X11 session manager with shutdown/
reboot/suspend support via systemd. In connection with gdm it also supports user 
switching.

LXSession is derived from XSM and is developed as default X11 session manager 
of LXDE, the Lightweight X11 Desktop Environment. Though being part of LXDE, 
it's totally desktop-independent and only has few dependencies.

%description -l de
LXSession Lite ist ein Standard konformer X11 Sitzungsverwalter mit 
Unterstützung für Herunterfahren, Neustart und Schlafmodus mittels systemd. 
Zusammen mit GDM unterstützt auch Benutzerwechsel.

LXSession Lite ist von XSM abgeleitet und wird als Sitzungsverwalter von LXDE,
der leichtgewichtigen X11 Desktop Umgebung, entwickelt. Obwohl er Teil von 
LXDE ist, ist er komplett Desktop unabhängig und hat nur wenige 
Abhängigkeiten.

%package edit
Summary:		Simple GUI to configure what’s automatically started in LXDE

%description edit
LXSession-edit is a tool to manage freedesktop.org compliant desktop session 
autostarts. Currently adding and removing applications from the startup list 
is not yet available, but it will be support in the next release.

%package -n lxpolkit
Summary:		Simple PolicyKit authentication agent
Requires:		polkit >= 0.95
# required to replace polkit-gnome and polkit-kde
Provides:		PolicyKit-authentication-agent

%description -n lxpolkit
LXPolKit is a simple PolicyKit authentication agent developed for LXDE, the 
Lightweight X11 Desktop Environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?use_release}
%setup -q -n %{name}-%{main_version}%{git_builddir}

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -n %{name}-%{main_version}%{git_builddir} -a 0
git clone ./%{name}.git/
cd %{name}

git checkout -b %{main_version}-fedora %{git_rev}
cp -a [A-Z]* ..
cp -a data/ ..

cat > GITHASH <<EOF
EOF

cat GITHASH | while read line
do
  commit=$(echo "$line" | sed -e 's|[ \t].*||')
  git cherry-pick $commit
done

# Restore timestamps
set +x
echo "Restore timestamps"
git ls-tree -r --name-only HEAD | while read f
do
	unixtime=$(git log -n 1 --pretty='%ct' -- $f)
	touch -d "@${unixtime}" $f
done
set -x
%endif

git config user.name "lxpanel Fedora maintainer"
git config user.email "lxpanel-maintainers@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

#%patch0 -p1 -b .dsofix
%patch -P1000 -p1 -b .reload
%patch -P1002 -p1 -b .notify
%patch -P1005 -p1 -b .nullcheck
%patch -P2001 -p1 -b .custom
%patch -P2002 -p1 -b .indicator
%patch -P2003 -p1 -b .ally
%if 0%{?use_gitbare}
git commit -m "Apply Fedora specific configulation" -a
%endif

# Umm?? Why are warnings killed by default?
sed -i.warn Makefile.am \
	-e '\@include.*config\.h@s| -w | |'

%if 0%{?use_gitbare}
git commit -m "Enable warnings" -a
%endif

# Don't start in Xfce to avoid bugs like
# https://bugzilla.redhat.com/show_bug.cgi?id=616730
sed -i 's/^NotShowIn=GNOME;KDE;/NotShowIn=GNOME;KDE;XFCE;/g' data/lxpolkit.desktop.in.in

# fix icon in desktop file
# http://lxde.git.sourceforge.net/git/gitweb.cgi?p=lxde/lxsession-edit;a=commit;h=3789a96691eadac9b8f3bf3034a97645860bd138
sed -i 's/^Icon=xfwm4/Icon=session-properties/g' data/lxsession-edit.desktop.in
%if 0%{?use_gitbare}
git commit -m "Apply Fedora specific configulation 2" -a
%endif

mkdir m4 || :
sh autogen.sh

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

%configure \
	--enable-man \
	--disable-silent-rules \
	--enable-advanced-notifications \
	--enable-debug \
	%{nil}
make clean

# Tweak optflags here
find . -name Makefile | \
	xargs sed -i -e 's|\(-Werror=format-security\)|\1 -Werror=implicit-function-declaration -Werror=return-type |'
%make_build -k

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

rm -rf $RPM_BUILD_ROOT
%make_install
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/xdg/%{name}

desktop-file-install \
    --remove-key="NotShowIn" \
    --add-only-show-in="LXDE;" \
    --delete-original \
    --dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
    %{buildroot}%{_sysconfdir}/xdg/autostart/lxpolkit.desktop

desktop-file-install \
    --remove-key="NotShowIn" \
    --add-only-show-in="LXDE;" \
    --delete-original \
     %{buildroot}%{_datadir}/applications/*.desktop

%if 0%{?use_gitbare}
cd ..
%endif
%find_lang %{name}

%files -f %{name}.lang

%doc AUTHORS
%doc	ChangeLog
%license	COPYING
%doc	README
%doc	data/desktop.conf.example

%{_bindir}/%{name}
%{_bindir}/%{name}-logout
%{_bindir}/%{name}-db
%{_bindir}/%{name}-default
%{_bindir}/%{name}-default-apps
%{_bindir}/%{name}-default-terminal

%dir	%{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}-xsettings

%{_bindir}/lxsettings-daemon
%{_bindir}/%{name}-xdg-autostart
%{_bindir}/lxlock
%{_bindir}/lxclipboard

%dir	%{_datadir}/%{name}/
%{_datadir}/%{name}/images/
%dir	%{_datadir}/%{name}/ui/
%{_datadir}/%{name}/ui/lxsession-default-apps.ui

%{_datadir}/applications/lxsession-default-apps.desktop

# we need to own
%dir %{_sysconfdir}/xdg/%{name}

%{_mandir}/man*/%{name}*.*
%{_mandir}/man1/lxlock.1*
%{_mandir}/man1/lxpolkit.1*
%{_mandir}/man1/lxclipboard.1*
%{_mandir}/man1/lxsettings-daemon.1*

%files edit
%{_bindir}/%{name}-edit
%{_datadir}/applications/lxsession-edit.desktop
%{_datadir}/%{name}/ui/lxsession-edit.ui

%files -n lxpolkit
%{_bindir}/lxpolkit
%{_sysconfdir}/xdg/autostart/lxpolkit.desktop
%{_datadir}/%{name}/ui/lxpolkit.ui

%changelog
%autochangelog
