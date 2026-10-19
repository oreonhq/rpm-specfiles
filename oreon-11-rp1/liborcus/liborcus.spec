%global source0_hash 3555660197d6d38d720643f430804bb0f95a484c1fe6c28c00808ae67f978d15
%global apiversion 0.21
%bcond_without convtools
%bcond_without python
Name: liborcus
Version: 0.21.0
Release:        1%{?dist}
Summary:        Standalone file import filter library for spreadsheet documents
License: MPL-2.0
URL: https://gitlab.com/orcus/orcus
Source0:        https://gitlab.com/orcus/orcus/-/archive/%{version}/orcus-%{version}.tar.bz2
Patch0: include.patch
%if %{with convtools}
%endif
%if %{with python}
%endif
# oreon:deps
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  chrpath
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libixion-0.20)
BuildRequires:  pkgconfig(mdds-3.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%if %{with convtools}
%package model
Summary: Spreadsheet model for %{name} conversion tools
Requires: %{name}%{?_isa} = %{version}-%{release}
%description model
The %{name}-model package contains a spreadsheet model used by the
conversion tools.
%endif

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Tools for working with %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Helper tools for %{name} and converters of various file formats to HTML
and text.

%if %{with python}
%package python3
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description python3
Python 3 bindings for %{name}.
%endif

%package doc
Summary: API documentation for %{name}
BuildArch: noarch
%description doc
API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n orcus-%{version} -p0

%if %{without convtools}
%global condopts %{?condopts} --disable-spreadsheet-model
%endif
%if %{without python}
%global condopts %{?condopts} --disable-python
%endif

%build

NOCONFIGURE=1 ./autogen.sh
%configure --disable-debug --disable-silent-rules --disable-static \
    --disable-werror --with-pic %{?condopts}
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{python3_sitearch}/*.la
%if %{with convtools}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -S '%{name} %{version}' -n 'convert a CSV file' -o orcus-csv.1 %{buildroot}%{_bindir}/orcus-csv
help2man -N -S '%{name} %{version}' -n 'convert a Gnumeric file' -o orcus-gnumeric.1 %{buildroot}%{_bindir}/orcus-gnumeric
help2man -N -S '%{name} %{version}' -n 'convert an ODF spreadsheet' -o orcus-ods.1 %{buildroot}%{_bindir}/orcus-ods
help2man -N -S '%{name} %{version}' -n 'transform an XML file' -o orcus-xls-xml.1 %{buildroot}%{_bindir}/orcus-xls-xml
help2man -N -S '%{name} %{version}' -n 'convert a OpenXML spreadsheet' -o orcus-xlsx.1 %{buildroot}%{_bindir}/orcus-xlsx
help2man -N -S '%{name} %{version}' -n 'convert an XML file' -o orcus-xml.1 %{buildroot}%{_bindir}/orcus-xml
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -p -m 0644 orcus-*.1 %{buildroot}/%{_mandir}/man1
%endif
make doc-doxygen
find %{buildroot}/%{_bindir} -type f -name 'orcus-*' -print0 | xargs -0 chrpath --delete
find %{buildroot}/%{_libdir} -type f -name '*.so.*' -print0 | xargs -0 chrpath --delete
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%check

%ldconfig_scriptlets
%if %{with convtools}
%ldconfig_scriptlets model
%endif
%files -f %{oreon_filedir}/main.list
%files -n liborcus-model -f %{oreon_filedir}/liborcus-model.list
%files -n liborcus-devel -f %{oreon_filedir}/liborcus-devel.list
%files -n liborcus-tools -f %{oreon_filedir}/liborcus-tools.list
%files -n liborcus-python3 -f %{oreon_filedir}/liborcus-python3.list
%files -n liborcus-doc -f %{oreon_filedir}/liborcus-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.21.0-1
- Prepare for Oreon 11 (RP1)
