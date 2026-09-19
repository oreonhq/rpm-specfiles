%global source0_hash 65d76c9fa822de2a36793fb542337d313f8b254eb0bd74e04fd5c6f9bc7c9f51

Name:           perl-ElasticSearch-SearchBuilder
Version:        0.19
Release:        35%{?dist}
Summary:        Perlish compact query language for ElasticSearch
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/ElasticSearch-SearchBuilder
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DRTECH/ElasticSearch-SearchBuilder-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
The Query DSL for ElasticSearch (see Query DSL), which is used to write
queries and filters, is simple but verbose, which can make it difficult to
write and understand large queries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ElasticSearch-SearchBuilder-%{version}
chmod 644 lib/ElasticSearch/SearchBuilder.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
