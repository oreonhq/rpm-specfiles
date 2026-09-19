%global source0_hash dd6c4cb4d30bc32114b0787faa2a1e2b4fedd1b91c2ef37965ecba11331bb062

Name:           perl-Net-LDAP-Server
Version:        0.43
Release:        29%{?dist}
Summary:        Net::LDAP::Server Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-LDAP-Server
Source0:        https://cpan.metacpan.org/authors/id/A/AA/AAR/Net-LDAP-Server-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators

BuildRequires:  perl(Convert::ASN1)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::ASN)
BuildRequires:  perl(Net::LDAP::Constant)
BuildRequires:  perl(Net::LDAP::Entry)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(fields)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Net::LDAP::Server provides the protocol handling for an LDAP server. You
can subclass it and implement the methods you need. Then you just
instantiate your subclass and call its C<handle> method to establish a
connection with the client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-LDAP-Server-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changelog README
%doc examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
