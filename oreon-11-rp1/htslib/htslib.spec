%global source0_hash 28a8de191381c7a97a35675ceac76fa1ea95e7b678d6a2e9d600a7874e4077de
%global so_version 3
Name: htslib
Version: 1.24
Release:        1%{?dist}
Summary:        C library for high-throughput sequencing data formats
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL: http://www.htslib.org
Source0:        https://github.com/samtools/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl-interpreter
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
HTSlib is an implementation of a unified C library for accessing common file
formats, such as SAM, CRAM and VCF, used for high-throughput sequencing data,
and is the core library used by samtools and bcftools.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Additional htslib-based tools
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Includes the popular tabix indexer, which creates both .tbi and .csi formats,
the htsfile identifier tool, and the bgzip compression utility.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --enable-plugins \
    --with-plugin-path='%{_usr}/local/libexec/htslib:$(plugindir)' \
    --enable-gcs \
    --enable-libcurl \
    --enable-s3
%make_build
sed -i -E '/^(Libs|Requires)\.private:/d' htslib.pc.tmp
%install
%make_install
pushd %{buildroot}/%{_libdir}
chmod 755 libhts.so.%{version}
popd
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}/%{_libdir}/libhts.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n htslib-devel -f %{oreon_filedir}/htslib-devel.list
%files -n htslib-tools -f %{oreon_filedir}/htslib-tools.list

%changelog

%autochangelog
