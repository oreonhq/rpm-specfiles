%global source0_hash 61f668b10b9461cba22d0020d9b37de7002cee9b46192544154367a261ad8916

# Review: https://bugzilla.redhat.com/show_bug.cgi?id=219930

%global	use_release	0
%global	use_gitbare	1

%if 0%{?use_gitbare} < 1
# force
%global	use_release	1
%endif

%global	git_version	%{nil}
%global	git_ver_rpm	%{nil}
%global	git_builddir	%{nil}

%if 0%{?use_gitbare}
%global	gittardate		20260313
%global	gittartime		2237
%global	use_gitcommit_as_rel		1

%global	gitbaredate	20260313
%global	git_rev		4dec3d0d3d8f9e2a9d14dd1b099d378289b67db4
%global	git_short		%(echo %{git_rev} | cut -c-8)
%global	git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_gitcommit_as_rel}
%global	git_ver_rpm	^%{git_version}
%global	git_builddir	-%{git_version}
%endif

%dnl	%global		use_gcc_strict_sanitize	1

%global		main_version	0.11.1
%global		baserelease	1

Name:			lxpanel
Version:		%{main_version}%{git_ver_rpm}
Release:		%{baserelease}%{?dist}%{?use_gcc_strict_sanitize:.san}
Summary:		A lightweight X11 desktop panel

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			http://lxde.org/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{main_version}.tar.xz
%endif
# Shell script to create tarball from git scm
Source100:		create-tarball-from-git.sh
Source101:		create-lxpanel-git-bare-tarball.sh

# Patches reported upstream
Patch52:		0002-SF-894-task-button-correctly-find-the-window-current.patch

## distro specific patches
# default configuration
Patch100:		lxpanel-0.10.2-default.patch
# use nm-connection-editor to edit network connections
# Applied in 0.8.2
#Patch101:		lxpanel-0.8.1-nm-connection-editor.patch
# use zenity instead of xmessage to display low battery warning
Patch102:		lxpanel-0.8.2-battery-plugin-use-zenity.patch
# volumealsa: poll alsa mixer several times at startup (for pipewire)
# https://bugzilla.redhat.com/show_bug.cgi?id=1960829
Patch103:		lxpanel-0.10.1-0003-volumealsa-poll-alsa-mixer-several-times-at-startup.patch

#BuildRequires:	docbook-utils
BuildRequires:	make
BuildRequires:	gettext
BuildRequires:	intltool

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:	pkgconfig(libfm-gtk)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(keybinder)
BuildRequires:	pkgconfig(indicator-0.4)
BuildRequires:	pkgconfig(libmenu-cache) >= 0.3.0
BuildRequires:	pkgconfig(alsa)
BuildRequires:	/usr/bin/curl-config

%if 0%{?use_gitbare}
BuildRequires:	automake
BuildRequires:	libtool
%endif

%if 0%{?use_gcc_strict_sanitize}
BuildRequires:	libasan
BuildRequires:	libubsan
%endif

BuildRequires:	git
BuildRequires:	gcc

# required for the battery plugin with Patch102
Recommends:	zenity

%description
lxpanel is a lightweight X11 desktop panel. It works with any ICCCM / NETWM 
compliant window manager (eg sawfish, metacity, xfwm4, kwin) and features a 
tasklist, pager, launchbar, clock, menu and sytray.

%package        devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

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

cp -a [A-Z]* ..
%endif

git config user.name "lxpanel Fedora maintainer"
git config user.email "lxpanel-maintainer@fedoraproject.org"

%if 0%{?use_release}
git add .
git rm --cached \
	config.guess config.sub configure \
	ltmain.sh \
	%{nil}
git commit -m "base" -q
%endif

cat %PATCH52 | git am
cat %PATCH103 | git am

%patch -P100 -p1 -b .default
#%%patch101 -p1 -b .system-config-network
%patch -P102 -p1 -b .zenity

git commit -m "Apply Fedora specific configulation" -a

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

%if 0%{?use_gitbare}
bash autogen.sh
%endif

%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
%endif

%configure \
	--enable-indicator-support \
	--disable-silent-rules \
	--with-plugins='netstatus,volume,cpu,deskno,batt,kbled,xkb,thermal,cpufreq,monitors,indicator,weather' \
	%{nil}
%make_build

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/lxpanel/*.la

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}

%files -f %{name}.lang
%license	COPYING
%doc	AUTHORS
%doc	README
%config(noreplace)	%{_sysconfdir}/xdg/lxpanel/

%{_bindir}/lxpanel*
%{_datadir}/lxpanel/
%{_libdir}/lxpanel/
%{_mandir}/man1/lxpanel*

%files devel
%{_includedir}/lxpanel/
%{_libdir}/pkgconfig/lxpanel.pc

%changelog
%autochangelog
