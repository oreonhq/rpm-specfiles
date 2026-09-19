%global source0_hash 5488af8882293a79fb320baa03f1f3ddc219902dc4c9641069ca6a035fbe4bd4

Name:		mmseq
Version:	1.0.11
Release:	26%{?dist}
Summary:	Haplotype and isoform specific expression estimation for RNA-seq

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%endif

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/eturro/%{name}
Source0:	https://github.com/eturro/%{name}/archive/%{version}.zip
#Patch1:		mmseq-flags.patch
Patch2:		mmseq-zlib.patch

BuildRequires:  gcc-c++
BuildRequires:	make
BuildRequires:	boost-devel
BuildRequires:	perl-generators
BuildRequires:	htslib-devel
BuildRequires:	gsl-devel
BuildRequires:	zlib-devel
BuildRequires:	armadillo-devel
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%endif

Requires:	ruby
Requires:	samtools
Requires:	perl-interpreter

%description
Software for fast, scalable haplotype and isoform expression
estimation using multi-mapping RNA-seq reads.  Example scripts are included.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
#Use Fedora compilation headers
#%%patch1 -p1 -b .mmseq-flags.patch
#Fix zlib linking
%patch -P2 -p1 -b .mmseq-zlib.patch

# Remove bundled binaries
# Only 2 bin/*-linux files are included in Source0 archive.
rm -f bin/*-linux

%if %{with flexiblas}
sed -e 's/-lblas/-lflexiblas/g' -e 's/-llapack/-lflexiblas/g' -i src/Makefile
%endif

%build
cd src
make %{?_smp_mflags} CXXFLAGS="%{optflags}"

%check
# Check src/VERSION is correctly set.
test "$(bin/mmseq --version 2>&1 || true)" = "%{name}-%{version}"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 bin/bam2hits %{buildroot}%{_bindir}
install -p -m 0755 bin/extract_transcripts %{buildroot}%{_bindir}
install -p -m 0755 bin/hitstools %{buildroot}%{_bindir}
install -p -m 0755 bin/mmcollapse %{buildroot}%{_bindir}
install -p -m 0755 bin/mmdiff %{buildroot}%{_bindir}
install -p -m 0755 bin/mmseq %{buildroot}%{_bindir}
install -p -m 0755 bin/offsetGTF %{buildroot}%{_bindir}
install -p -m 0755 bin/t2g_hits %{buildroot}%{_bindir}
install -p -m 0755 bin/*.sh %{buildroot}%{_bindir}
install -p -m 0755 bin/*.rb %{buildroot}%{_bindir}
install -p -m 0755 bin/ensembl_gtf_to_gff.pl %{buildroot}%{_bindir}

%files
%doc README.md COPYING doc/
%{_bindir}/bam2hits
%{_bindir}/extract_transcripts
%{_bindir}/hitstools
%{_bindir}/mmcollapse
%{_bindir}/mmdiff
%{_bindir}/mmseq
%{_bindir}/offsetGTF
%{_bindir}/t2g_hits
%{_bindir}/fastagrep.sh
%{_bindir}/mouse_strain_transcriptome.sh
%{_bindir}/usage.sh
%{_bindir}/filterGTF.rb
%{_bindir}/haploref.rb
%{_bindir}/testregexp.rb
%{_bindir}/ensembl_gtf_to_gff.pl

%changelog
%autochangelog
