%global source0_hash 168aa744f7ef380c51d8cdd7b9fe0de2b75fc6d25d061f88354108c7de5edabd

# Enable a coverage plugin
%bcond_without perl_Test2_Harness_enables_coverage

Name:           perl-Test2-Harness
%global cpan_version 1.000163
Version:        1.0.163
Release:        1%{?dist}
Summary:        Test2 Harness designed for the Test2 event system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test2-Harness
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Harness-%{cpan_version}.tar.gz
# Help generators to recognize a Perl code
Patch99:        Test2-Harness-1.000114-Adapt-tests-to-shebangs.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# git not used by App::Yath::Plugin::Git at the tests
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Devel::Cover)
# Devel::NYTProf not used at tests
# Email::Stuffer 0.016 not used at tests
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path) >= 2.11
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(goto::file) >= 0.005
# HTTP::Tiny 0.070 not used at tests
# HTTP::Tiny::Multipart not used at tests
BuildRequires:  perl(Importer) >= 0.025
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Handle) >= 1.27
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Linux::Inotify2)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Long::Jump) >= 0.000001
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Term::ANSIColor) >= 4.03
BuildRequires:  perl(Term::Table) >= 0.015
BuildRequires:  perl(Test::Builder::Formatter) >= 1.302170
BuildRequires:  perl(Test2::API) >= 1.302170
BuildRequires:  perl(Test2::Event) >= 1.302170
BuildRequires:  perl(Test2::Formatter) >= 1.302170
BuildRequires:  perl(Test2::Hub)
%if %{with perl_Test2_Harness_enables_coverage}
%define test2_plugin_cover_min_version 0.000025
BuildRequires:  perl(Test2::Plugin::Cover) >= %{test2_plugin_cover_min_version}
%endif
# Test2::Plugin::DBIProfile not used at tests
BuildRequires:  perl(Test2::Plugin::IOEvents) >= 0.001001
BuildRequires:  perl(Test2::Plugin::MemUsage) >= 0.002003
BuildRequires:  perl(Test2::Plugin::UUID) >= 0.002001
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Util) >= 1.302170
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(Test2::Util::Table)
BuildRequires:  perl(Test2::Util::Term) >= 0.000127
BuildRequires:  perl(Test2::Util::Times)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::HiRes)
# Win32::Console::ANSI not used on Linux
BuildRequires:  perl(YAML::Tiny)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(ok)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::Bundle::Extended) >= 0.000127
BuildRequires:  perl(Test2::Require::AuthorTesting)
BuildRequires:  perl(Test2::Tools::AsyncSubtest) >= 0.000127
BuildRequires:  perl(Test2::Tools::GenTemp)
BuildRequires:  perl(Test2::Tools::Spec)
BuildRequires:  perl(Test2::Tools::Subtest) >= 0.000127
BuildRequires:  perl(Test2::Tools::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000127
BuildRequires:  perl(Test::Builder) >= 1.302170
BuildRequires:  perl(Test::More) >= 1.302170
BuildRequires:  perl(utf8)
# Optional tests:
%if %{with perl_Test2_Harness_enables_coverage}
%define test2_require_module_min_version 0.000127
BuildRequires:  perl(Test2::Require::Module) >= %{test2_require_module_min_version}
%endif
# t2/lib/App/Yath/Plugin/SelfTest.pm tries building a C code using a gcc and
# to run a bash script. But SelfTest.pm itself is never executed.
# bash not used
# gcc not used
# App::Yath::Plugin::Git tries "git" command
Suggests:       git-core
Suggests:       perl(Cpanel::JSON::XS)
Requires:       perl(Data::Dumper)
Suggests:       perl(Devel::Cover)
Suggests:       perl(Devel::NYTProf)
Suggests:       perl(Email::Stuffer) >= 0.016
Requires:       perl(Exporter)
Requires:       perl(File::Path) >= 2.11
Suggests:       perl(FindBin)
Requires:       perl(goto::file) >= 0.005
Suggests:       perl(HTTP::Tiny) >= 0.070
Suggests:       perl(HTTP::Tiny::Multipart) >= 0.08
Requires:       perl(Importer) >= 0.025
Requires:       perl(IO::Compress::Bzip2)
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(IO::Uncompress::Bunzip2)
Requires:       perl(IO::Uncompress::Gunzip)
Requires:       perl(IO::Handle) >= 1.27
Suggests:       perl(IO::Pager) >= 1.00
Suggests:       perl(JSON::MaybeXS)
Requires:       perl(JSON::PP)
Suggests:       perl(Linux::Inotify2)
Requires:       perl(Long::Jump) >= 0.000001
Suggests:       perl(Term::ANSIColor) >= 4.03
Requires:       perl(Term::Table) >= 0.015
Requires:       perl(Test2::API) >= 1.302170
Requires:       perl(Test2::Event) >= 1.302170
Requires:       perl(Test2::Formatter) >= 1.302170
Requires:       perl(Test2::Hub)
%if %{with perl_Test2_Harness_enables_coverage}
Suggests:       perl(Test2::Plugin::Cover) >= %{test2_plugin_cover_min_version}
%endif
Suggests:       perl(Test2::Plugin::DBIProfile) >= 0.002002
Requires:       perl(Test2::Plugin::IOEvents) >= 0.001001
Requires:       perl(Test2::Plugin::MemUsage) >= 0.002003
Requires:       perl(Test2::Plugin::UUID) >= 0.002001
Requires:       perl(Test2::Util) >= 1.302170
Requires:       perl(Test2::Util::Term) >= 0.000127
Requires:       perl(Test::Builder::Formatter) >= 1.302170

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::Path|goto::file|Importer|IO::Handle|List::Util|Long::Jump|Term::Table|Test2::API|Test2::Formatter|Test2::Util|Test2::Util::Term|Test2::V0|Test::Builder|Test::More|Test2::Plugin::Cover|Test2::Require::Module)\\)$
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\((Ax|Bar|Baz|Bx|Cx|Foo|main::HBase|main::HBase::Wrapped)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((AAA|Ax|App::Yath::Command::(Broken|Fake|fake)|App::Yath::Plugin::(Options|SelfTest|Test|TestPlugin)|Bar|Baz|Bx|BBB|Broken|CCC|Cx|FAST|Foo|Manager|Plugin|Preload|Preload::[^)]*|Resource|SmokePlugin|TestPreload|TestSimplePreload)\\)

