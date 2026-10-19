%global source0_hash 8fe65cfc0261ed3c8a4395f0524286f5719669fe305f9b03b16cf3684d62cd70
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_Test_Harness_enables_optional_test
%else
%bcond_with perl_Test_Harness_enables_optional_test
%endif
Name:           perl-Test-Harness
Epoch:          1
Version:        3.52
Release:        1%{?dist}
Summary:        Run Perl standard test scripts with statistics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Harness
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Test-Harness-%{version}.tar.gz
Patch0:        Test-Harness-3.38-Remove-shell-bangs.patch
BuildArch:      noarch
%if %{with perl_Test_Harness_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Suggests:       perl(Term::ANSIColor)
Suggests:       perl(Time::HiRes)
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_datadir}/doc
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_datadir}/doc
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(My.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Dev::Null\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(EmptyParser\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(IO::c55Capture\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(NoFork\\)
Provides:       perl(App::Prove)
Provides:       perl(TAP::Harness)
Provides:       perl(Test::Harness)
Provides:       perl(TAP::Base)
Provides:       perl(TAP::Harness::Env)
Provides:       perl(TAP::Parser::Aggregator)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(TAP::Formatter::HTML)
BuildRequires:  perl(TAP::Harness::Archive)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package allows tests to be run and results automatically aggregated and
output to STDOUT.

Although, for historical reasons, the Test-Harness distribution takes its name
from this module it now exists only to provide TAP::Harness with an interface
that is somewhat backwards compatible with Test::Harness 2.xx. If you're
writing new code consider using TAP::Harness directly instead.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Harness-%{version}
%patch -P0 -p1

# Help generators to recognize Perl scripts
for F in `find t -name *.t -o -name *.pl`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/000-load.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Harness-tests -f %{oreon_filedir}/perl-Test-Harness-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:3.52-5
- Import
