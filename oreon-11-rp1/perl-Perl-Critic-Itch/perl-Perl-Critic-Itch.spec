%global source0_hash f3151b35fbe664bfbae6b2996f22666f6908988c2c2cd813a212b5321e571061
Name:           perl-Perl-Critic-Itch
Version:        0.07
Release:        1%{?dist}
Summary:        Collection of Perl::Critic policies to solve some itches
License:        GPL-3.0-or-later OR Artistic-2.0
URL:            https://metacpan.org/release/Perl-Critic-Itch
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARCELO/Perl-Critic-Itch-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Perl::Critic) >= 1.052
Requires:       perl(Perl::Critic::Utils) >= 1.052
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Perl::Critic::Utils\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Perl::Critic::Violation)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl-generators
# /oreon:deps
%description
Perl::Critic::Itch was created to fulfill some special requests when analyzing
Perl Code. This policies, may not be useful to everyone, and surely not
consensual, but they solve some little itches I had, and it makes me sleep
better at night!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Itch-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
