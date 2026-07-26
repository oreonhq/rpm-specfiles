%global source0_hash a8c2cd40679097fc3b842576e1b53ec35fd43481a86a50383eeb4e24ebbcd6d6

Name:           perl-Net-LDAP-SID
Version:        0.001
Release:        28%{?dist}
Summary:        Net::LDAP::SID Perl module
License:        Artistic-2.0
URL:            https://metacpan.org/release/Net-LDAP-SID
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARMAN/Net-LDAP-SID-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-interpreter >= 0:5.008003
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

%description
Active Directory Security Identifier manipulation

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-LDAP-SID-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