%description
This is a test harness toolkit for Perl Test2 system. It provides a yath tool,
a command-line tool for executing the tests under the Test2 harness.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(FindBin)
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Test::Builder) >= 1.302170
Requires:       perl(Test::More) >= 1.302170
%if %{with perl_Test2_Harness_enables_coverage}
Requires:       perl(Test2::Plugin::Cover) >= %{test2_plugin_cover_min_version}
Requires:       perl(Test2::Require::Module) >= %{test2_require_module_min_version}
%endif
Requires:       perl(Test2::V0) >= 0.000127

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test2-Harness-%{cpan_version}
chmod -x t2/non_perl/test.c
%if !%{with perl_Test2_Harness_enables_coverage}
for T in t/integration/coverage{,2,3,4}.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{\A\Q'"$T"'\E\b' MANIFEST
done
%endif
# Help generators to recognize a Perl code
%patch -P 99 -p 1
for F in test.pl $(find t t2 -name '*.t' -o -name '*.tx') t/unit/App/Yath/Plugin/Git.script; do
    perl -i -MConfig -pe 'print qq{$Config{startperl}\n} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a test.pl t t2 %{buildroot}%{_libexecdir}/%{name}
# Remove tests which enumerate files in ./lib
for F in t/0-load_all.t t/1-pod_name.t; do
    rm %{buildroot}%{_libexecdir}/%{name}/"$F"
done
# Use /usr/bin/yath
ln -s $(realpath --relative-to %{buildroot}%{_libexecdir}/%{name} \
    %{buildroot}%{_bindir}) \
    %{buildroot}%{_libexecdir}/%{name}/scripts
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/integration/test.t writes into CWD,
# <https://github.com/Test-More/Test2-Harness/issues/259>
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset AUTHOR_TESTING AUTOMATED_TESTING DBI_PROFILE FAIL_ALWAYS FAIL_ONCE \
    FAILURE_DO_PASS GIT_BRANCH GIT_COMMAND GIT_LONG_SHA GIT_SHORT_SHA GIT_STATUS \
    HARNESS_IS_VERBOSE NESTED_YATH RESOURCE_TEST \
    T2_HARNESS_IS_VERBOSE T2_HARNESS_JOB_IS_TRY T2_HARNESS_JOB_FILE \
    T2_HARNESS_MY_JOB_CONCURRENCY T2_HARNESS_MY_JOB_COUNT \
    T2_HARNESS_MY_MAX_JOB_CONCURRENCY T2_HARNESS_STAGE \
    T2_HARNESS_JOB_CONCURRENCY TEST2_HARNESS_ACTIVE TEST2_HARNESS_LOG_FORMAT \
    TEST2_HARNESS_NO_WRITE_TEST_INFO \
    YATH_INTERACTIVE YATH_LOG_FILE_FORMAT YATH_SELF_TEST
export AUTOMATED_TESTING=1
T2_HARNESS_JOB_COUNT="$(getconf _NPROCESSORS_ONLN)" ./test.pl
prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r ./t
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING AUTOMATED_TESTING DBI_PROFILE FAIL_ALWAYS FAIL_ONCE \
    FAILURE_DO_PASS GIT_BRANCH GIT_COMMAND GIT_LONG_SHA GIT_SHORT_SHA GIT_STATUS \
    HARNESS_IS_VERBOSE NESTED_YATH RESOURCE_TEST \
    T2_HARNESS_IS_VERBOSE T2_HARNESS_JOB_IS_TRY T2_HARNESS_JOB_FILE \
    T2_HARNESS_MY_JOB_CONCURRENCY T2_HARNESS_MY_JOB_COUNT \
    T2_HARNESS_MY_MAX_JOB_CONCURRENCY T2_HARNESS_STAGE \
    T2_HARNESS_JOB_CONCURRENCY TEST2_HARNESS_ACTIVE TEST2_HARNESS_LOG_FORMAT \
    TEST2_HARNESS_NO_WRITE_TEST_INFO \
    YATH_INTERACTIVE YATH_LOG_FILE_FORMAT YATH_SELF_TEST
export AUTOMATED_TESTING=1
export T2_HARNESS_JOB_COUNT=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; $j=1 unless $j; print "$j"' -- \
    %{?_smp_mflags})
export HARNESS_OPTIONS=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; print "j$j" if $j' -- \
    %{?_smp_mflags})
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/yath
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/Yath
%{perl_vendorlib}/App/Yath.pm
%dir %{perl_vendorlib}/Test2
%{perl_vendorlib}/Test2/Formatter
%{perl_vendorlib}/Test2/Harness
%{perl_vendorlib}/Test2/Harness.pm
%dir %{perl_vendorlib}/Test2/Tools
%{perl_vendorlib}/Test2/Tools/HarnessTester.pm
%{_mandir}/man1/yath.*
%{_mandir}/man3/App::Yath.*
%{_mandir}/man3/App::Yath::*
%{_mandir}/man3/Test2::Formatter*
%{_mandir}/man3/Test2::Harness.*
%{_mandir}/man3/Test2::Harness::*
%{_mandir}/man3/Test2::Tools::HarnessTester.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
