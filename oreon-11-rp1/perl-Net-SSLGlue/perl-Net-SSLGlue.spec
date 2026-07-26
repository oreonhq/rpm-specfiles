%global source0_hash 9011bccaa123de613930c9062aeead7952fdabc4b3b33821b611a09d8e5d5e61

Name:           perl-Net-SSLGlue
Version:        1.058
Release:        28%{?dist}
Summary:        Add/extend SSL support for common perl modules
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Net-SSLGlue
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SULLR/Net-SSLGlue-%{version}.tar.gz

# Remove interactive question
# Only minimal test which doesnt requires Internet connexion
Patch0:         perl-Net-SSLGlue-test.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::Socket::SSL) >= 1.19
# Required to have tests effective
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(LWP::UserAgent) >= 6.06
Requires:       perl(LWP::Protocol::https) >= 6.06
Requires:       perl(Net::FTP)
Requires:       perl(Net::FTP::dataconn)

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(IO::Socket::SSL\\)$
%global __requires_exclude %__requires_exclude|^perl\\(LWP::UserAgent\\)$

%description
Some commonly used perl modules don't have SSL support at all, even if the
protocol would support it. Others have SSL support, but most of them don't
do proper checking of the servers certificate.

The Net::SSLGlue::* modules try to add SSL support or proper certificate to
these modules. Currently is support for the following modules available:

- Net::SMTP - add SSL from beginning or using STARTTLS
- Net::LDAP - add proper certificate checking
- LWP - add proper certificate checking 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-SSLGlue-%{version}
%patch -P0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README Changes examples
%license COPYRIGHT
%{perl_vendorlib}/Net
%{_mandir}/man3/Net*

%changelog
%autochangelog
