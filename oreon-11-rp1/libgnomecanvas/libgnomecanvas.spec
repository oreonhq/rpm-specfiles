%global source0_hash 859b78e08489fce4d5c15c676fec1cd79782f115f516e8ad8bed6abcb8dedd40

%define gettext_package libgnomecanvas-2.0

Summary: GnomeCanvas widget
Name: libgnomecanvas
Version: 2.30.3
Release: 33%{?dist}
URL: http://www.gnome.org/
Source0: http://download.gnome.org/sources/libgnomecanvas/2.30/%{name}-%{version}.tar.bz2
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
BuildRequires: gtk2-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libglade2-devel 
BuildRequires: gail-devel
BuildRequires: libtool gettext
BuildRequires: intltool
BuildRequires: make

%description
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%package devel
Summary: Libraries and headers for libgnomecanvas
Requires: %{name} = %{version}-%{release}
# for /usr/share/gtk-doc/html
Requires: gtk-doc

%description devel
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-gtk-doc --enable-glade --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} 

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{gettext_package}

%ldconfig_scriptlets

%files -f %{gettext_package}.lang
%doc COPYING.LIB AUTHORS NEWS README
%{_libdir}/lib*.so.*
%{_libdir}/libglade/2.0/libcanvas.so

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/libgnomecanvas

%changelog
%autochangelog
