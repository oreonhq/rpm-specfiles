%global source0_hash 5488af8882293a79fb320baa03f1f3ddc219902dc4c9641069ca6a035fbe4bd4
Name:		mmseq
Version:	1.0.11
Release:        1%{?dist}
Summary:        Haplotype and isoform specific expression estimation for RNA-seq
License:	GPL-2.0-or-later
URL:		https://github.com/eturro/%{name}
Source0:        https://github.com/eturro/%{name}/archive/%{version}.zip
Patch2:		mmseq-zlib.patch
%if %{with flexiblas}
%endif
Requires:	ruby
Requires:	samtools
Requires:	perl-interpreter
# oreon:deps
BuildRequires:  armadillo-devel
BuildRequires:  boost-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  htslib-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
