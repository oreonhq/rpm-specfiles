%global source0_hash 93e36010940464626e5f31b9faedd65e12ed8d1abf16ce052febf23f495aefc8

Name:           perl-AnyEvent-BDB
Version:        1.1
Release:        49%{?dist}
Summary:        Truly asynchronous Berkeley DB access
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyEvent-BDB
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-BDB-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(AnyEvent) >= 3.81
BuildRequires:  perl(base)
BuildRequires:  perl(BDB) >= 1.5
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(AnyEvent) >= 3.81
Requires:       perl(BDB) >= 1.5
Requires:       perl(Exporter)
Requires:       perl(warnings)

# Remove under-speficied dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((AnyEvent|BDB)\\)$

%description
Loading this module will install the necessary magic to seamlessly integrate
BDB into AnyEvent, i.e. you no longer need to concern yourself with calling
BDB::poll_cb or any of that stuff.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyEvent-BDB-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}

%check
make test

%files
%license COPYING
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
