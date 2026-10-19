%global source0_hash d14030ce6122727935fbd676d0876808da1e112721f3cb108564a4d9bf73da71
%if 0%{?fedora} > 31 || 0%{?rhel} > 7 || 0%{?oreon} >= 11
%global _without_python2 1
%else
%global _with_python2 1
%endif
Name:           libewf
Version:        20140608
Release:        33%{?dist}
Summary:        Library for the Expert Witness Compression Format (EWF)
License:        LGPL-3.0-or-later
URL:            http://sourceforge.net/projects/libewf/
Source0:        https://src.fedoraproject.org/repo/pkgs/libewf/%{name}-%{version}.tar.gz/fdf615f23937fad8e02b60b9e3e5fb35/%{name}-%{version}.tar.gz
Patch0:         libewf-ewfoutput-openssl3.diff
%if 0%{?_with_python2}
%endif
# oreon:deps
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Libewf is a library for support of the Expert Witness Compression Format (EWF),
it support both the SMART format (EWF-S01) and the EnCase format (EWF-E01). 
Libewf allows you to read and write media information within the EWF files.

%package -n     ewftools
Summary:        Utilities for the Expert Witness Compression Format (EWF)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-tools = %{version}-%{release}
Obsoletes:      %{name}-tools <= %{version}-%{release}
%if 0%{?_with_python2}
Requires:       python2-fuse >= 0.2
%endif
%description -n ewftools
Several tools for reading and writing EWF files.
It contains tools to acquire, verify and export EWF files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static \
  --enable-wide-character-type \
%if 0%{?_with_python2}
  --enable-python \
%endif
%if "%{version}" <= "20140608"
  CFLAGS="${RPM_OPT_FLAGS} -std=gnu89"
%endif
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles ewftools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ewftools -f %{oreon_filedir}/ewftools.list
%files -n libewf-devel -f %{oreon_filedir}/libewf-devel.list

%changelog

%autochangelog
