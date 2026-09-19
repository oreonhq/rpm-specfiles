%global source0_hash f0ecd4532a1d9aff962f5028cfcf191da84274c5d3a1200f57cfbeb545a54b3c

Summary:        Utilities for SAS management protocol (SMP)
Name:           smp_utils
Version:        0.99
Release:        15%{?dist}
License:        BSD-3-Clause
URL:            http://sg.danny.cz/sg/smp_utils.html
Source0:        http://sg.danny.cz/sg/p/%{name}-%{version}.tgz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: make
BuildRequires:  gcc

%description
This is a package of utilities. Each utility sends a Serial Attached
SCSI (SAS) Management Protocol (SMP) request to a SMP target.
If the request fails then the error is decoded. If the request succeeds
then the response is either decoded, printed out in hexadecimal or
output in binary. This package supports multiple interfaces since
SMP passthroughs are not mature. This package supports the linux
2.4 and 2.6 series and should be easy to port to other operating
systems.

Warning: Some of these tools access the internals of your system
and the incorrect usage of them may render your system inoperable.

%package libs
Summary: Shared library for %{name}

%description libs
This package contains the shared library for %{name}.

%package devel
Summary: Development library and header files for the smp_utils library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the %{name} library and its header files for
developing applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?smp_mflags} CFLAGS="%{optflags} -DSMP_UTILS_LINUX"

%install
make install \
        PREFIX=%{_prefix} \
        DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_libdir}/*.la

%files
%doc ChangeLog COPYING COVERAGE CREDITS README
%{_bindir}/*
%{_mandir}/man8/*

%files libs
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/scsi/*.h
%{_libdir}/*.so

%changelog
%autochangelog
