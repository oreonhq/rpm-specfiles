%global source0_hash 60d517c1acabe54ae337f64451264fc76730696eaae26b5480fb37166689b5f3
Name:		totem-pl-parser
Version:	3.26.7
Release:        1%{?dist}
Summary:        Totem Playlist Parser library
License:	LicenseRef-Callaway-LGPLv2+
Url:		https://wiki.gnome.org/Apps/Videos
Source0:        https://download.gnome.org/sources/%{name}/3.26/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libarchive-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  uchardet-devel
# /oreon:deps
%description
A library to parse and save playlists, as used in music and movie players.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Denable-gtk-doc=true \
	-Denable-libarchive=yes \
	-Denable-libgcrypt=yes \
	-Dintrospection=true
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n totem-pl-parser-devel -f %{oreon_filedir}/totem-pl-parser-devel.list

%changelog

%autochangelog
