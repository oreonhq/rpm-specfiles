%global source0_hash 6dcd92604d64e96cc6c188194ae16a9d3a46556224f77b6f3d1d1312b68f9a3d

Name:           perl-UUID-Tiny
Version:        1.04
Release:        35%{?dist}
Summary:        Pure Perl UUID Support With Functional Interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UUID-Tiny
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAUGUSTIN/UUID-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::MD5)
# Not used in test - perl(Digest::SHA)
BuildRequires:  perl(Digest::SHA1)
# Not used in test - perl(Digest::SHA::PurePerl)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::HiRes)
# Tests
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
Requires:       perl(Digest::SHA1)

%description
UUID::Tiny is a lightweight, low dependency Pure Perl module for UUID
creation and testing. This module provides the creation of version 1 time
based UUIDs (using random multicast MAC addresses), version 3 MD5 based
UUIDs, version 4 random UUIDs, and version 5 SHA-1 based UUIDs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n UUID-Tiny-%{version}

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
