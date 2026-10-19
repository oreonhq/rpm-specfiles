%global source0_hash 61f668b10b9461cba22d0020d9b37de7002cee9b46192544154367a261ad8916
%global	use_release	0
%global	use_gitbare	1
%if 0%{?use_gitbare} < 1
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
Release:        1%{?dist}
Summary:        A lightweight X11 desktop panel
License:		GPL-2.0-or-later
URL:			http://lxde.org/
%if 0%{?use_gitbare}
Source0:        %{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
%endif
Source100:		create-tarball-from-git.sh
Source101:		create-lxpanel-git-bare-tarball.sh
Patch52:		0002-SF-894-task-button-correctly-find-the-window-current.patch
Patch100:		lxpanel-0.10.2-default.patch
Patch102:		lxpanel-0.8.2-battery-plugin-use-zenity.patch
Patch103:		lxpanel-0.10.1-0003-volumealsa-poll-alsa-mixer-several-times-at-startup.patch
%if 0%{?use_gitbare}
%endif
%if 0%{?use_gcc_strict_sanitize}
%endif
Recommends:	zenity
# oreon:deps
BuildRequires:  /usr/bin/curl-config
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(indicator-0.4)
BuildRequires:  pkgconfig(keybinder)
BuildRequires:  pkgconfig(libfm-gtk)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(libwnck-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n lxpanel-devel -f %{oreon_filedir}/lxpanel-devel.list

%changelog

%autochangelog
