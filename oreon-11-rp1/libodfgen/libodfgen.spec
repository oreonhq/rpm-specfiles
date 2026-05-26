%global apiversion 0.1

Name: libodfgen
Version: 0.1.8
Release: %autorelease
Summary: An ODF generator library

License: LGPL-2.1-or-later OR MPL-2.0
URL: https://sourceforge.net/p/libwpd/wiki/libodfgen/
Source: http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
Patch0: includes.patch
# oreon url source checksums begin
%global source0_sha256 55200027fd46623b9bdddd38d275e7452d1b0ff8aeddcad6f9ae6dc25f610625
%global source0_file libodfgen-0.1.8.tar.xz
# oreon url source checksums end

BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(libxml-2.0)

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libodfgen-0.1.8.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "55200027fd46623b9bdddd38d275e7452d1b0ff8aeddcad6f9ae6dc25f610625" || { echo "oreon: Source0 SHA256 mismatch for libodfgen-0.1.8.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

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
# we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

%ldconfig_scriptlets

%files
%doc README NEWS
%license COPYING.*
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING.*
%doc docs/doxygen/html

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.8-1
- Import
