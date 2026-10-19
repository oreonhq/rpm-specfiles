%global source0_hash cf40c75c7d6f0aad1d4969828fc62025c6222bc6a84f0bb9d6ead7e45970508d
Name:          mate-menus
Version:       1.28.0
Release:        1%{?dist}
Summary:        Displays menus for MATE Desktop
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gobject-introspection-devel
BuildRequires:  make
BuildRequires:  mate-common
# /oreon:deps
%description
Displays menus for MATE Desktop

%package libs
Summary: Shared libraries for mate-menus
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description libs
Shared libraries for mate-menus

%package preferences-category-menu
Summary: Categories for the preferences menu
Requires:    %{name}-libs%{?_isa} = %{version}-%{release}
%description preferences-category-menu
Categories for the preferences menu

%package devel
Summary: Development files for mate-menus
Requires:    %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development files for mate-menus

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# fedora specific
# fix for usage of multimedia-menus, games-menu and wine-menu packages
sed -i -e '/<!-- End Other -->/ a\  <MergeFile>applications-merged/multimedia-categories.menu</MergeFile>' layout/mate-applications.menu
sed -i -e '/<MergeFile>applications-merged\/multimedia-categories.menu<\/MergeFile>/ a\  <MergeFile>applications-merged/games-categories.menu</MergeFile>' layout/mate-applications.menu
sed -i -e '/<MergeFile>applications-merged\/games-categories.menu<\/MergeFile>/ a\  <MergeFile>applications-merged/wine.menu</MergeFile>' layout/mate-applications.menu

#Patch1
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
    --disable-static \
    --enable-introspection=yes \
    --disable-collection
make %{?_smp_mflags} V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mate-menus-libs -f %{oreon_filedir}/mate-menus-libs.list
%files -n mate-menus-preferences-category-menu -f %{oreon_filedir}/mate-menus-preferences-category-menu.list
%files -n mate-menus-devel -f %{oreon_filedir}/mate-menus-devel.list

%changelog

%autochangelog
