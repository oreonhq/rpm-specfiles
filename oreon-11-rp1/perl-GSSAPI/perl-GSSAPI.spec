#
# Rebuild option:
#
#   --with testsuite         - run the test suite
#

Name:           perl-GSSAPI
Version:        0.28
Release:        51%{?dist}
Summary:        Perl extension providing access to the GSSAPIv2 library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GSSAPI
Source0:        https://cpan.metacpan.org/authors/id/A/AG/AGROLMS/GSSAPI-%{version}.tar.gz
# Fix a crash in gss_release_oid() when destructing out_mech (rhbz #1994263, CPAN RT#121873)
Patch0:         GSSAPI-0.28-Fix-a-crash-in-gss_release_oid-when-destructing-out_.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  which
# Run-time
%{?_with_testsuite:BuildRequires: perl(Carp)}
%{?_with_testsuite:BuildRequires: perl(constant)}
%{?_with_testsuite:BuildRequires: perl(Exporter)}
%{?_with_testsuite:BuildRequires: perl(overload)}
%{?_with_testsuite:BuildRequires: perl(warnings)}
%{?_with_testsuite:BuildRequires: perl(XSLoader)}
# Tests
%{?_with_testsuite:BuildRequires: perl(ExtUtils::testlib)}
%{?_with_testsuite:BuildRequires: perl(Test::More)}
# Optional tests
%{?_with_testsuite:BuildRequires: perl(Test::Pod) >= 1.00}

%description
This module gives access to the routines of the GSSAPI library, as
described in rfc2743 and rfc2744 and implemented by the Kerberos-1.2
distribution from MIT.

%prep
%setup -q -n GSSAPI-%{version}
%patch -P0 -p1
chmod -c a-x examples/*.pl

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

%check
# fails a couple of tests if network not available
%{?_with_testsuite:make test}

%files
%doc Changes README examples/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/GSSAPI*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.28-51
- Prepare for Oreon 11 (RP1)
