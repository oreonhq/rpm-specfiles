%global source0_hash b2fb836ea0b5253a352fb5ca55742e29f06f94f9421c5b8eeccef2e5d43f622c
Name:           libxls
Version:        1.6.3
Release:        1%{?dist}
Summary:        Read binary Excel files from C/C++
License:        BSD-2-Clause
URL:            https://github.com/libxls/libxls
Source0:        https://github.com/libxls/libxls/releases/download/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
This is libxls, a C library for reading Excel files in the old binary OLE
format, plus a command-line tool for converting XLS to CSV (named,
appropriately enough, libxls2csv).

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --program-prefix=lib
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

PATH=%{buildroot}%{_bindir}:$PATH LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
    make check || ( cat ./test-suite.log && exit 1 )
%files -f %{oreon_filedir}/main.list
%files -n libxls-devel -f %{oreon_filedir}/libxls-devel.list

%changelog

%autochangelog
