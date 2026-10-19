%global source0_hash 93e36010940464626e5f31b9faedd65e12ed8d1abf16ce052febf23f495aefc8
Name:           perl-AnyEvent-BDB
Version:        1.1
Release:        49%{?dist}
Summary:        Truly asynchronous Berkeley DB access
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyEvent-BDB
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-BDB-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(AnyEvent) >= 3.81
Requires:       perl(BDB) >= 1.5
Requires:       perl(Exporter)
Requires:       perl(warnings)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((AnyEvent|BDB)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(BDB)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
