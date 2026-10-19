%global source0_hash 1e07e92b1e3b8f04cc7d5b6051aeedd52a06e67731c28d918c226ff13b73d6d0
Name:           perl-WWW-Bugzilla
Version:        1.5
Release:        41%{?dist}
Summary:        Handles submission/update of bugzilla bugs via WWW::Mechanize
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Bugzilla
Source0:        https://cpan.metacpan.org/authors/id/B/BM/BMC/WWW-Bugzilla-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Class::MethodMaker) >= 1.08
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Class::MethodMaker)
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module provides a perl API for adding and updating Bugzilla bugs.
It can be useful in writing custom frontends to a Bugzilla server, and
the frontends do not have to sit on the same server as long as they
can reach it via HTTP.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Bugzilla-%{version}
mkdir lib
cp -r WWW lib

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{?_with_testsuite:make test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
