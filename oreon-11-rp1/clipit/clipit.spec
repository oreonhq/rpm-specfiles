%global source0_hash 41736bb88250483a6784281f667a643a7f683a2441b724398adf7217dc9754fb
%global         main_ver      1.4.5
%global         reponame      ClipIt
%global         gitdate       20241103
%global         gitcommit     f35db540c9d3c57b13439d66597736e917e8c9a1
%global         shortcommit   %(c=%{gitcommit}; echo ${c:0:7})
%global         tarballdate   20250116
%global         tarballtime   2347
%global         use_release   0
%global         use_gitbare   1
%global         use_gitcommit_as_ver  1
%if 0%{?use_gitbare} < 1
%global         use_release   1
%endif
%if 0%{?use_gitcommit_as_ver} >= 1
%global         rpm_ver       %{main_ver}^%{gitdate}git%{shortcommit}
%global         builddir_ver  %{main_ver}-%{gitdate}git%{shortcommit}
%else
%define         rpmver        %{main_ver}
%global         builddir_ver  %{main_ver}
%endif
Name:           clipit
Version:        %{rpm_ver}
Release:        5%{?dist}
Summary:        A lightweight, fully featured GTK+ clipboard manager
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/CristianHenzel/ClipIt
%if 0%{?use_release} >= 1
Source0:        https://github.com/CristianHenzel/ClipIt/archive/v%{version}.tar.gz
%endif
%if 0%{?use_gitbare} >= 1
%endif
Source1:        %{name}.appdata.xml
Source2:        create-clipit-git-bare-tarball.sh
Patch0:         0001-Autostart-in-MATE.patch
Patch1:         clipit-1.4.5-force-gdk_backend-x11.patch
Patch3:         https://sources.debian.org/data/main/c/clipit/1.4.5%2Bgit20210313-3/debian/patches/incompatible-pointer-types.patch
Patch4:         clipit-pr211-c23-function-prototype.patch
%if 0%{?use_gitbare} >= 1
%endif
Requires:       xdotool
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)
# /oreon:deps
%description
ClipIt is a lightweight, fully featured GTK+ clipboard manager. It was forked
from Parcellite, adding additional features and bug-fixes to the project.
ClipIts main features are:
* Save a history of your last copied items
* Search through the history
* Global hot-keys for most used functions
* Execute actions with clipboard items
* Exclude specific items from history

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?use_release} >= 1
%setup -q -n %{reponame}-%{builddir_ver}
%endif

%if 0%{?use_gitbare} >= 1
%setup -q -c -n %{reponame}-%{builddir_ver} -T -a 0
git clone ./%{reponame}.git

cd %{reponame}
git checkout -b fedora-%{builddir_ver}-head %{gitcommit}
cp -a [A-Z]* ..

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"
%endif

%patch -P0 -p1 -b .mate
%patch -P1 -p1 -b .nowayland
%patch -P3 -p1 -b .c99_cast
%patch -P4 -p1 -b .c23

sed -i data/clipit.desktop.in -e '\@_Comment.*hr@d'
sed -i data/clipit-startup.desktop.in -e '\@_Comment.*hr@d'

%if 0%{?use_gitbare} >= 1
git commit -m "Apply Fedora specific configuration" -a
%endif

./autogen.sh

%build

%if 0%{?use_gitbare} >= 1
cd %{reponame}
%endif
%configure \
	--with-gtk3 \
	%{nil}
%make_build
%install
%if 0%{?use_gitbare} >= 1
cd %{reponame}
%endif
%make_install
%if 0%{?use_gitbare} >= 1
cd ..
%endif
%find_lang %{name}
desktop-file-install --delete-original \
    --remove-category=Application \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --delete-original \
    --dir %{buildroot}%{_sysconfdir}/xdg/autostart \
    %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
mkdir -p %{buildroot}%{_metainfodir}
install -c -p -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
