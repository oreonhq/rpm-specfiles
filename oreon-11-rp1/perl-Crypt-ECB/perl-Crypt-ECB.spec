%global source0_hash a8cac070374d2a022d5860bca6cebb146e8351bf676bfbaf49a8edafb6ccad56

Name:           perl-Crypt-ECB
Version:        2.23
Release:        8%{?dist}
Summary:        Encrypt data using ECB Mode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-ECB
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-ECB-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

%description
This module is a Perl-only implementation of the ECB mode. In combination
with a block cipher such as DES, IDEA or Blowfish, you can encrypt and
decrypt messages of arbitrarily long length. Though for security reasons
other modes than ECB such as CBC should be preferred. See textbooks on
cryptography if you want to know why.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-ECB-%{version}
chmod -x eg/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license ARTISTIC GPLv1
%doc CHANGES eg README README.XTEA
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
