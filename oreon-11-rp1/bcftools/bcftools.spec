%global source0_hash 8caddc22610ee2851666047c859bb91da0c1e32d0c2ec553db6f153ad130e46f
Name: bcftools
Version: 1.24
Release:        1%{?dist}
Summary:        Tools for genomic variant calling and manipulating VCF/BCF files
License: GPL-3.0-or-later
URL: https://www.htslib.org/
Source0:        https://github.com/samtools/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Conflicts: samtools < 1.0
ExcludeArch: s390x
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gsl-devel
BuildRequires:  htslib-devel
BuildRequires:  htslib-tools
BuildRequires:  make
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-interpreter
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%check

ldd bcftools | grep -E '/lib(64)?(/lp64d)?/libhts\.so\.'
%ifarch i686
sed -i -E '/^test_vcf_convert_hs2vcf.+convert.gs.gt.ids.3N6.gen.+/ s/^/#/' test/test.pl
%endif
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
