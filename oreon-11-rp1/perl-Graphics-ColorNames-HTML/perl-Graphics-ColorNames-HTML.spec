%global source0_hash c977d7e5424a3ce3cf28509b93422cb9df2872faaa3225afbe470537a0747bd9

Name:           perl-Graphics-ColorNames-HTML
Version:        3.3.1
Release:        22%{?dist}
Summary:        HTML color names and equivalent RGB values
License:        CC0-1.0
URL:            https://metacpan.org/release/Graphics-ColorNames-HTML/
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/Graphics-ColorNames-HTML-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(integer)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Types::Common::Numeric) >= 1.004
BuildRequires:  perl(Types::Standard)

%description
This module defines color names and their associated RGB values from the
HTML 4.0 Specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Graphics-ColorNames-HTML-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
