%global source0_hash 6d27867256a35ccf9b69253eb2a88a32baca3b97d5f4ef7f82e3667fa435251c
Name:           libgxps
Version:        0.3.2
Release:        1%{?dist}
Summary:        GObject based library for handling and rendering XPS documents
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/libgxps
Source0:        https://ftp.gnome.org/pub/gnome/sources/%{name}/0.3/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  lcms2-devel
BuildRequires:  libarchive-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  meson
# /oreon:deps
%description
libgxps is a GObject based library for handling and rendering XPS
documents.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Command-line utility programs for manipulating XPS files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
The %{name}-tools contains command-line programs for manipulating XPS format
documents using the %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Denable-gtk-doc=true -Denable-man=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libgxps-devel -f %{oreon_filedir}/libgxps-devel.list
%files -n libgxps-tools -f %{oreon_filedir}/libgxps-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.2-12
- Prepare for Oreon 11 (RP1)
