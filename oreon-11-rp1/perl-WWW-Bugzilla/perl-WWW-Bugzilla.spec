%global source0_hash 1e07e92b1e3b8f04cc7d5b6051aeedd52a06e67731c28d918c226ff13b73d6d0

#
# Rebuild option:
#
#   --with testsuite         - run the test suite (requires network)
#

Name:           perl-WWW-Bugzilla
Version:        1.5
Release:        41%{?dist}
Summary:        Handles submission/update of bugzilla bugs via WWW::Mechanize

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Bugzilla
Source0:        https://cpan.metacpan.org/authors/id/B/BM/BMC/WWW-Bugzilla-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Class::MethodMaker) >= 1.08
BuildRequires:  perl(WWW::Mechanize) >= 1.22
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(Params::Validate)
Requires:       perl(Class::MethodMaker) >= 1.08

%{?perl_default_filter}

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

%check
%{?_with_testsuite:make test}

%files
%doc Changes README
%license ARTISTIC GPL
%{perl_vendorlib}/WWW/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
