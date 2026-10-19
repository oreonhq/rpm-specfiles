%global source0_hash 18757a3a1ff00d246275b46c3e819abf138824698a7bed8fa96fe3a7e69058cb
Name:           rep-gtk
Version:        0.90.8.3
Release:        1%{?dist}
Summary:        GTK+ binding for librep Lisp environment
License:        GPL-2.0-or-later
URL:            http://sawfish.wikia.com/
Source0:        http://download.tuxfamily.org/librep/%{name}/%{name}_%{version}.tar.bz2
Patch0: rep-gtk-c99.patch
Patch1: gcc14.patch
Patch2: gcc14-2.patch
Requires:       librep >= 0.90.5
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gtk2-devel
BuildRequires:  librep-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
%global oreon_srcdir %{name}_%{version}
%oreon_prep
%build

./autogen.sh --nocfg
%configure CFLAGS="%{optflags} -Wno-incompatible-pointer-types"
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
find %{buildroot}%{_libdir} -name \*.la -exec rm '{}' \;
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rep-gtk-devel -f %{oreon_filedir}/rep-gtk-devel.list

%changelog

%autochangelog
