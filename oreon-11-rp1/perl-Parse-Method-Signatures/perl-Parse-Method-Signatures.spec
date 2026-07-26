%global source0_hash 0e1977df8ddf034d558b2f8527f09b1b395c8fdf7bbc2ef946bde00c40ae947d

Name:           perl-Parse-Method-Signatures
Version:        1.003019
Release:        26%{?dist}
Summary:        Perl6 like method signature parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parse-Method-Signatures
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Parse-Method-Signatures-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::AutoInstall)
BuildRequires:  perl(Module::Install) >= 0.91
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load) >= 0.19
BuildRequires:  perl(List::MoreUtils) >= 0.20
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Traits) >= 0.06
BuildRequires:  perl(MooseX::Types) >= 0.17
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Structured)
BuildRequires:  perl(MooseX::Types::Util)
BuildRequires:  perl(namespace::clean) >= 0.10
BuildRequires:  perl(PPI) >= 1.203
BuildRequires:  perl(PPI::Statement::Expression)
BuildRequires:  perl(PPI::Token::Word)
# Tests:
BuildRequires:  perl(aliased)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)
Requires:       perl(Class::Load) >= 0.19
Requires:       perl(List::MoreUtils) >= 0.20
Requires:       perl(MooseX::Traits) >= 0.06
Requires:       perl(MooseX::Types) >= 0.17
Requires:       perl(namespace::clean) >= 0.10
Requires:       perl(PPI) >= 1.203

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Load|List::MoreUtils|MooseX::Types|namespace::clean|PPI)\\)$

%description
Inspired by Perl6::Signature but streamlined to just support the subset
deemed useful for TryCatch and MooseX::Method::Signatures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parse-Method-Signatures-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
