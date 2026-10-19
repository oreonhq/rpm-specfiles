%global source0_hash 14d3b6981ffa10c31b70b1d8c2496aa5986793726baeee391e964faf3d9e714c
Name:          perl-Net-IMAP-Simple-SSL
Version:       1.3
Release:        1%{?dist}
Summary:        Simple IMAP account handling with SSL
License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://metacpan.org/release/Net-IMAP-Simple-SSL
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-IMAP-Simple-SSL-%{version}.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Net::IMAP::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make %{?_smp_mflags} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
