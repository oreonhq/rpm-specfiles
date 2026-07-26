%global source0_hash d14030ce6122727935fbd676d0876808da1e112721f3cb108564a4d9bf73da71

%if 0%{?fedora} > 31 || 0%{?rhel} > 7
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
Source0:        https://53efc0a7187d0baa489ee347026b8278fe4020f6.googledrive.com/host/0B3fBvzttpiiSMTdoaVExWWNsRjg/%{name}-%{version}.tar.gz
Patch0:         libewf-ewfoutput-openssl3.diff

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  fuse-devel
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
#Needed for mount.ewf(.py) support
%if 0%{?_with_python2}
BuildRequires:  python2-devel
%endif

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
#Requires:       disktype
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

%autosetup -p1

%build
# FIXME: Package suffers from c11/inline issues
# Workaround by appending -std=gnu89 to CFLAGS
# Proper fix would be to fix the source-code
%configure --disable-static \
  --enable-wide-character-type \
%if 0%{?_with_python2}
  --enable-python \
%endif
%if "%{version}" <= "20140608"
  CFLAGS="${RPM_OPT_FLAGS} -std=gnu89"
%endif

# Remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/*.so.*

%files -n ewftools
%{_bindir}/ewf*
%{_mandir}/man1/*.gz
%if 0%{?_with_python2}
%{python2_sitearch}/pyewf.so
%endif

%files devel
%{_includedir}/libewf.h
%{_includedir}/libewf/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libewf.pc
%{_mandir}/man3/*.gz

%changelog
%autochangelog
