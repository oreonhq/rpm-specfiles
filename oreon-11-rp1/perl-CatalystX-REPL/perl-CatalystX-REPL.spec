%global source0_hash 0bdc17a4bc16565ce353366b4ac81475ee8a843144305f44ee59b3ef01fb3af1

Name:           perl-CatalystX-REPL
Version:        0.04
Release:        41%{?dist}
Summary:        Read-eval-print-loop for debugging your Catalyst application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CatalystX-REPL
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/CatalystX-REPL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp::REPL)
BuildRequires:  perl(Catalyst) >= 5.80006
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Expect)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Catalyst) >= 5.80006

%{?perl_default_filter}

%description
Using Carp::REPL with a Catalyst application is hard. That's because of all
the internal exceptions that are being thrown and caught by Catalyst during
application startup. You'd have to manually skip over all of those.

This role works around that by automatically setting up Carp::REPL after
starting your application, if the CATALYST_REPL or MYAPP_REPL environment
variables are set.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CatalystX-REPL-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
RELEASE_TESTING=1 make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
%autochangelog
