%global source0_hash 18757a3a1ff00d246275b46c3e819abf138824698a7bed8fa96fe3a7e69058cb

Name:           rep-gtk
Version:        0.90.8.3
Release:        25%{?dist}
Summary:        GTK+ binding for librep Lisp environment
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sawfish.wikia.com/
Source0:        http://download.tuxfamily.org/librep/%{name}/%{name}_%{version}.tar.bz2
Patch0: rep-gtk-c99.patch
Patch1: gcc14.patch
Patch2: gcc14-2.patch

BuildRequires: make
BuildRequires:  gtk2-devel
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  librep-devel >= 0.90.5
Requires:       librep >= 0.90.5

%description
This is a binding of GTK+ for the librep Lisp interpreter. It is based
on Marius Vollmer's guile-gtk package (initially version 0.15, updated
to 0.17), with a new glue-code generator.

%package devel
Summary:        Development files for rep-gtk
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Link libraries and C header files for librep development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}_%{version}

%build
./autogen.sh --nocfg
%configure CFLAGS="%{optflags} -Wno-incompatible-pointer-types"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot}%{_libdir} -name \*.la -exec rm '{}' \;

%files
%license COPYING
%doc NEWS README* TODO
%{_libdir}/rep/*

%files devel
%{_includedir}/rep-gtk/
%{_libdir}/pkgconfig/rep-gtk.pc

%changelog
%autochangelog
