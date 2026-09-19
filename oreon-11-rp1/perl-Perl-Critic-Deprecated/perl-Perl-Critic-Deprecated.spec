%global source0_hash 160970c29a72afbe412fa4ce1d14ce662ee271ea6fd1754ee62f00f89f62aac2

Name:           perl-Perl-Critic-Deprecated
Version:        1.119
Release:        34%{?dist}
Summary:        Perl::Critic policies that have been superseded by others
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Deprecated
Source0:        https://cpan.metacpan.org/modules/by-module/Perl/Perl-Critic-Deprecated-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Perl::Critic::Policy) >= 1.094
BuildRequires:  perl(Perl::Critic::Utils) >= 1.094
BuildRequires:  perl(PPI::Node)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Optional run-time:
# Regexp::Parser not used by tests
# Test Suite
BuildRequires:  perl(Perl::Critic::TestUtils) >= 1.094
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(Perl::Critic::Policy) >= 1.094
Requires:       perl(Perl::Critic::Utils) >= 1.094

# Filter underspecified dependecies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Perl::Critic::Policy|Perl::Critic::Utils)\\)$

%description
The included policies are:
  - Write "$my_variable = 42" instead of "$MyVariable = 42".
  - Write "sub my_function{}" instead of "sub MyFunction{}".
  - Put source-control keywords in every file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Deprecated-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Perl/
%{_mandir}/man3/Perl::Critic::Deprecated.3*
%{_mandir}/man3/Perl::Critic::Policy::Miscellanea::RequireRcsKeywords.3*
%{_mandir}/man3/Perl::Critic::Policy::NamingConventions::ProhibitMixedCaseSubs.3*
%{_mandir}/man3/Perl::Critic::Policy::NamingConventions::ProhibitMixedCaseVars.3*
%{_mandir}/man3/Perl::Critic::Utils::PPIRegexp.3*

%changelog
%autochangelog
