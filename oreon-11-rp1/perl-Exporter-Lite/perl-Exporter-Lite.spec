%global source0_hash 79d8b14fd5013922c63e850f15bf51059f2502404535eb6690ef23612c2a198d

Name:           perl-Exporter-Lite
Version:        0.09
Release:        9%{?dist}
Summary:        Lightweight exporting of functions and variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Exporter-Lite
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Exporter-Lite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.006
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)

%description
Exporter::Lite is an alternative to Exporter, intended to provide a
lightweight subset of the most commonly-used functionality. It supports
import(), @EXPORT and @EXPORT_OK and not a whole lot else.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Exporter-Lite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Exporter
%{_mandir}/man3/*.3*

%changelog
%autochangelog
