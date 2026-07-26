%global source0_hash 5ead923c8283de2fc31f957b8b32387612aafce0789550fa8232056397912aa0

%global upstream_version 0.54_05
Name:           perl-TestML
Version:        %(echo '%{upstream_version}' | tr _ .)
Release:        23%{?dist}
Summary:        Generic software Testing Meta Language
# src/perl5/pkg/doc/TestML.pod: GPL-1.0-or-later OR Artistic-1.0-Perl
# src/perl5/pkg/dist.ini:       GPL-1.0-or-later OR Artistic-1.0-Perl
## unused and not packaged
# src/testml-compiler-coffee/pkg/package.json:              MIT
# src/testml-compiler-perl5/pkg/doc/TestML/Compiler.pod:    GPL-1.0-or-later OR Artistic-1.0-Perl
# src/python/pkg/setup.py:      MIT
# src/python/pkg/LICENSE:       MIT text
# src/python/pkg/ReadMe.md:     MIT
# src/node/pkg/package.json:    MIT
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/testml-lang/testml/
Source0:        %{url}archive/pkg-perl5-%{upstream_version}.tar.gz
# Upstream build script requires checking out various git trees and
# executing sripts dowloaded from the Internet. Use a trivial Makefile.PL
# instead.
Source1:        Makefile.PL
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
# Carp not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
# Text::Diff not used at tests
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# XXX not used at tests
# Tests:
# bash for bin/getopt.sh
BuildRequires:  bash
# git in bin/getopt.sh not helpful
BuildRequires:  grep
# perl-Test-Harness for /usr/bin/prove
BuildRequires:  perl-Test-Harness
BuildRequires:  perl(constant)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pegex::Base)
BuildRequires:  perl(Pegex::Parser)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  which
Requires:       perl(Carp)
Requires:       perl(List::Util)
Requires:       perl(Text::Diff)
Requires:       perl(warnings)
Requires:       perl(XXX)

# Remove private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(TestML::Compiler.*\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((TestML::Compiler.*|TestMLBridge)\\)

%description
TestML <http://www.testml.org/> is a generic, programming language agnostic,
meta language for writing unit tests. The idea is that you can use the same
test files in multiple implementations of a given programming idea. Then you
can be more certain that your application written in, say, Python matches your
Perl implementation.

In a nutshell you write a bunch of data tests that have inputs and expected
results. Using a simple syntax, you specify what functions the data must pass
through to produce the expected results. You use a bridge class to write the
data functions that pass the data through your application.

In Perl 5, TestML module is the evolution of the Test::Base module. It has
a superset of Test:Base's goals. The data markup syntax is currently exactly
the same as Test::Base.

Currently, TestML is being redesigned. This package contains the new unstable
implementation. The original, production-ready, implementation is available
under TestML1 name in perl-TestML1 package.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       grep
Requires:       perl-Test-Harness
Requires:       perl(warnings)
Requires:       which

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n testml-pkg-perl5-%{upstream_version}
cd src/perl5
cp %{SOURCE1} .
mv pkg/doc/TestML.pod lib/
mv pkg/Changes .

%build
cd src/perl5
perl Makefile.PL VERSION=%{upstream_version} INSTALLDIRS=vendor \
    NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
cd src/perl5
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream/bin
cp -a ../../bin/{getopt.sh,testml,testml-cli.sh,testml-compiler,testml-perl5-tap} %{buildroot}%{_libexecdir}/%{name}/upstream/bin
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream/test
cp -a ../../test/runtime-tml %{buildroot}%{_libexecdir}/%{name}/upstream/test
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream/src/perl5
cp -a test %{buildroot}%{_libexecdir}/%{name}/upstream/src/perl5
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream/src/perl5/bin
cp -a bin/testml-perl5-tap %{buildroot}%{_libexecdir}/%{name}/upstream/src/perl5/bin
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream/src/testml-compiler-perl5
cp -a ../testml-compiler-perl5/{bin,lib} %{buildroot}%{_libexecdir}/%{name}/upstream/src/testml-compiler-perl5
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# bin/testml writes tests compiled with TestML::Compiler into ./.testml.
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"/upstream/src/perl5
unset TESTML_BRIDGE TESTML_DEVEL TESTML_FILEVAR
export PATH=../../bin:$PATH TESTML_ROOT=../.. TESTML_RUN=perl5-tap
prove -I . -j "$(getconf _NPROCESSORS_ONLN)" test/*.tml
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
cd src/perl5
unset TESTML_BRIDGE TESTML_DEVEL TESTML_FILEVAR
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
PATH=../../bin:$PATH TESTML_ROOT=../.. TESTML_RUN=perl5-tap make test

%files
%doc src/perl5/Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
