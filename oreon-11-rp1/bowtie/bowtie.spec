%global source0_hash e23517aa53846ef828172be911750cd05748522117efcbbe5a36f3241fb40761
Name:		bowtie
Version:	1.3.1
Release:        10%{?dist}
Summary:        An ultrafast, memory-efficient short read aligner
License:	Artistic-2.0 AND Zlib
URL:		http://bowtie-bio.sourceforge.net/index.shtml
Source0:        http://downloads.sourceforge.net/%{name}-bio/%{name}-%{version}-src.zip
Source1:	bowtie-%{version}-tests.tgz
Patch1:		bowtie-test-remove-perl-Sys-Info-dep.patch
Requires:	python3
ExcludeArch: i686 armv7hl
Provides: bundled(tiny-thread) = 1.1
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  hostname
BuildRequires:  make
BuildRequires:  perl(Clone)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(lib)
BuildRequires:  perl-interpreter
BuildRequires:  python3
BuildRequires:  tbb-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description

Bowtie, an ultrafast, memory-efficient short read aligner for short
DNA sequences (reads) from next-gen sequencers. Please cite: Langmead
B, et al. Ultrafast and memory-efficient alignment of short DNA
sequences to the human genome. Genome Biol 10:R25.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-src

# Remove the directory to avoid building bowtie with bundled libraries.
rm -rf third_party/

# Fix shebang to use system python3.
for file in $(find . -name "*.py") bowtie bowtie-*; do
  sed -E -i '1s|/usr/bin/env python[3]?|%{__python3}|' "${file}"
done

%build

%ifnarch x86_64
export POPCNT_CAPABILITY=0
%endif
CFLAGS=$(echo "${CFLAGS}" | sed -e 's/-Wp,-D_GLIBCXX_ASSERTIONS//')
export CFLAGS
CXXFLAGS=$(echo "${CXXFLAGS}" | sed -e 's/-Wp,-D_GLIBCXX_ASSERTIONS//')
export CXXFLAGS
%make_build allall EXTRA_FLAGS="-g"
%install
%make_install prefix="%{_prefix}"
mkdir -p %{buildroot}/%{_datadir}/bowtie
cp -a reads %{buildroot}/%{_datadir}/bowtie/
cp -a indexes %{buildroot}/%{_datadir}/bowtie/
cp -a genomes %{buildroot}/%{_datadir}/bowtie/
cp -a scripts %{buildroot}/%{_datadir}/bowtie/
for cmd in bowtie-*-debug; do
  cp -p "${cmd}" %{buildroot}/%{_bindir}/
done
%oreon_autofiles main

%check

for cmd in bowtie bowtie-build bowtie-inspect; do
  ./"${cmd}" --version | grep 'version %{version}'
done
tar xzvf %{SOURCE1}
cat %{PATCH1} | patch -p1
scripts/test/simple_tests.pl --bowtie=./bowtie --bowtie-build=./bowtie-build
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
