%global source0_hash 28f806b5412c7908b56cf1673084b8b44ce1cb54c9417d784d91428e1a04096e

Name:		perl-Test-Perl-Critic
Summary:	Use Perl::Critic in test programs
Version:	1.04
Release:	26%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Perl-Critic
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Perl-Critic-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build) >= 0.40
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(English)
BuildRequires:	perl(Perl::Critic) >= 1.105
BuildRequires:	perl(Perl::Critic::Utils) >= 1.105
BuildRequires:	perl(Perl::Critic::Violation) >= 1.105
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder) >= 0.88
BuildRequires:	perl(warnings)
# Optional Runtime
BuildRequires:	perl(MCE::Grep) >= 1.827
# Test Suite
BuildRequires:	perl(Test::More)
# Runtime
Requires:	perl(MCE::Grep) >= 1.827
Requires:	perl(Perl::Critic) >= 1.105
Requires:	perl(Perl::Critic::Utils) >= 1.105
Requires:	perl(Perl::Critic::Violation) >= 1.105
Requires:	perl(Test::Builder) >= 0.88

# Avoid doc-file dependencies from tests
%{?perl_default_filter}

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Perl::Critic\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Perl::Critic::Utils\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Perl::Critic::Violation\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::Builder\\)$

Provides:       perl(Test::Perl::Critic)
%description
Test::Perl::Critic wraps the Perl::Critic engine in a convenient
subroutine suitable for test programs written using the Test::More
framework. This makes it easy to integrate coding-standards enforcement
into the build process. For ultimate convenience (at the expense of some
flexibility), see the criticism pragma.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Perl-Critic-%{version}

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
%doc Changes README t/ xt/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Perl::Critic.3*

%changelog
%autochangelog
