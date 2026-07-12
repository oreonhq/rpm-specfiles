%global source0_hash 05c29ec3482e572313a60da2181b0b30c5db7cf01f8ae7616ad67e1b66263296

Name:           perl-Lingua-EN-Inflect
Version:        1.905
Release:        15%{?dist}
Summary:        Convert singular to plural, select "a" or "an"
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-EN-Inflect
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Lingua-EN-Inflect-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)
# Dependencies:
Requires:       perl(Carp)

Provides:       perl(Lingua::EN::Inflect)
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Lingua-EN-Inflect-%{version}
chmod -c -x Changes lib/Lingua/EN/Inflect.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Lingua/
%{_mandir}/man3/*.3*


%changelog
%autochangelog
