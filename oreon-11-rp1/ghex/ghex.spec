%global source0_hash e2bcf62438edaf04ca961aef8dafd35a2d208aa45f00ee557000b37214c0972e
%global tarball_version %%(echo %{version} | tr '~' '.')
%global __provides_exclude_from ^%{_libdir}/gtkhex-4.0/.*\\.so$
Name:           ghex
Version:        50.4
Release:        1%{?dist}
Summary:        Binary editor for GNOME
License:        GPL-2.0-or-later AND GFDL-1.1-no-invariants-or-later AND CC-BY-SA-4.0
URL:            https://gitlab.gnome.org/GNOME/ghex
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/g-ir-scanner
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
# /oreon:deps
%description
GHex can load raw data from binary files and display them for editing in the
traditional hex editor view. The display is split in two columns, with
hexadecimal values in one column and the ASCII representation in the other.
A useful tool for working with raw data.

%package        libs
Summary:        GtkHex library
%description    libs
The %{name}-libs package contains the shared GtkHex library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.GHex.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.GHex.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n ghex-libs -f %{oreon_filedir}/ghex-libs.list
%files -n ghex-devel -f %{oreon_filedir}/ghex-devel.list

%changelog

%autochangelog
