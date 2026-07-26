%global source0_hash b199ae6add235d7c2886cba2e97f536636db41b62297caa03136ec7807668250

Name:           perl-Perl-Critic-Lax
Version:        0.014
Release:        9%{?dist}
Summary:        Policies that let you slide on common exceptions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Lax
Source0:        https://cpan.metacpan.org/modules/by-module/Perl/Perl-Critic-Lax-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(parent)
# This is plug-in into Perl::Critic
BuildRequires:  perl(Perl::Critic) >= 1.088
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitLeadingZeros)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(utf8)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Test::More)
# This is plug-in into Perl::Critic
Requires:       perl(Perl::Critic) >= 1.088
Requires:       perl(Perl::Critic::Policy)

%description
The Perl-Critic-Lax distribution includes versions of core Perl::Critic
modules with built-in exceptions. If you really like a Perl::Critic policy,
but find that you often violate it in a specific way that seems pretty darn
reasonable, maybe there's a Lax policy. If there isn't, send one in!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Lax-%{version}

%build
perl Makefile.PL INSTALLDIRS=perl
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_privlib}/Perl/
%{_mandir}/man3/Perl::Critic::Lax.3*
%{_mandir}/man3/Perl::Critic::Policy::Lax::ProhibitComplexMappings::LinesNotStatements.3*
%{_mandir}/man3/Perl::Critic::Policy::Lax::ProhibitEmptyQuotes::ExceptAsFallback.3*
%{_mandir}/man3/Perl::Critic::Policy::Lax::ProhibitLeadingZeros::ExceptChmod.3*
%{_mandir}/man3/Perl::Critic::Policy::Lax::ProhibitStringyEval::ExceptForRequire.3*
%{_mandir}/man3/Perl::Critic::Policy::Lax::RequireConstantOnLeftSideOfEquality::ExceptEq.3*
%{_mandir}/man3/Perl::Critic::Policy::Lax::RequireEndWithTrueConst.3*
%{_mandir}/man3/Perl::Critic::Policy::Lax::RequireExplicitPackage::ExceptForPragmata.3*

%changelog
%autochangelog
