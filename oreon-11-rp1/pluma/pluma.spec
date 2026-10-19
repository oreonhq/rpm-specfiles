%global source0_hash 27137ff1bb1c53a90d2308b8a6b203e5d07f13a644a0d950f3ead7bb9cf1e241
%global branch 1.28
Summary:        Text editor for the MATE desktop
Name:          pluma
Version:       %{branch}.1
Release:        1%{?dist}
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Patch1:        pluma_0001-configure-Only-use-girepository-2.0-if-libpeas-uses-.patch
Requires: %{name}-data = %{version}-%{release}
Requires: mate-desktop-libs
Requires: caja-schemas
Requires: zenity
Requires: libpeas-loader-python3
# oreon:deps
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)
BuildRequires:  desktop-file-utils
BuildRequires:  enchant-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  iso-codes-devel
BuildRequires:  libSM-devel
BuildRequires:  libpeas1-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
# /oreon:deps
%description
pluma is a small, but powerful text editor designed specifically for
the MATE desktop. It has most standard text editor functions and fully
supports international text in Unicode. Advanced features include syntax
highlighting and automatic indentation of source code, printing and editing
of multiple documents in one window.

pluma is extensible through a plugin system, which currently includes
support for spell checking, comparing files, viewing CVS ChangeLogs, and
adjusting indentation levels.

%package data
Summary:   Data files for pluma
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}
%description data
This package contains shared data needed for pluma.

%package devel
Summary:   Support for developing plugins for the pluma text editor
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  gtksourceview4-devel
%description devel
Development files for pluma

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Patch1
NOCONFIGURE=1 ./autogen.sh

# Fix debug permissions with messy hack 
find ./*/* -type f -exec chmod 644 {} \;
find ./*/*/* -type f -exec chmod 644 {} \;

%build

%configure \
        --disable-static          \
        --enable-gtk-doc-html     \
        --enable-gvfs-metadata    \
        --disable-schemas-compile
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                                \
    --delete-original                               \
    --dir %{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/*.desktop
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pluma-data -f %{oreon_filedir}/pluma-data.list
%files -n pluma-devel -f %{oreon_filedir}/pluma-devel.list

%changelog

%autochangelog
