%global source0_hash cde14d314304294744d2add923386b3047f430bc7d0a7d2664052a4edbfc2a03

Name:           perl-Perl-Critic-StricterSubs
Version:        0.08
Release:        4%{?dist}
Summary:        Perl::Critic plugin for stricter subroutine checks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-StricterSubs
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Perl-Critic-StricterSubs-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::PathList)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Perl::Critic::Exception::Configuration::Option::Policy::ParameterValue)
BuildRequires:  perl(Perl::Critic::Policy) >= 1.082
BuildRequires:  perl(Perl::Critic::Utils) >= 1.082
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Readonly)
# Tests:
BuildRequires:  perl(Perl::Critic::TestUtils) >= 1.082
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
Requires:       perl(Perl::Critic::Policy) >= 1.082
Requires:       perl(Perl::Critic::Utils) >= 1.082

# Filter under-specified dependencies:
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Perl::Critic::(Policy|TestUtils|Utils)\\)$
# Do not provide private modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((EmptyExports|HasExports|NoExports)\\)

%description
As a dynamic language, Perl doesn't require you to define subroutines until
run-time. Although this is a powerful feature, it can also be a major source
of bugs. The Perl::Critic::Policy modules in this distribution are aimed at
reducing errors caused by invoking subroutines that are not defined.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Perl::Critic::TestUtils) >= 1.082

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-StricterSubs-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Perl
%dir %{perl_vendorlib}/Perl/Critic
%dir %{perl_vendorlib}/Perl/Critic/Policy
%dir %{perl_vendorlib}/Perl/Critic/Policy/Modules
%{perl_vendorlib}/Perl/Critic/Policy/Modules/RequireExplicitInclusion.pm
%dir %{perl_vendorlib}/Perl/Critic/Policy/Subroutines
%{perl_vendorlib}/Perl/Critic/Policy/Subroutines/ProhibitCallsToUndeclaredSubs.pm
%{perl_vendorlib}/Perl/Critic/Policy/Subroutines/ProhibitCallsToUnexportedSubs.pm
%{perl_vendorlib}/Perl/Critic/Policy/Subroutines/ProhibitExportingUndeclaredSubs.pm
%{perl_vendorlib}/Perl/Critic/Policy/Subroutines/ProhibitQualifiedSubDeclarations.pm
%{perl_vendorlib}/Perl/Critic/StricterSubs
%{perl_vendorlib}/Perl/Critic/StricterSubs.pm
%{_mandir}/man3/Perl::Critic::Policy::Modules::RequireExplicitInclusion.*
%{_mandir}/man3/Perl::Critic::Policy::Subroutines::ProhibitCallsToUndeclaredSubs.*
%{_mandir}/man3/Perl::Critic::Policy::Subroutines::ProhibitCallsToUnexportedSubs.*
%{_mandir}/man3/Perl::Critic::Policy::Subroutines::ProhibitExportingUndeclaredSubs.*
%{_mandir}/man3/Perl::Critic::Policy::Subroutines::ProhibitQualifiedSubDeclarations.*
%{_mandir}/man3/Perl::Critic::StricterSubs.*
%{_mandir}/man3/Perl::Critic::StricterSubs::Utils.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
