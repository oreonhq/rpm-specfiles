%global source0_hash 6b2dc40eadc73049898e71314b3e8243016619a8c182b001d88f4a71362514f1
%global		use_release	0
%global		use_gitbare	1
%if 0%{?use_gitbare} < 1
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
Release:        4%{?dist}
Summary:        Lightweight X11 session manager
Summary(de):	Leichtgewichtiger X11 Sitzungsverwalter
License:		GPL-2.0-or-later AND HPND AND LGPL-3.0-or-later
URL:			http://lxde.sourceforge.net/
%if 0%{?use_gitbare}
Source0:        %{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
%endif
Patch1000:		lxsession-0.5.2-git9f8d6133-reload.patch
Patch1002:		lxsession-0.5.2-notify-daemon-default.patch
Patch1005:		lxsession-0.5.4-load-settings-nullcheck.patch
Patch2001:		lxsession-0.5.5-add-custom-xdg-config-dir.patch
Patch2002:		lxsession-0.5.5-split-indicator-support.patch
Patch2003:		lxsession-0.5.6-lxsession-workaround-for-setting-ally-bus.patch
Obsoletes:		lxsession-lite <= 0.3.6-6
Provides:		lxsession-lite = %{version}-%{release}
Obsoletes:		lxde-settings-daemon <= 0.4.1-2
Provides:		lxde-settings-daemon = 0.4.1-3
Requires:		upower
# oreon:deps
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  vala
# /oreon:deps
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
%oreon_autofiles lxpolkit usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxsession-edit -f %{oreon_filedir}/lxsession-edit.list
%files -n lxpolkit -f %{oreon_filedir}/lxpolkit.list

%changelog

%autochangelog
