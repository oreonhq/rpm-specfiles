%global source0_hash f8a3f36effeec38f043c53ab1f2d9ed45064f14205c5ef8e3c815763b90803c4

# The value of Makefile LIBHTS_SOVERSION.
%global so_version 3

Name: htslib
Version: 1.23.1
Release: 1%{?dist}
Summary: C library for high-throughput sequencing data formats

# The entire source code is MIT/Expat except cram/ which is Modified-BSD.
# But as there is no "Expat" license in short name list, set "MIT".
# Expat license is same with MIT license.
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/C5AHVIW3F6LF5CYLR2PSHNANFYKP327P/
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL: http://www.htslib.org
Source0: https://github.com/samtools/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: bzip2-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel
# It's used in make test.
BuildRequires: perl-interpreter
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(lib)
BuildRequires: make

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

# As we don't install libhts.a, the .private keywords are irrelevant.
sed -i -E '/^(Libs|Requires)\.private:/d' htslib.pc.tmp

%install
%make_install
pushd %{buildroot}/%{_libdir}
chmod 755 libhts.so.%{version}
popd

find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}/%{_libdir}/libhts.a

%check
make test

%ldconfig_scriptlets

%files
%license LICENSE
%doc NEWS
%{_libdir}/libhts.so.%{version}
%{_libdir}/libhts.so.%{so_version}
# The plugin so files should be in the main package,
# as they are loaded when libhts.so.%%{so_version} is used.
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/hfile_gcs.so
%{_libexecdir}/%{name}/hfile_libcurl.so
%{_libexecdir}/%{name}/hfile_s3.so
# The man5 pages are aimed at users.
%{_mandir}/man5/faidx.5*
%{_mandir}/man5/sam.5*
%{_mandir}/man5/vcf.5*
%{_mandir}/man7/htslib-s3-plugin.7*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libhts.so
%{_libdir}/pkgconfig/htslib.pc

%files tools
%{_bindir}/annot-tsv
%{_bindir}/bgzip
%{_bindir}/htsfile
%{_bindir}/ref-cache
%{_bindir}/tabix
%{_mandir}/man1/annot-tsv.1.gz
%{_mandir}/man1/bgzip.1*
%{_mandir}/man1/htsfile.1*
%{_mandir}/man1/ref-cache.1.gz
%{_mandir}/man1/tabix.1*

%changelog
%autochangelog
