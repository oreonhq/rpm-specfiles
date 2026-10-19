%global source0_hash 0855467a6426428a3e369389da386d1766b2d20d6ffe147fa7f066c0bbe3b1e6
%global		use_release  0
%global		use_gitbare  1
%if 0%{?use_gitbare} < 1
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
Release:        1%{?dist}
Summary:        Default configuration files for LXDE
License:		GPL-2.0-only
URL:			http://lxde.sourceforge.net/
%if 0%{?use_release} >= 1
Source0:        %{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_gitbare} >= 1
%endif
Source100: 	create-%{name}-git-bare-tarball.sh
Source1: 		lxde-lock-screen.desktop
Source2:		lxde-desktop-preferences.desktop
Source10:       gtkrc.custom
Source11:		libfm.conf.custom
Patch10:		%{name}-0.99.2-pcmanfm-config.patch
Patch11:		%{name}-0.99.3-lxpanel-config.patch
Patch12:		%{name}-0.5.5-openbox-menu.patch
Patch13:		%{name}-0.3.2.1-logout-banner.patch
Patch15:        %{name}-0.5.5-vendor.patch
Patch16:		%{name}-0.99.2-office-no-sal-variable.patch
Requires:		lxmenu-data
Requires:		lxsession >= 0.4.0
Requires:		lxpanel
Requires:		pcmanfm
Requires:		openbox
Requires:		xdg-utils
Requires:		xorg-x11-xinit
Requires:		/usr/bin/xprop
Requires:		system-logos
Requires:		desktop-backgrounds-compat
BuildArch:		noarch
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  make
# /oreon:deps
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

# Change openbox window border theme
# Onyx border style is hard to see...

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
mkdir -p %{buildroot}%{_sysconfdir}/xdg/lxsession/gtk-2.0
install -cpm 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/xdg/lxsession/gtk-2.0/gtkrc
mkdir -p %{buildroot}%{_sysconfdir}/xdg/lxsession/libfm
install -cpm 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/xdg/lxsession/libfm/libfm.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
