%global source0_hash 01899a46f9420cdc1385d52fcfc84cce2806f9c996b787081a90d7dfc85eafa3

Name: bcftools
Version: 1.23.1
Release: 1%{?dist}
Summary: Tools for genomic variant calling and manipulating VCF/BCF files

# This software is available under a choice of one of two licenses,
# the MIT/Expat (MIT) or the GNU General Public License Version 3
# (GPL-3.0-or-later).
# And if compiled with the GNU Scientific Library, in this case it is built
# with --enable-libgsl, the use of this software is governed by the
# GPL-3.0-or-later license.
# See <https://github.com/samtools/bcftools/blob/develop/LICENSE>.
License: GPL-3.0-or-later
# https:// is better than http://.
URL: https://www.htslib.org/
Source0: https://github.com/samtools/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: gsl-devel
BuildRequires: htslib-devel
BuildRequires: htslib-tools
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
BuildRequires: zlib-devel
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
# bcftools had been included in samtools version 0.X.
# https://github.com/samtools/samtools/commit/e7ae7f96c7e78a2dd6eabdaed57037c483951929
Conflicts: samtools < 1.0
# A big-endian (s390x) environment is not supported.
# https://github.com/samtools/htslib/issues/355
ExcludeArch: s390x

%description
BCFtools is a set of utilities that manipulate genomic variant calls in the
Variant Call Format (VCF) and its binary counterpart (BCF). All commands work
transparently with both VCFs and BCFs, both uncompressed and BGZF-compressed.

(This BCFtools includes the polysomy subcommand, which is implemented using
the GNU Scientific Library. Hence this package is licensed according to the
GNU General Public License, rather than the MIT license used when BCFtools
is built without the polysomy subcommand.)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i '1s|/usr/bin/env perl|/usr/bin/perl|' misc/*.pl misc/plot-vcfstats
sed -i '1s|/usr/bin/env python3\{0,1\}|%{__python3}|' misc/*.py

%build
# needed because we patch configure.ac
autoreconf -fiv

%configure CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" \
  --prefix=%{_prefix} \
  --with-htslib=system \
  --enable-perl-filters \
  --enable-libgsl \
  --with-bcf-plugin-path='%{_usr}/local/libexec/bcftools:$(plugindir)'
%make_build

%install
%make_install

%check
# Check if bcftools is built with system htslib.
# /lib64/lp64d/ exists on riscv64
ldd bcftools | grep -E '/lib(64)?(/lp64d)?/libhts\.so\.'

%ifarch i686
# Skip 2 failed tests.
# https://github.com/samtools/bcftools/issues/1776
sed -i -E '/^test_vcf_convert_hs2vcf.+convert.gs.gt.ids.3N6.gen.+/ s/^/#/' test/test.pl
%endif
make test

%files
%doc AUTHORS NEWS
%license LICENSE
# We do not use a wildcard to list bin files, because this often leads
# to problems when the name changes or something additional is installed.
%{_bindir}/bcftools
%{_bindir}/color-chrs.pl
%{_bindir}/gff2gff
%{_bindir}/gff2gff.py
%{_bindir}/guess-ploidy.py
%{_bindir}/plot-roh.py
%{_bindir}/plot-vcfstats
%{_bindir}/roh-viz
%{_bindir}/run-roh.pl
%{_bindir}/vcfutils.pl
%{_bindir}/vrfs-variances
%{_libexecdir}/bcftools
%{_mandir}/man1/bcftools.1*

%changelog
%autochangelog
