%global source0_hash 24958dd0fb6725b9476190e3be6d120262b8e3093b71614ca19855d2843f9682

Name:		bowtie
Version:	1.3.1
Release:	10%{?dist}
Summary:	An ultrafast, memory-efficient short read aligner

# bowite: Artistic 2.0
# tinythread.{h,cpp}: zlib
# Automatically converted from old format: Artistic 2.0 and zlib - review is highly recommended.
License:	Artistic-2.0 AND Zlib
URL:		http://bowtie-bio.sourceforge.net/index.shtml
Source0:	http://downloads.sourceforge.net/%{name}-bio/%{name}-%{version}-src.zip
# git clone https://github.com/BenLangmead/bowtie.git
# cd bowtie
# git checkout v1.3.1
# tar czvf bowtie-1.3.1-tests.tgz scripts/test/
Source1:	bowtie-%{version}-tests.tgz
# Remove perl-Sys-Info module depenency, as it does not exist on Fedora.
Patch1:		bowtie-test-remove-perl-Sys-Info-dep.patch
Requires:	python3
BuildRequires:	gcc-c++
BuildRequires:	hostname
BuildRequires:	perl-interpreter
BuildRequires:	perl(Clone)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(lib)
BuildRequires:	python3
BuildRequires:	tbb-devel
BuildRequires:	zlib-devel
BuildRequires: make
# 32-bit CPU architectures are not supported for bowtie version >= 1.1.0.
# https://github.com/BenLangmead/bowtie/commit/5f90d3fdad97a8181ddaa96c64faeef1f2b6edf9
ExcludeArch: i686 armv7hl

# Bundled libraries
# https://fedoraproject.org/wiki/Bundled_Libraries?rd=Packaging:Bundled_Libraries#Requirement_if_you_bundle
# TinyThread++
# https://tinythreadpp.bitsnbites.eu/
# https://gitorious.org/tinythread/tinythreadpp
Provides: bundled(tiny-thread) = 1.1

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
# Set flags considering bowtie2's testing cases for each architecture.
# https://github.com/BenLangmead/bowtie2/blob/master/.travis.yml
# https://github.com/BenLangmead/bowtie/pull/102
%ifnarch x86_64
export POPCNT_CAPABILITY=0
%endif

# A workaround to pass the tests.
# Cline paired 2 (fw:1, sam:1) test aborted with -Wp,-D_GLIBCXX_ASSERTIONS
# https://github.com/BenLangmead/bowtie/issues/136
CFLAGS=$(echo "${CFLAGS}" | sed -e 's/-Wp,-D_GLIBCXX_ASSERTIONS//')
export CFLAGS
CXXFLAGS=$(echo "${CXXFLAGS}" | sed -e 's/-Wp,-D_GLIBCXX_ASSERTIONS//')
export CXXFLAGS

# Set debug flag "-g" to prevent the error
# "Empty %%files file debugsourcefiles.list".
%make_build allall EXTRA_FLAGS="-g"

%install
%make_install prefix="%{_prefix}"

mkdir -p %{buildroot}/%{_datadir}/bowtie
cp -a reads %{buildroot}/%{_datadir}/bowtie/
cp -a indexes %{buildroot}/%{_datadir}/bowtie/
cp -a genomes %{buildroot}/%{_datadir}/bowtie/
cp -a scripts %{buildroot}/%{_datadir}/bowtie/

# Install bowtie-*-debug commands used by `bowtie --debug`.
for cmd in bowtie-*-debug; do
  cp -p "${cmd}" %{buildroot}/%{_bindir}/
done

%check
for cmd in bowtie bowtie-build bowtie-inspect; do
  ./"${cmd}" --version | grep 'version %{version}'
done

tar xzvf %{SOURCE1}
cat %{PATCH1} | patch -p1

# See Makefile simple-test target.
scripts/test/simple_tests.pl --bowtie=./bowtie --bowtie-build=./bowtie-build

%files
%license LICENSE
%doc MANUAL NEWS VERSION AUTHORS TUTORIAL doc/{manual.html,style.css}
%dir %{_datadir}/bowtie
%{_bindir}/bowtie
%{_bindir}/bowtie-align-l
%{_bindir}/bowtie-align-l-debug
%{_bindir}/bowtie-align-s
%{_bindir}/bowtie-align-s-debug
%{_bindir}/bowtie-build
%{_bindir}/bowtie-build-l
%{_bindir}/bowtie-build-l-debug
%{_bindir}/bowtie-build-s
%{_bindir}/bowtie-build-s-debug
%{_bindir}/bowtie-inspect
%{_bindir}/bowtie-inspect-l
%{_bindir}/bowtie-inspect-l-debug
%{_bindir}/bowtie-inspect-s
%{_bindir}/bowtie-inspect-s-debug
%{_datadir}/bowtie/genomes
%{_datadir}/bowtie/indexes
%{_datadir}/bowtie/reads
%{_datadir}/bowtie/scripts

%changelog
%autochangelog
