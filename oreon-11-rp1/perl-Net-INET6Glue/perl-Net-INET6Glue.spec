%global source0_hash 90c36398f9501414cccda8b29f23a7f74f2f2b4f552e12debf16218c735bbb17

Name:           perl-Net-INET6Glue
Version:        0.604
Release:        15%{?dist}
Summary:        Make common modules IPv6 ready by hot-patching
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-INET6Glue
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SULLR/Net-INET6Glue-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::INET6) >= 2.54
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Net::INET6Glue is a collection of modules to make common modules IPv6 ready
by hot-patching them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-INET6Glue-%{version}

%build
PERL_MM_USE_DEFAULT=1 /usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes COPYRIGHT README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
