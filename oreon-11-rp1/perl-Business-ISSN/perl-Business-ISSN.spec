%global source0_hash b16b3a1b0e53cd45ed3328906d33ad4d59a13b57abf341424553aecf3e443aac

Name:           perl-Business-ISSN
Version:        1.008
Release:        %autorelease
Summary:        Perl library for International Standard Serial Numbers
License:        Artistic-2.0
URL:            https://metacpan.org/release/Business-ISSN
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Business-ISSN-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Provides:       perl(Business::ISSN)
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Business-ISSN-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
# currently only a placeholder in examples/
%doc Changes README.pod
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
