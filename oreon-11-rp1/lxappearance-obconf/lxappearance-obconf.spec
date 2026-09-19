%global source0_hash b71d7cc353083f17fd3439907b4674726aa8057707e65a3a556357fcc4783c5a

%global		use_release	0
%global		use_git		0
%global		use_gitbare	1

%if 0%{?use_git} < 1
%if 0%{?use_gitbare} < 1
# force
%global		use_release	1
%endif
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%if 0%{?use_gitbare}
%global		gittardate		20250325
%global		gittartime		1644
%define		use_gitcommit_as_rel		0

%global		gitbaredate	20250324
%global		git_rev		e7060122bb68be31eaade873d279a4f5b2399243
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif

%global		main_version	0.2.4

Name:			lxappearance-obconf
Version:		%{main_version}%{git_ver_rpm}
Release:		3%{?dist}
Summary:		Plugin to configure Openbox inside LXAppearance

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			http://lxde.org/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
%endif
Source1:		create-%{name}-git-bare-tarball.sh

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(obrender-3.5) >= 3.5
BuildRequires:	pkgconfig(obt-3.5) >= 3.5
BuildRequires:	openbox-devel >= 3.5.2
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(lxappearance)
BuildRequires:	libSM-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	/usr/bin/git
Requires:		lxappearance >= 0.5.0
Requires:		openbox >= 3.5.2

%description
This plugin adds an additional tab called "Window Border" to LXAppearance.
It is only visible when the plugin is installed and Openbox is in use.

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
%endif

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

sh autogen.sh

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

%configure \
	--disable-static \
	--disable-silent-rules \
	%{nil}
%make_build

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install
%if 0%{?use_gitbare}
cd ..
%endif

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}

%files -f %{name}.lang
# FIXME add NEWS and TODO if not empty
%license	COPYING
%doc	AUTHORS
%doc	CHANGELOG
%doc	README

%{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf/

%changelog
%autochangelog
