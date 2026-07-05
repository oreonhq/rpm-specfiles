%global source0_hash ab21fa99130e33a0aff6cdb596f647e5e565d207d634ba2ef06bdbef50424e99

Name:           perl-MIME-Base32
Version:        1.303
Release:        1%{?dist}
Summary:        Base32 encoder / decoder
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-Base32
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MIME-Base32-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Encodes and decodes data in a similar way like MIME::Base64 does.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MIME-Base32-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license ARTISTIC-1.0 GPL-1
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*
