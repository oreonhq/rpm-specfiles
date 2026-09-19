%global source0_hash 0855467a6426428a3e369389da386d1766b2d20d6ffe147fa7f066c0bbe3b1e6

# Review: https://bugzilla.redhat.com/show_bug.cgi?id=442270

# Review at https://bugzilla.redhat.com/show_bug.cgi?id=540034

%global		use_release  0
%global		use_gitbare  1

%if 0%{?use_gitbare} < 1
# force
%global		use_release  1
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%global		main_version	0.99.3

%if 0%{?use_gitbare}
%global		gittardate		20250322
%global		gittartime		1819
%define		use_gitcommit_as_rel		0

%global		gitbaredate	20250322
%global		git_rev		f38621d0bed738857e651eef6c0b3e3381f9da8b
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}

%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%else
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}
%endif

%endif

Name:			lxde-common
Version:		%{main_version}%{git_ver_rpm}
Release:		6%{?dist}
Summary:		Default configuration files for LXDE

# SPDX confirmed
License:		GPL-2.0-only
URL:			http://lxde.sourceforge.net/
%if 0%{?use_release} >= 1
Source0: 		http://downloads.sourceforge.net/pcmanfm/%{name}-%{mainver}%{?prever}.tar.xz
%endif
%if 0%{?use_gitbare} >= 1
Source0: 		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
Source100: 	create-%{name}-git-bare-tarball.sh
Source1: 		lxde-lock-screen.desktop
Source2:		lxde-desktop-preferences.desktop
# Install custom gtkrc to enable gtk-menu-images by default (bug 1830588)
Source10:       gtkrc.custom
# Set default LXDE terminal as lxterminal (bug 2011471)
Source11:		libfm.conf.custom

# Distro specific patches
Patch10:		%{name}-0.99.2-pcmanfm-config.patch
Patch11:		%{name}-0.99.3-lxpanel-config.patch
Patch12:		%{name}-0.5.5-openbox-menu.patch
Patch13:		%{name}-0.3.2.1-logout-banner.patch
# Use Adwaita Icon Theme
# FIXME: but the below is actually working?? Anyway for now
# we install custon gtkrc (see Source10)
Patch15:        %{name}-0.5.5-vendor.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1638808
# https://sourceforge.net/p/lxde/bugs/868/
Patch16:		%{name}-0.99.2-office-no-sal-variable.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	git
BuildRequires:	desktop-file-utils
# because of some patches:
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	intltool

Requires:		lxmenu-data
Requires:		lxsession >= 0.4.0
Requires:		lxpanel
Requires:		pcmanfm
Requires:		openbox

Requires:		xdg-utils
Requires:		xorg-x11-xinit
# needed because of new gdm
Requires:		/usr/bin/xprop
# Use vendor's artwork
Requires:		system-logos
Requires:		desktop-backgrounds-compat

BuildArch:		noarch

%description
This package contains the configuration files for LXDE, the Lightweight X11 
Desktop Environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?use_release} >= 1
%setup -q -n %{name}-%{main_version}%{?prever}
git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -n %{name}-%{main_version}%{git_builddir} -a 0
git clone ./%{name}.git/
cd %{name}

%if !%{use_gitcommit_as_rel}
git checkout -b fedora-%{version} %{version}
%endif

# Restore timestamps
set +x
echo "Restore timestamps"
git ls-tree -r --name-only HEAD | while read f
do
	unixtime=$(git log -n 1 --pretty='%ct' -- $f)
	touch -d "@${unixtime}" $f
done
set -x

cp -a [A-Z]* ..
%endif

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainer@fedoraproject.org"

%patch -P10 -p1 -b .orig
%patch -P11 -p1 -b .orig2
%patch -P12 -p1 -b .orig3
%patch -P13 -p1 -b .logout-banner
%patch -P15 -p1 -b .vendor
%patch -P16 -p1 -b .office

# Fedora >= 19 doesn't use vendor prefixes for desktop files. Instead of
# maintaining two patches we just strip the prefixes from the files we just
# patched with patch 100.
sed -i 's|id=fedora-|id=|' lxpanel/panel.in

# Fedora 43 changed default background file format
%if 0%{?fedora} >= 42
sed -i.f43 pcmanfm/pcmanfm.conf.in \
	-e '\@wallpaper=@s|default.png|default.jxl|'
%endif

# Change openbox window border theme
# Onyx border style is hard to see...
%if 0%{?fedora} >= 43
sed -i openbox/rc.xml.in \
	-e '\@<theme@{n;s|<name>.*</|<name>Clearlooks</|}'
%endif

# Add ACLOCAL_PATH for gettext 0.25 (ref: bug 2366708)
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
# Calling autotools must be done before executing
# configure if needed
autoreconf -fi

%build
%if 0%{?use_gitbare} >= 1
cd %{name}
%endif

%configure

%install
%if 0%{?use_gitbare} >= 1
cd %{name}
%endif

%make_install

desktop-file-install \
	--remove-key=Encoding \
	--dir=%{buildroot}%{_datadir}/applications \
	lxde-logout.desktop
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications               \
	%{SOURCE1}

desktop-file-install \
	--remove-key=Encoding \
	--dir=%{buildroot}%{_datadir}/applications \
	%{SOURCE2}

#install custom gtkrc
mkdir -p %{buildroot}%{_sysconfdir}/xdg/lxsession/gtk-2.0
install -cpm 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/xdg/lxsession/gtk-2.0/gtkrc

#install custom libfm.conf to set default terminal
mkdir -p %{buildroot}%{_sysconfdir}/xdg/lxsession/libfm
install -cpm 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/xdg/lxsession/libfm/libfm.conf

%files
%doc	AUTHORS
%license	COPYING

%dir	%{_sysconfdir}/xdg/lxsession/LXDE/
%config(noreplace) %{_sysconfdir}/xdg/lxsession/LXDE/autostart
%config(noreplace) %{_sysconfdir}/xdg/lxsession/LXDE/desktop.conf

%dir	%{_sysconfdir}/xdg/lxsession/gtk-2.0
%{_sysconfdir}/xdg/lxsession/gtk-2.0/gtkrc

%dir	%{_sysconfdir}/xdg/lxsession/libfm
%config(noreplace) %{_sysconfdir}/xdg/lxsession/libfm/libfm.conf

%dir	%{_sysconfdir}/xdg/pcmanfm/
%dir	%{_sysconfdir}/xdg/pcmanfm/LXDE/
%config(noreplace) %{_sysconfdir}/xdg/pcmanfm/LXDE/pcmanfm.conf

%{_bindir}/startlxde
%{_bindir}/lxde-logout
%{_bindir}/openbox-lxde

%dir	%{_datadir}/lxde/
%{_datadir}/lxde/images/
%{_datadir}/lxde/wallpapers/

%config(noreplace)	%{_sysconfdir}/xdg/lxpanel/LXDE
%config(noreplace)	%{_sysconfdir}/xdg/openbox/LXDE

%{_mandir}/man1/*.1.gz
%{_datadir}/xsessions/LXDE.desktop
%{_datadir}/applications/lxde-*.desktop

%changelog
%autochangelog
