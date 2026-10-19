%global source0_hash 55200027fd46623b9bdddd38d275e7452d1b0ff8aeddcad6f9ae6dc25f610625
%global apiversion 0.1
Name: libodfgen
Version: 0.1.8
Release:        1%{?dist}
Summary:        An ODF generator library
License: LGPL-2.1-or-later OR MPL-2.0
URL: https://sourceforge.net/p/libwpd/wiki/libodfgen/
Source0:        https://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
Patch0:        includes.patch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
%{name} is a library for generating ODF documents. It is directly
pluggable into input filters based on librevenge. It is used in
libreoffice or calligra, for example.

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

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libodfgen-0.1.8
%oreon_prep
%build

%configure --disable-silent-rules --disable-static
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_docdir}/%{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libodfgen-devel -f %{oreon_filedir}/libodfgen-devel.list
%files -n libodfgen-doc -f %{oreon_filedir}/libodfgen-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.8-1
- Import
