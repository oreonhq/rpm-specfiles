%global source0_hash 5ead923c8283de2fc31f957b8b32387612aafce0789550fa8232056397912aa0
%global upstream_version 0.54_05
Name:           perl-TestML
Version:        %(echo '%{upstream_version}' | tr _ .)
Release:        23%{?dist}
Summary:        Generic software Testing Meta Language
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/testml-lang/testml/
Source0:        https://github.com/testml-lang/testml/archive/pkg-perl5-%{upstream_version}.tar.gz
Source1:        Makefile.PL
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(List::Util)
Requires:       perl(Text::Diff)
Requires:       perl(warnings)
Requires:       perl(XXX)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(TestML::Compiler.*\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((TestML::Compiler.*|TestMLBridge)\\)
# oreon:deps
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Pegex::Base)
BuildRequires:  perl(Pegex::Parser)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-Test-Harness
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  which
# /oreon:deps
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
set -e
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cd src/perl5
unset TESTML_BRIDGE TESTML_DEVEL TESTML_FILEVAR
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
PATH=../../bin:$PATH TESTML_ROOT=../.. TESTML_RUN=perl5-tap make test
%files -f %{oreon_filedir}/main.list
%files -n perl-TestML-tests -f %{oreon_filedir}/perl-TestML-tests.list

%changelog

%autochangelog
