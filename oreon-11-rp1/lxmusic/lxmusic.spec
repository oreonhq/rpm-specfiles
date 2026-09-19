%global source0_hash b96aee4ba4f2eb61df05c6525f35d95848622a35ad15d50d29d9f45724ffa52f

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
%global		gittardate		20250316
%global		gittartime		1429
%define		use_gitcommit_as_rel		0

%global		gitbaredate	20250316
%global		git_rev		346e213e252aeeee3a04b60c9374c62870a2d796
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_git} || (0%{?use_gitbare} && 0%{?use_gitcommit_as_rel})
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif

%global		main_version	0.4.8

Name:			lxmusic
Version:		%{main_version}%{git_ver_rpm}
Release:		3%{?dist}
Summary:		Lightweight XMMS2 client with simple user interface

License:		GPL-2.0-or-later
URL:			http://lxde.org
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		https://github.com/lxde/%{name}/archive/%{main_version}/%{name}-%{version}.tar.gz
%endif
Source100:		create-lxmusic-git-bare-tarball.sh

# As long as there are no plugins, disable the Tools menu
Patch0:		lxmusic-0.3.0-no-tools-menu.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1250738
# https://sourceforge.net/p/lxde/bugs/774/
Patch10:		lxmusic-0.4.6-saver_quit_from_taskber_on_play.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	git
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(xmms2-client)
BuildRequires:	pkgconfig(xmms2-client-glib)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	gettext
BuildRequires:	intltool

BuildRequires:	desktop-file-utils
BuildRequires: /usr/bin/appstream-util
Requires:		xmms2 >= 0.7

%description
LXMusic is a very simple gtk+ XMMS2 client written in pure C. It has very few 
functionality, and can do nothing more than play the music. The UI is very 
clean and simple. This is currently aimed to be used as the default music 
player of LXDE (Lightweight X11 Desktop Environment) project.

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

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

%patch -P0 -p1 -b .no-tools
%patch -P10 -p1 -b .saverquit

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

bash autogen.sh

%configure
%make_build

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<application>
<id type="desktop">lxmusic.desktop</id>
<metadata_license>CC0-1.0</metadata_license>
<name>LXMusic</name>
<summary>A minimalist music player for LXDE</summary>
<description>
<p>LXMusic is a simple GUI XMMS2 client with minimal functionality.</p>
</description>
</application>
EOF

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc	AUTHORS
%doc	README
%license	COPYING

%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/lxmusic.desktop

%dir	%{_datadir}/lxmusic/
%{_datadir}/lxmusic/*.ui.glade
%{_datadir}/icons/hicolor/*/*/lxmusic.png

%changelog
%autochangelog
