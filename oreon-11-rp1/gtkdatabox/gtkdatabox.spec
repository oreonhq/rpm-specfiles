%global source0_hash 8bee70206494a422ecfec9a88d32d914c50bb7a0c0e8fedc4512f5154aa9d3e3

Name:           gtkdatabox
Version:        1.0.0
Release:        14%{?dist}
Summary:        GTK+ widget for fast data display
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/gtkdatabox
Source:         http://downloads.sourceforge.net/%{name}-1/%{name}-%{version}.tar.gz
# Fixed configure archive downloaded from https://sourceforge.net/projects/gtkdatabox/files/gtkdatabox-1/
# https://sourceforge.net/p/gtkdatabox/bugs/13/

BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  pkgconfig
BuildRequires:  autoconf
BuildRequires:  glade-devel
BuildRequires:  make

%description
GtkDatabox is a widget for the GTK+ library designed to display
large amounts of numerical data fast and easy.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries, header files, and examples
for developing applications that use %{name}.

%package        glade
Summary:        Glade 3 support files for %{name}
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-libglade
Obsoletes:      %{name}-libglade2

%description    glade
The %{name}-glade package contains support files for glade.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# need reconfig to support aarch64
autoconf
%configure \
  --disable-static \
  --enable-glade \
  LIBS="-lm"
# fix rpath libtool issues
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# fix ChangeLog encoding issues
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.tmp && mv -f ChangeLog.tmp ChangeLog
%make_build

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_libdir}/libgtkdatabox*.so.*
%{_datadir}/icons/hicolor/scalable/apps/widget-gladedatabox-gtk_databox.svg
%{_datadir}/icons/hicolor/scalable/apps/widget-gladedatabox-gtk_databox_ruler.svg

%files devel
%doc examples/*.c
%{_includedir}/gtkdatabox*.h
%{_libdir}/libgtkdatabox.so
%{_libdir}/pkgconfig/gtkdatabox.pc
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/gtkdatabox-1/

%files glade
%{_libdir}/glade/modules/libgladedatabox.so
%{_datadir}/glade/catalogs/gtkdatabox.xml

%changelog
%autochangelog
