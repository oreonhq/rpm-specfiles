%global source0_hash 350b10d24a76d7e8c8ae98b74c2d432a2c8ddec08935d09856d20b695a35e600
%global apiversion 0.1
Name: libfreehand
Version: 0.1.4
Release:        1%{?dist}
Summary:        A library for import of Macromedia/Adobe FreeHand documents
License: MPL-2.0
URL: http://wiki.documentfoundation.org/DLP/Libraries/libfreehand
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
libfreehand is library providing ability to interpret and import
Macromedia/Adobe FreeHand documents into various applications.

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
Summary: Tools to transform Macromedia/Adobe FreeHand documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform Macromedia/Adobe FreeHand documents into other formats.
Currently supported: SVG, raw, text.

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
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in fh2raw fh2svg fh2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 fh2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libfreehand-devel -f %{oreon_filedir}/libfreehand-devel.list
%files -n libfreehand-doc -f %{oreon_filedir}/libfreehand-doc.list
%files -n libfreehand-tools -f %{oreon_filedir}/libfreehand-tools.list

%changelog

%autochangelog
