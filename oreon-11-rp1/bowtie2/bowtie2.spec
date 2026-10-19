%global source0_hash e38d1833ec235ca27fa57589d32d897c9addf87085b7cb7bc978662954662da2
Name: bowtie2
Version: 2.5.5
Release:        1%{?dist}
Summary:        An ultra fast and memory-efficient read aligner
License: GPL-3.0-or-later AND Zlib
URL: http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
Source0:        https://github.com/BenLangmead/%{name}/archive/v%{version}.tar.gz
%ifnarch x86_64
%endif
ExcludeArch: %{ix86} %{arm} s390x
Provides: bundled(tiny-thread) = 1.1
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libasan
BuildRequires:  libubsan
BuildRequires:  make
BuildRequires:  perl(Clone)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(lib)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  python3
BuildRequires:  simde-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description

Bowtie 2 is an ultra fast and memory-efficient tool for aligning sequencing
reads to long reference sequences. It is particularly good at aligning reads
of about 50 up to 100s or 1,000s of characters, and particularly good at
aligning to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes the
genome with an FM Index to keep its memory footprint small: for the human
genome, its memory footprint is typically around 3.2 GB. Bowtie 2 supports
gapped, local, and paired-end alignment modes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Remove the directory to avoid building bowtie with bundled libraries.
rm -rf third_party

# Invalid double quote characters are used in the code.
# https://github.com/BenLangmead/bowtie2/issues/278
sed -e 's/“/"/g' -e 's/”/"/g' -i processor_support.h

# Fix shebang to use the system interpreters.
sed -i '1s|/usr/bin/env perl|%{_bindir}/perl|' bowtie2
for file in bowtie2-{build,inspect}; do
  sed -i '1s|/usr/bin/env python3|%{__python3}|' "${file}"
done

%build

%set_build_flags
%ifnarch x86_64
export POPCNT_CAPABILITY=0
export NO_TBB=1
%endif
%make_build all
%install
%make_install PREFIX="%{_prefix}"
mkdir -p %{buildroot}%{_mandir}/man1
for cmd in bowtie2 bowtie2-{build,inspect}; do
  help2man -N -s 1 -o "%{buildroot}%{_mandir}/man1/${cmd}.1" \
    --version-string="%{version}" \
    "%{buildroot}%{_bindir}/${cmd}"
done
%oreon_autofiles main

%check

for cmd in bowtie2 bowtie2-{build,inspect}; do
  ./"${cmd}" --version | grep 'version %{version}'
done
sed -i '/my $binary_type/ s/"release", "debug", "sanitized"/"release"/' \
  scripts/test/simple_tests.pl
ASAN_OPTIONS="halt_on_error=1" \
UBSAN_OPTIONS="halt_on_error=1" \
scripts/test/simple_tests.pl \
  --bowtie2=./bowtie2 \
  --bowtie2-build=./bowtie2-build \
  --compressed
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
