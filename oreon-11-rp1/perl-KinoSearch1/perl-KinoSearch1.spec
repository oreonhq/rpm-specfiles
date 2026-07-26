%global source0_hash 56a4bcfc6656f7609e825dd78881fcf3c6fa696e702c1cb0155cb58c056278bf

Name:           perl-KinoSearch1
Version:        1.01
Release:        52%{?dist}
Summary:        Search engine library
# ApacheLicense2.0.txt is only included because the upstream
# author decided to include it and is only for informative purposes.
# We believe that it doesn't apply, since author didn't use any Lucene
# code (according to mail in LICENSING.mbox).
# ApacheLicense2.0.txt: Apache-2.0
# buildlib/KinoSearch1/Test/TestUtils.pm:   GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/KinoSearch1.pm    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/KinoSearch1/Util/ToolSet.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSING.mbox:       explanation of a presence of ApacheLicense2.0.txt file
# README:               GPL-1.0-or-later OR Artistic-1.0-Perl
# src/ppport.h:         GPL-1.0-or-later OR Artistic-1.0-Perl
## Never used and not in any binary package
# devel/dump_index:                 GPL-1.0-or-later OR Artistic-1.0-Perl
# t/benchmarks/extract_reuters.plx: GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/KinoSearch1
Source0:        https://cpan.metacpan.org/authors/id/C/CR/CREAMYG/KinoSearch1-%{version}.tar.gz
# Make regular expressions compatible with Perl 5.24.0, proposed to an
# upstream, CPAN RT#105144
Patch0:         KinoSearch1-1.01-Do-not-use-C-in-regexps.patch
# Fix missing function declarations, proposed to an upstream, CPAN RT#147184
Patch1:         KinoSearch1-1.01-c99.patch
Source1:        LICENSING.mbox
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Module::Build) >= 0.36
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(constant)
# Data::Dumper not used at tests
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Lingua::Stem::Snowball) >= 0.94
BuildRequires:  perl(Lingua::StopWords) >= 0.02
BuildRequires:  perl(locale)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XSLoader)
# Tests only:
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
# Plucene not used
# Plucene::Analysis::WhitespaceAnalyzer not used
# Plucene::Document not used
# Plucene::Document::Field not used
# Plucene::Index::Writer not used
# POSIX not used
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
Requires:       perl(Data::Dumper)
Requires:       perl(Lingua::Stem::Snowball) >= 0.94
Requires:       perl(Lingua::StopWords) >= 0.02

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Lingua::Stem::Snowball|Lingua::StopWords)\\)$
# Remove private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(KinoSearch1::Test::TestUtils\\)
%global __provides_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(KinoSearch1::Test::TestUtils\\)

%description
KinoSearch1 is a loose port of the Java search engine library Apache
Lucene, written in Perl and C. The archetypal application is website
search, but it can be put to many different uses.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n KinoSearch1-%{version}
install -m 0644 %{SOURCE1} LICENSING.mbox
# Remove unused tests
for F in t/benchmarks/ t/pod-coverage.t; do
    rm -r "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Align shebangs and file modes
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor optimize="%{optimize}"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a buildlib t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/{000-load,pod}.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license ApacheLicense2.0.txt LICENSING.mbox
%doc buildlib Changes README
%{perl_vendorarch}/auto/KinoSearch1
%{perl_vendorarch}/KinoSearch1
%{perl_vendorarch}/KinoSearch1.pm
%{_mandir}/man3/KinoSearch1.*
%{_mandir}/man3/KinoSearch1::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
