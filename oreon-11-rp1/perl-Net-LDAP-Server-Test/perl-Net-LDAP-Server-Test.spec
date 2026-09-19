%global source0_hash b120717b5f1f6f6b13b31437fdd218ee0fc69eb01218de14d922f929cf8d2d8e

Name:           perl-Net-LDAP-Server-Test
Version:        0.22
Release:        28%{?dist}
Summary:        Test Net::LDAP code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-LDAP-Server-Test
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARMAN/Net-LDAP-Server-Test-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-interpreter >= 0:5.008003
BuildRequires:  perl-generators

BuildRequires:  perl(Carp)
BuildRequires:  perl(Convert::ASN1)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::ASN)
BuildRequires:  perl(Net::LDAP::Constant)
BuildRequires:  perl(Net::LDAP::Control)
BuildRequires:  perl(Net::LDAP::Entry)
BuildRequires:  perl(Net::LDAP::Filter)
BuildRequires:  perl(Net::LDAP::FilterMatch)
BuildRequires:  perl(Net::LDAP::LDIF)
BuildRequires:  perl(Net::LDAP::Server) >= 0.3
BuildRequires:  perl(Net::LDAP::SID)
BuildRequires:  perl(Net::LDAP::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Optional
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

BuildRequires:  %{__make}
BuildRequires:  %{__perl}

%description
Test your Net::LDAP code without having a real LDAP server available.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-LDAP-Server-Test-%{version}

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
