%global source0_hash 104b7e791b6632745898e9b6a0037b7540235771a4d8c3bde2c764466ad912f1
%global apiversion 0.1
Name: libe-book
Version: 0.1.4
Release:        1%{?dist}
Summary:        A library for import of reflowable e-book formats
License: MPL-2.0
URL: https://sourceforge.net/projects/libebook/
Source0:        http://downloads.sourceforge.net/libebook/%{name}-%{version}.tar.xz
Patch0: 0001-fix-build-with-ICU-68.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(liblangtag)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
%{name} is a library for import of reflowable e-book formats.
Currently supported are PalmDoc, TealDoc, Plucker eBook, eReader eBook,
FictionBook v.2, TCR, zTXT and Broad Band eBook (LRF).

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
Summary: Tools to transform e-books into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform e-books into other formats.
Currently supported: XHTML, raw, text.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in ebook2html ebook2raw ebook2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 ebook2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libe-book-devel -f %{oreon_filedir}/libe-book-devel.list
%files -n libe-book-doc -f %{oreon_filedir}/libe-book-doc.list
%files -n libe-book-tools -f %{oreon_filedir}/libe-book-tools.list

%changelog

%autochangelog
