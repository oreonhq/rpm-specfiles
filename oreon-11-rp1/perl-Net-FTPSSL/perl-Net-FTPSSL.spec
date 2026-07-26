%global source0_hash 9e95d192ea12a2a3d4b9279287b1c600914d952d56bd1dc513752306a4a0807a

Name:           perl-Net-FTPSSL
Version:        0.42
Release:        20%{?dist}
Summary:        Perl module for FTP over SSL/TLS
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Net-FTPSSL
Source0:        https://cpan.metacpan.org/authors/id/C/CL/CLEACH/Net-FTPSSL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Socket::INET)
# According to Changes, v0.97 causes unspecified hang,
# but v1.08 is well tested. In el5 we have v1.01, dropping
# the v1.08 requirement that META.yml has.
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Net::SSLeay::Handle)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Net::FTPSSL is a class implementing a simple FTP client over a Secure
Sockets Layer (SSL) or Transport Layer Security (TLS) connection written in
Perl as described in RFC959 and RFC2228. It will use TLS by default.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-FTPSSL-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# "You can also perform a deeper test.
# Some information will be required for this test:
# A secure ftp server address, a user, a password and a directory
# where the user has permissions to read and write."
echo n |%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Net*
%{_mandir}/man3/Net*

%changelog
%autochangelog
