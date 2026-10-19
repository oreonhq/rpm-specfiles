%global source0_hash 4687a9cc96c32d7406e5072c4da150fca696c563e5cde62b024f82fa53d32332
%global apiversion 0.0
Name: libqxp
Version: 0.0.3
Release:        1%{?dist}
Summary:        Library for import of QuarkXPress documents
License: MPL-2.0
URL: http://wiki.documentfoundation.org/DLP/Libraries/libqxp
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
# /oreon:deps
%description
libqxp is library providing ability to interpret and import QuarkXPress
document formats into various applications. Currently it only supports
QuarkXPress 3.1-4.1.

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
Summary: Tools to transform QuarkXPress documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform QuarkXPress documents into other formats.
Currently supported: SVG, plain text, raw.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules --disable-static
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_docdir}/%{name}
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in qxp2raw qxp2svg qxp2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 qxp2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make %{?_smp_mflags} check
%files -f %{oreon_filedir}/main.list
%files -n libqxp-devel -f %{oreon_filedir}/libqxp-devel.list
%files -n libqxp-doc -f %{oreon_filedir}/libqxp-doc.list
%files -n libqxp-tools -f %{oreon_filedir}/libqxp-tools.list

%changelog

%autochangelog
