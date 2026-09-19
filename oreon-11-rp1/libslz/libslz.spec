%global source0_hash c1fa88556e97541a550e59fd1f0fc8f6b4c02444b14c13eb553c9827123122c5

Name:           libslz
Version:        1.2.1
Release:        5%{?dist}
Summary:        StateLess Zip

License:        MIT
URL:            http://www.libslz.org/
Source:         https://github.com/wtarreau/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make

%description
SLZ is a fast and memory-less stream compressor which produces an output that
can be decompressed with zlib or gzip. It does not implement decompression at
all, zlib is perfectly fine for this.

The purpose is to use SLZ in situations where a zlib-compatible stream is
needed and zlib's resource usage would be too high while the compression ratio
is not critical. The typical use case is in HTTP servers and gateways which
have to compress many streams in parallel with little CPU resources to assign
to this task, and without having to limit the compression ratio due to the
memory usage. In such an environment, the server's memory usage can easily be
divided by 10 and the CPU usage by 3.

%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for SLZ, the zenc and zdec commands that respectively
compress using SLZ and dump the decoding process.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build CFLAGS="%{optflags}" LIB_LFLAGS='%{?__global_ldflags}'

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} STRIP=/bin/true
rm %{buildroot}%{_libdir}/*.a

%files
%doc README
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_bindir}/*
%{_includedir}/*

%changelog
%autochangelog
