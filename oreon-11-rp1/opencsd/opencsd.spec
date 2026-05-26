%global opencsd_tag 78141e2f0ef8fb67284cc1a159cb62737666c965

Name:           opencsd
Version:        1.6.1
Release:        %autorelease
Summary:        An open source CoreSight(tm) Trace Decode library

License:        BSD-3-Clause
URL:            https://github.com/Linaro/OpenCSD
Source0:        https://github.com/Linaro/OpenCSD/archive/%{opencsd_tag}.tar.gz

Patch0:         0001-hack-test.patch
# oreon url source checksums begin
%global source0_sha256 58373fde4b4d377902e15211b163b326a680d464c15c475cad0e63e7ab05586d
%global source0_file 78141e2f0ef8fb67284cc1a159cb62737666c965.tar.gz
# oreon url source checksums end

BuildRequires:  patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make

%description
This library provides an API suitable for the decode of ARM(r)
CoreSight(tm) trace streams.

%package devel
Summary: Development files for the CoreSight(tm) Trace Decode library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The opencsd-devel package contains headers and libraries needed
to develop CoreSight(tm) trace decoders.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/78141e2f0ef8fb67284cc1a159cb62737666c965.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "58373fde4b4d377902e15211b163b326a680d464c15c475cad0e63e7ab05586d" || { echo "oreon: Source0 SHA256 mismatch for 78141e2f0ef8fb67284cc1a159cb62737666c965.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n OpenCSD-%{opencsd_tag}

%build
cd decoder/build/linux
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
LIB_PATH=%{_lib} make %{?_smp_mflags}

%install
cd decoder/build/linux
PREFIX=%{buildroot}%{_prefix} LIB_PATH=%{_lib} make install install_man DISABLE_STATIC=1 DEF_SO_PERM=755

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} decoder/tests/run_pkt_decode_tests.bash -bindir %{buildroot}%{_bindir}/ use-installed

%files
%license LICENSE
%doc HOWTO.md README.md
%{_libdir}/*so\.*
%{_bindir}/*
%{_mandir}/man1/trc_pkt_lister.1.gz

%files devel
%doc decoder/docs/prog_guide/*
%{_includedir}/*
# no man files..
%{_libdir}/*so

#------------------------------------------------------------------------------

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.1-1
- Import
