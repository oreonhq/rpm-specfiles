%global source0_hash 324e235946757a7a69e2e238f21899f3cf5c6d1ce276c268522c35b7c6c4b19c

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
%global		gittardate		20250329
%global		gittartime		1449
%define		use_gitcommit_as_rel		0

%global		gitbaredate	20250327
%global		git_rev		ca13623c6176585db4759ce4371fbf89c56fa630
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif

%global		main_version	0.3.1

Name:			gpicview
Version:		%{main_version}%{git_ver_rpm}
Release:		3%{?dist}
Summary:		Simple and fast Image Viewer for X

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			https://github.com/lxde/%{name}/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		https://github.com/lxde/%{name}/archive/%{main_version}/%{name}-%{version}.tar.gz
%endif
Source101:		create-gpicview-git-bare-tarball.sh

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	libjpeg-devel
BuildRequires:	desktop-file-utils

BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	git

Requires:		/usr/bin/xdg-mime

%description
Gpicview is an simple and image viewer with a simple and intuitive interface.
It's extremely lightweight and fast with low memory usage. This makes it 
very suitable as default image viewer of desktop system. Although it is 
developed as the primary image viewer of LXDE, the Lightweight X11 Desktop 
Environment, it only requires GTK+ and can be used in any desktop environment.

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

git config user.name "gpicview Fedora maintainer"
git config user.email "gpicview-maintainers@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

bash autogen.sh
%configure \
	--enable-gtk3 \
	--disable-silent-rules \
	%{nil}
%make_build

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install
desktop-file-install \
	--delete-original \
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
	--remove-category=Application \
	--remove-category=Utility \
	--remove-category=Photography \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}

%files -f %{name}.lang
%license	COPYING
%doc	AUTHORS

%{_bindir}/gpicview
%{_datadir}/applications/*gpicview.desktop
%dir	%{_datadir}/gpicview/
%{_datadir}/gpicview/pixmaps/
%{_datadir}/gpicview/ui/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
