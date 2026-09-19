%global source0_hash 9e1f00c4c9f286be59ac0e07ddb7504f3b6433c93c5c7941d6e3208306ff5806

Name:		fastx_toolkit
Version:	0.0.14
Release:	39%{?dist}
Summary:	Tools to process short-reads FASTA/FASTQ files

License:	AGPL-3.0-or-later
URL:		http://hannonlab.cshl.edu/%{name}/index.html
Source0:	http://hannonlab.cshl.edu/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-gcc47.patch

BuildRequires:  gcc-c++
BuildRequires:	libgtextutils-devel
BuildRequires:	perl-generators
BuildRequires: make
# FASTX-Barcode-Splitter requires the GNU Sed program.
Requires:	sed
# fasta_clipping_histogram requires PerlIO::gzip and GD::Graph::bars
Requires:	perl-PerlIO-gzip
Requires:	perl-GDGraph

%description

The FASTX-Toolkit is a collection of command line tools for
Short-Reads FASTA/FASTQ files preprocessing.

Next-Generation sequencing machines usually produce FASTA or FASTQ
files, containing multiple short-reads sequences (possibly with
quality information).

The main processing of such FASTA/FASTQ files is mapping (aka
aligning) the sequences to reference genomes or other databases using
specialized programs. Example of such mapping programs are: Blat,
SHRiMP, LastZ, MAQ and many many others.

However, It is sometimes more productive to preprocess the FASTA/FASTQ
files before mapping the sequences to the genome - manipulating the
sequences to produce better mapping results.

The FASTX-Toolkit tools perform some of these preprocessing tasks. 

%package       galaxy
Summary:       Integrate fastx_toolkit with a local Galaxy installation
Requires:      %{name} = %{version}-%{release}

%description   galaxy

These files allow the integration of fastx_toolkit with a local
installation of Galaxy (http://main.g2.bx.psu.edu/), a web-based
platform for analyzing multiple alignments, comparing genomic
annotations, profiling metagenomic samples and much more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#Patch to fix compilation with GCC 4.7
%patch -P0 -p1 -b .%{name}-gcc47.patch

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

mkdir %{buildroot}/%{_datadir}/%{name}
cp -a galaxy/ %{buildroot}/%{_datadir}/%{name}

# remove unnecessary m4 files
rm %{buildroot}/%{_datadir}/aclocal/*.m4

# remove autotools Makefile
find %{buildroot}/%{_datadir}/%{name}/galaxy/ -name "Makefile\.*" -delete

%files
%doc AUTHORS COPYING NEWS README THANKS
%{_bindir}/fast*

%files	galaxy
%{_datadir}/%{name}

%changelog
%autochangelog
