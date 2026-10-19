%global source0_hash 28f806b5412c7908b56cf1673084b8b44ce1cb54c9417d784d91428e1a04096e
Name:		perl-Test-Perl-Critic
Summary:        Use Perl::Critic in test programs
Version:	1.04
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Perl-Critic
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Perl-Critic-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(MCE::Grep) >= 1.827
Requires:	perl(Perl::Critic) >= 1.105
Requires:	perl(Perl::Critic::Utils) >= 1.105
Requires:	perl(Perl::Critic::Violation) >= 1.105
Requires:	perl(Test::Builder) >= 0.88
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Perl::Critic\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Perl::Critic::Utils\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Perl::Critic::Violation\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::Builder\\)$
Provides:       perl(Test::Perl::Critic)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(MCE::Grep)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Perl::Critic::Violation)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
