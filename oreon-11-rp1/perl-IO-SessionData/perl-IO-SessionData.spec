%global source0_hash 64a4712a3edbb3fd10230db296c29c8c66f066adfbc0c3df6a48258fef392ddd

Name:           perl-IO-SessionData
Version:        1.03
Release:        33%{?dist}
Summary:        IO::SessionData and IO::SessionSet modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-SessionData
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-SessionData-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(warnings)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(Errno)
Requires:       perl(POSIX)

%description
A set of session modules, former parts of the SOAP::Lite distribution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-SessionData-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/IO/

%changelog
%autochangelog
