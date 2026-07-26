%global source0_hash f3151b35fbe664bfbae6b2996f22666f6908988c2c2cd813a212b5321e571061

Name:           perl-Perl-Critic-Itch
Version:        0.07
Release:        39%{?dist}
Summary:        Collection of Perl::Critic policies to solve some itches
# Automatically converted from old format: GPLv3+ or Artistic 2.0 - review is highly recommended.
License:        GPL-3.0-or-later OR Artistic-2.0
URL:            https://metacpan.org/release/Perl-Critic-Itch
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARCELO/Perl-Critic-Itch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Perl::Critic) >= 1.052
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils) >= 1.052
# Tests only
BuildRequires:  perl(File::Find)
BuildRequires:  perl(lib)
BuildRequires:  perl(Perl::Critic::TestUtils) >= 1.052
BuildRequires:  perl(Perl::Critic::Violation) >= 1.052
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Perl::Critic) >= 1.052
Requires:       perl(Perl::Critic::Utils) >= 1.052

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Perl::Critic::Utils\\)$

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

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
