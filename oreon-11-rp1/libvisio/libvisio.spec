%global source0_hash 2a6efd40b6d9dbcb70fba3be53112366882ba97b57151df3698dfa478c8d8dd3
%global apiversion 0.1
Name: libvisio
Version: 0.1.11
Release:        1%{?dist}
Summary:        A library for import of Microsoft Visio diagrams
License: MPL-2.0
URL: http://wiki.documentfoundation.org/DLP/Libraries/libvisio
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
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
%{name} is library providing ability to interpret and import
Microsoft Visio diagrams into various applications. You can find it
being used in LibreOffice.

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
Summary: Tools to transform Microsoft Visio diagrams into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform Microsoft Visio diagrams into other formats.
Currently supported: XHTML, raw, plain text.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static --disable-silent-rules
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
for tool in vsd2raw vss2text vsd2xhtml vss2raw vsd2text vss2xhtml; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 vsd2*.1 vss2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make check %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list
%files -n libvisio-devel -f %{oreon_filedir}/libvisio-devel.list
%files -n libvisio-doc -f %{oreon_filedir}/libvisio-doc.list
%files -n libvisio-tools -f %{oreon_filedir}/libvisio-tools.list

%changelog

%autochangelog
