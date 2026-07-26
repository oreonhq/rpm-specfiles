%global source0_hash fc56a2f2455fef9697b9797a7584c5097d6fc686e65f54a3a5f3fed34aea7443

Name:           perl-HTTP-Exception
Version:        0.04007
Release:        22%{?dist}
Summary:        Throw HTTP-Errors as (Exception::Class-) Exceptions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Exception
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMUELLER/HTTP-Exception-%{version}.tar.gz
BuildArch:      noarch

# build requirements
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# run requirements
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exception::Class::Base)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Middleware::HTTPExceptions)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(lib)
# extended test requirements
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
Every HTTP::Exception is a Exception::Class - Class. So the same
mechanisms apply as with Exception::Class-classes. In fact have a look
at Exception::Class' docs for more general information on exceptions and
Exception::Class::Base for information on what methods a caught
exception also has.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Exception-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 make test

%files
%doc Changes README
%{perl_vendorlib}/HTTP*
%{_mandir}/man3/HTTP*

%changelog
%autochangelog
