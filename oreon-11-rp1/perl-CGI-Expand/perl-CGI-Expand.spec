%global source0_hash 6e82d118e3c4c0c2dafcda5875ede5e8ddbfffe0b7dfaa648e451e039a45a4a9

Name:           perl-CGI-Expand
Version:        2.05
Release:        4%{?dist}
Summary:        Convert flat hash to nested data using TT2's dot convention
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/CGI-Expand
Source0:        https://www.cpan.org/modules/by-module/CGI/CGI-Expand-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

%description
Converts a CGI query into structured data using a dotted name convention
similar to TT2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Expand-%{version}

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
%{perl_vendorlib}/CGI/
%{_mandir}/man3/CGI::Expand.3pm*

%changelog
%autochangelog
