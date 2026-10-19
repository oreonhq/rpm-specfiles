%global source0_hash 4277f799245f1efde01cd917fd538ba6b12cf91c9f8a73fe2035fd5456ec078d
%global xfceversion 4.20
Name:           exo
Version:        4.20.0
Release:        1%{?dist}
Summary:        Application library for the Xfce desktop environment
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            http://xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libnotify-devel
BuildRequires:  make
BuildRequires:  perl-URI
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(libxfce4util-1.0)
# /oreon:deps
%description
Extension library for Xfce, targeted at application development.

%package        devel
Summary:        Development tools for exo library
Requires:       %{name} = %{version}-%{release}
Requires:       libxfce4util-devel
Requires:       pkgconfig
%description devel
Development tools and static libraries and header files for the exo library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --enable-gtk-doc --disable-static
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang exo
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n exo-devel -f %{oreon_filedir}/exo-devel.list

%changelog

%autochangelog
