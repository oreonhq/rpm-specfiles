%global source0_hash 6f90a027e1531a0e5406cf1de13c709b5216966df8f73d0bab9ab919209763ee

Name:           perl-XML-Parser-Lite
# Use three digits since 0.719 -> 0.72
%global cpan_version 0.722
Version:        %{cpan_version}
Release:        22%{?dist}
Summary:        Lightweight regexp-based XML parser
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND LicenseRef-REX
URL:            https://metacpan.org/release/XML-Parser-Lite
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/XML-Parser-Lite-%{cpan_version}.tar.gz
BuildArch:      noarch
# SOAP::Lite is not actually needed
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(re)
# Tests only
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)

%description
This Perl module implements an XML parser with an interface similar to
XML::Parser.  Though not all callbacks are supported, you should be able to
use it in the same way you use XML::Parser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Parser-Lite-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
