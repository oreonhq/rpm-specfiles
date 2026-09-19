%global source0_hash 0e0060eb363635a885706c6a26f5fcaafeae759f7b2acae49dda70e195dd44d6

Name:           perl-Number-Format
Version:        1.76
Release:        8%{?dist}
Summary:        Perl extension for formatting numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Number-Format
Source0:        https://cpan.metacpan.org/modules/by-module/Number/Number-Format-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(POSIX)
# Tests only
BuildRequires:  perl(Test::More)

%description
This module provides an easy means of formatting numbers in a manner
suitable for displaying to the user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Number-Format-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc CHANGES README TODO
%{perl_vendorlib}/Number/
%{_mandir}/man3/Number::Format.3*

%changelog
%autochangelog
