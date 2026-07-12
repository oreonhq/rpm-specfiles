%global source0_hash 1c48e9b00bc32578b2176e6f79c4a11713d875befa8fbb7f48b7a9c8172fe8bd

Name:           perl-Business-ISMN
Version:        1.205
Release:        %autorelease
Summary:        Perl library for International Standard Music Numbers
License:        Artistic-2.0
URL:            https://metacpan.org/release/Business-ISMN
Source0:        https://cpan.metacpan.org/modules/by-module/Business/Business-ISMN-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More) >= 1.00
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Tie::Cycle) >= 1.21
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Recommends:     perl(GD::Barcode::EAN13)

Provides:       perl(Business::ISMN)
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Business-ISMN-%{version}

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
%doc Changes README.pod
%{perl_vendorlib}/Business*
%{_mandir}/man3/Business::ISMN*

%changelog
%autochangelog
