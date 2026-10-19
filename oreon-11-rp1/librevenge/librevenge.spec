%global source0_hash 19eacf5ce55d7fe6a990a45142589cdf7da0c7b68701797f133482cb44f189fa
%global apiversion 0.0
Name: librevenge
Version: 0.0.6
Release:        1%{?dist}
Summary:        A base library for writing document import filters
License: ( LGPL-2.1-or-later OR MPL-2.0 ) AND BSD-3-Clause
URL: http://sourceforge.net/p/libwpd/wiki/librevenge/
Source0:        https://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
# /oreon:deps
%description
%{name} is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch
%description doc
The %{name}-doc package contains documentation files for %{name}.

%if ! 0%{?flatpak}
%package gdb
Summary: gdb pretty printers for %{name}
Requires: gdb
Requires: python3-six
Requires: %{name}%{?_isa} = %{version}-%{release}
Supplements: %{name}-debuginfo%{?_isa} = %{version}-%{release}
%description gdb
The %{name}-devel package contains gdb pretty printers that help with
debugging applications that use %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
    --disable-silent-rules \
    --disable-static \
%if ! 0%{?flatpak}
    --enable-pretty-printers
%endif
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}/%{name}
%py_byte_compile %{python3} %{buildroot}%{_datadir}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n librevenge-devel -f %{oreon_filedir}/librevenge-devel.list
%files -n librevenge-doc -f %{oreon_filedir}/librevenge-doc.list
%files -n librevenge-gdb -f %{oreon_filedir}/librevenge-gdb.list

%changelog

%autochangelog
