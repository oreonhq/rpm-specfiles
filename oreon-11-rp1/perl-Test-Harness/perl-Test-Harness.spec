%global source0_hash 8fe65cfc0261ed3c8a4395f0524286f5719669fe305f9b03b16cf3684d62cd70

# Run optional tests
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_Test_Harness_enables_optional_test
%else
%bcond_with perl_Test_Harness_enables_optional_test
%endif

Name:           perl-Test-Harness
Epoch:          1
Version:        3.52
Release:        5%{?dist}
Summary:        Run Perl standard test scripts with statistics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Harness
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Test-Harness-%{version}.tar.gz
# Remove hard-coded shell bangs
Patch0:         Test-Harness-3.38-Remove-shell-bangs.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Text::ParseWords)
# Optional run-time:
BuildRequires:  perl(Encode)
# Keep Pod::Usage 1.12 really optional
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Time::HiRes)
# Tests:
BuildRequires:  perl(Data::Dumper)
# Dev::Null bundled for bootstrap
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
# Optional tests:
%if %{with perl_Test_Harness_enables_optional_test}
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(File::Temp)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(TAP::Formatter::HTML) >= 0.10
BuildRequires:  perl(TAP::Harness::Archive)
BuildRequires:  perl(YAML)
%endif
%endif
Suggests:       perl(Term::ANSIColor)
Suggests:       perl(Time::HiRes)

# Filter example dependencies
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_datadir}/doc
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_datadir}/doc

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(My.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Dev::Null\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(EmptyParser\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(IO::c55Capture\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(NoFork\\)

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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/000-load.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes Changes-2.64 examples README
%{perl_vendorlib}/App*
%{perl_vendorlib}/TAP*
%{perl_vendorlib}/Test*
%{_bindir}/prove
%{_mandir}/man1/prove*
%{_mandir}/man3/App::Prove*
%{_mandir}/man3/TAP::Base*
%{_mandir}/man3/TAP::Formatter*
%{_mandir}/man3/TAP::Harness*
%{_mandir}/man3/TAP::Object*
%{_mandir}/man3/TAP::Parser*
%{_mandir}/man3/Test::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:3.52-5
- Import
