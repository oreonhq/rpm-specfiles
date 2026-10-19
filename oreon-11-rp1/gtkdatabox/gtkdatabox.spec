%global source0_hash 8bee70206494a422ecfec9a88d32d914c50bb7a0c0e8fedc4512f5154aa9d3e3
Name:           gtkdatabox
Version:        1.0.0
Release:        1%{?dist}
Summary:        GTK+ widget for fast data display
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/gtkdatabox
Source0:        http://downloads.sourceforge.net/%{name}-1/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  glade-devel
BuildRequires:  gtk3-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
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
%oreon_prep
%build

autoconf
%configure \
  --disable-static \
  --enable-glade \
  LIBS="-lm"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.tmp && mv -f ChangeLog.tmp ChangeLog
%make_build
%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtkdatabox-devel -f %{oreon_filedir}/gtkdatabox-devel.list
%files -n gtkdatabox-glade -f %{oreon_filedir}/gtkdatabox-glade.list

%changelog

%autochangelog
