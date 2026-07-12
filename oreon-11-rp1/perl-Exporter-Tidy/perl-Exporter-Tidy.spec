%global source0_hash 687abf7c008d512fd989c633a061ffa8b0f2e8380503469ecc52b9d9ad4200a6

Name:           perl-Exporter-Tidy
Version:        0.09
Release:        4%{?dist}
Summary:        Another way of exporting symbols
License:        any-OSI-perl-modules
URL:            https://metacpan.org/release/Exporter-Tidy
Source0:        https://cpan.metacpan.org/authors/id/J/JU/JUERD/Exporter-Tidy-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)

Provides:       perl(Exporter::Tidy)
%description
This module serves as an easy, clean alternative to Exporter. Unlike
Exporter, it is not subclassed, but it simply exports a custom import()
into your namespace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Exporter-Tidy-%{version}

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
%{perl_vendorlib}/Exporter*
%{_mandir}/man3/Exporter::Tidy*

%changelog
%autochangelog
