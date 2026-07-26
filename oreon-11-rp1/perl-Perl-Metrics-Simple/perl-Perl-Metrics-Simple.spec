%global source0_hash 0195cddf23a2ee430958acc4d8ed85f196e0d06cb8b9f3d638d91b10d4f10220

# Perform optional tests
%bcond_without perl_Perl_Metrics_Simple_enables_optional_test

Name:           perl-Perl-Metrics-Simple
Version:        1.0.3
Release:        7%{?dist}
Summary:        Count packages, subs, lines, etc. of many files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Metrics-Simple
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATISSE/Perl-Metrics-Simple-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find) >= 1.01
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(PPI) >= 1.113
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Readonly) >= 1.03
BuildRequires:  perl(Statistics::Basic::Mean)
BuildRequires:  perl(Statistics::Basic::Median)
BuildRequires:  perl(Statistics::Basic::StdDev)
# Recommended:
BuildRequires:  perl(Readonly::XS) >= 1.02
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
# Moose not used, t/test_files/Perl/Code/Analyze/Test/Moose.pm is not compiled
BuildRequires:  perl(Test::Compile) >= 1.1.0
BuildRequires:  perl(Test::More)
%if %{with perl_Perl_Metrics_Simple_enables_optional_test}
# Optional tests:
# Perl::Critic::Utils not used
# Test::Perl::Critic not used
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
Recommends:     perl(Readonly::XS) >= 1.02

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::Compile\\)$
# Remove unused dependenices
%global __requires_exclude %{__requires_exclude}|^perl\\(Moose\\)
# Remove private modules
%global __requires_exclude %{__requires_exclude}}|^perl\\(Perl::Metrics::Simple::Test
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Perl::Metrics::Simple::Test

%description
Perl::Metrics::Simple provides just enough methods to run static analysis
of one or many Perl files and obtain a few metrics: packages, subroutines,
lines of code, and an approximation of cyclomatic (McCabe) complexity for
the subroutines and the "main" portion of the code.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Compile) >= 1.1.0

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Metrics-Simple-v%{version}
perl -MConfig -i -pe 's/^#!.*perl/$Config{startperl}/ if $. == 1' bin/countperl
for F in \
%if !%{with perl_Perl_Metrics_Simple_enables_optional_test}
    t/0901_pod.t \
    t/0902_pod_coverage.t \
%endif
    t/perlcritic.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t \
    t/test_files/{no_packages_nor_subs,package_no_subs.pl,subs_no_package.pl} \
    t/more_test_files/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
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
# t/000_compile.t examines ./bin and ./lib. Do no create symlinks. They would
# spoil generated dependencies.
rm %{buildroot}%{_libexecdir}/%{name}/t/000_compile.t
rm %{buildroot}%{_libexecdir}/%{name}/t/0901_pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes EXAMPLES README Todo
%{_bindir}/countperl
%dir %{perl_vendorlib}/Perl
%dir %{perl_vendorlib}/Perl/Metrics
%{perl_vendorlib}/Perl/Metrics/Simple
%{perl_vendorlib}/Perl/Metrics/Simple.pm
%{_mandir}/man3/Perl::Metrics::Simple.*
%{_mandir}/man3/Perl::Metrics::Simple::*
%{_mandir}/man1/countperl.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
