%global source0_hash 27051a30cb057fdb5d5de65a1f165c7153dc76e27fe62251cbb86639eb2caf22
%global apiversion 0.0
Name: libzmf
Version: 0.0.2
Release:        1%{?dist}
Summary:        A library for import of Zoner document formats
License: MPL-2.0
URL: http://wiki.documentfoundation.org/DLP/Libraries/libzmf
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
Patch: libzmf-install-docs.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
libzmf is library providing ability to interpret and import Zoner
document formats into various applications. Currently it only supports
Zoner Callisto/Draw v 4-5.

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

%package tools
Summary: Tools to transform Zoner documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform Zoner documents into other formats.
Currently supported: SVG, raw.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_docdir}/%{name}
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in zmf2raw zmf2svg; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 zmf2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libzmf-devel -f %{oreon_filedir}/libzmf-devel.list
%files -n libzmf-doc -f %{oreon_filedir}/libzmf-doc.list
%files -n libzmf-tools -f %{oreon_filedir}/libzmf-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.2-1
- Prepare for Oreon 11 (RP1)
