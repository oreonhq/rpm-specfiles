%global source0_hash 6492b2beb26c3179cdd19abc90dc47a685be471c594d5ab664283e1d3586acdc

#global release_date 5Aug09
%{!?release_func:%global release_func() %1%%{?release_date:.%%release_date}%%{?dist}}
%define version_number 1.0.3

Name:           CVector
Version:        %{version_number}.1
Release:        %release_func 36
Summary:        ANSI C API for Dynamic Arrays

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://cvector.sourceforge.net/
%if 0%{?release_date:1}
Source0:        http://downloads.sourceforge.net/project/cvector/cvector/CVector-%{version}/CVector-%{version}-%{release_date}.tar.gz
%else
Source0:        http://downloads.sourceforge.net/project/cvector/cvector/CVector-1.0.3/CVector-%{version}.tar.gz
%endif
# to fix /-dynamic/-rdynamic/ issue, reported to upstream
Patch0:         CVector-1.0.3.1-dynamic.patch
# to fix libdir for lib64 architecture
Patch1:         CVector-1.0.3-lib64.patch

BuildRequires:  libtool
BuildRequires: make

%description
CVector is an ANSI C implementation of dynamic arrays to provide a
crude approximation to the C++ vector class.

%package devel
Summary:        Development tools for compiling programs using CVector
Requires:       %{name} = %{version}-%{release}

%description devel
The CVector-devel package includes the header and library files for
developing applications that use CVector.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .dynamic
%if "%{_lib}" == "lib64"
%patch -P1 -p1 -b .lib64
%endif

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install CFLAGS="%{optflags}" INSTALL_PREFIX="%{buildroot}%{_prefix}"

# remove .la and .a files
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%check
make tests

%ldconfig_scriptlets

%files
%doc README_CVector.html README_CVector.txt lgpl.txt
%{_libdir}/libCVector-%{version_number}.so.*

%files devel
%{_includedir}/CVector.h
%{_libdir}/libCVector.so

%changelog
%autochangelog
