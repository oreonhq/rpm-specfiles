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

# meson.build says:	 GPL-3.0-or-later
# src/eggaccelerators.{c,h}	LGPL-2.1-or-later
# src/keybinder.{c,h}	LGPL-2.1-or-later
# Other source	GPL-3.0-or-later
# SPDX confirmed
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/CristianHenzel/ClipIt
%if 0%{?use_release} >= 1
Source0:        https://github.com/CristianHenzel/ClipIt/archive/v%{version}.tar.gz
%endif
%if 0%{?use_gitbare} >= 1
Source0:        %{reponame}-%{tarballdate}T%{tarballtime}.tar.gz
%endif
Source1:        %{name}.appdata.xml
Source2:        create-clipit-git-bare-tarball.sh
# clipit doesn't autostart in MATE
# Fixed upstream but not yet merged
Patch0:         0001-Autostart-in-MATE.patch
# Force GDK_BACKEND to x11
Patch1:         clipit-1.4.5-force-gdk_backend-x11.patch
# Fix -Werror=incompatible-pointer-types
Patch3:         https://sources.debian.org/data/main/c/clipit/1.4.5%2Bgit20210313-3/debian/patches/incompatible-pointer-types.patch
# https://github.com/CristianHenzel/ClipIt/pull/211
# Fix compilation with C23 struct function prototype
Patch4:         clipit-pr211-c23-function-prototype.patch

%if 0%{?use_gitbare} >= 1
BuildRequires:  git
%endif
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  /usr/bin/appstream-util
Requires:       xdotool

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

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS
%doc ChangeLog
%doc README.md

%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/icons/hicolor/scalable/apps/%{name}-trayicon*.svg
%{_metainfodir}/%{name}.appdata.xml

%{_datadir}/applications/%{name}.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-startup.desktop

%changelog
%autochangelog
