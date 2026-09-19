%global source0_hash 4277f799245f1efde01cd917fd538ba6b12cf91c9f8a73fe2035fd5456ec078d

%global xfceversion 4.20

Name:           exo
Version:        4.20.0
Release:        %autorelease
Summary:        Application library for the Xfce desktop environment

# libexo-hal exo-helper mount-notify and exo-mount are all GPLv2+
# everything else is LGPLv2+
# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            http://xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  gettext
BuildRequires:  perl-URI
BuildRequires:  pkgconfig(glib-2.0) >= 2.24.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  libnotify-devel
BuildRequires:  intltool >= 0.31
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  make

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

%files -f exo.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS THANKS
%{_bindir}/exo-desktop-item-edit
%{_bindir}/exo-open
%{_libdir}/libexo-2.so.0
%{_libdir}/libexo-2.so.0.1.0
%{_datadir}/pixmaps/exo
%{_mandir}/man1/exo-open.1.*

%files devel
%doc %{_datadir}/gtk-doc
%{_includedir}/exo*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
