%global source0_hash 14d3b6981ffa10c31b70b1d8c2496aa5986793726baeee391e964faf3d9e714c

Name:          perl-Net-IMAP-Simple-SSL
Version:       1.3
Release:       44%{?dist}
Summary:       Simple IMAP account handling with SSL
License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://metacpan.org/release/Net-IMAP-Simple-SSL
Source0:       https://cpan.metacpan.org/modules/by-module/Net/Net-IMAP-Simple-SSL-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires: perl(base)
BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(Net::IMAP::Simple)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
# Tests
BuildRequires: perl(Test::More)

%description
Perl extension for simple IMAP account handling, mostly compatible
with Net::POP3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-IMAP-Simple-SSL-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make %{?_smp_mflags} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT

%check
make %{?_smp_mflags} test

%files
%doc README Changes
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/IMAP/
%dir %{perl_vendorlib}/Net/IMAP/Simple/
%{perl_vendorlib}/Net/IMAP/Simple/SSL.pm
%{_mandir}/man3/Net::IMAP::Simple::SSL.3*

%changelog
%autochangelog
