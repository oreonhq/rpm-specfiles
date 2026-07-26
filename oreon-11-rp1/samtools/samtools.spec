%global source0_hash 32266198a4bc6a6df395d8526688c9697d9c8e472f888c749fdde2e08ea88dd2

Name:		samtools
Version:	1.23.1
Release:	1%{?dist}
Summary:	Tools for nucleotide sequence alignments in the SAM format

License:	MIT
URL:		http://www.htslib.org/
Source0:	https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	gcc
BuildRequires:	htslib-devel
BuildRequires:	htslib-tools
BuildRequires:	make
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
# It's used in make test.
BuildRequires:	perl-interpreter
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(lib)

%description
SAM (Sequence Alignment/Map) is a flexible generic format for storing
nucleotide sequence alignment.
SAM Tools provide various utilities for manipulating alignments in the
SAM format, including sorting, merging, indexing and generating
alignments in a per-position format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Remove INSTALL file to suppress rpmlint warning.
rm -f INSTALL

%build
%configure CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" \
  --prefix=%{_prefix} \
  --with-htslib=system
%make_build

%install
%make_install

# Replace shebang for /usr/lib/rpm/redhat/brp-mangle-shebangs check.
for file in $(grep -l '^#!/usr/bin/env perl' %{buildroot}%{_bindir}/*); do
  sed -i '1 s|/usr/bin/env perl|/usr/bin/perl|' "${file}"
done

%check
# Check if samtools is built with system htslib.
ldd samtools | grep -E -e '/lib(64)?/libhts\.so\.' -e '/lib64/lp64d/libhts\.so\.'

make test

%files
%doc AUTHORS ChangeLog.old NEWS.md examples/
%license LICENSE
# We do not use a wildcard to list bin files, because this often leads
# to problems when the name changes or something additional is installed.
%{_bindir}/ace2sam
%{_bindir}/blast2sam.pl
%{_bindir}/bowtie2sam.pl
%{_bindir}/export2sam.pl
%{_bindir}/fasta-sanitize.pl
%{_bindir}/interpolate_sam.pl
%{_bindir}/maq2sam-long
%{_bindir}/maq2sam-short
%{_bindir}/md5fa
%{_bindir}/md5sum-lite
%{_bindir}/novo2sam.pl
%{_bindir}/plot-ampliconstats
%{_bindir}/plot-bamstats
%{_bindir}/psl2sam.pl
%{_bindir}/sam2vcf.pl
%{_bindir}/samtools
%{_bindir}/samtools.pl
%{_bindir}/seq_cache_populate.pl
%{_bindir}/soap2sam.pl
%{_bindir}/wgsim
%{_bindir}/wgsim_eval.pl
%{_bindir}/zoom2sam.pl
%{_mandir}/man1/samtools.1*
%{_mandir}/man1/samtools-*.1*
%{_mandir}/man1/wgsim.1*

%changelog
%autochangelog
