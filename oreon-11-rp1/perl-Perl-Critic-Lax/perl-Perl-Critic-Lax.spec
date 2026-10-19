%global source0_hash b199ae6add235d7c2886cba2e97f536636db41b62297caa03136ec7807668250
Name:           perl-Perl-Critic-Lax
Version:        0.014
Release:        9%{?dist}
Summary:        Policies that let you slide on common exceptions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Lax
Source0:        https://cpan.metacpan.org/modules/by-module/Perl/Perl-Critic-Lax-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Perl::Critic) >= 1.088
Requires:       perl(Perl::Critic::Policy)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitLeadingZeros)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
