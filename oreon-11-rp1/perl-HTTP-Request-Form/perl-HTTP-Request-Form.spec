%global source0_hash 8d73622d214adf35d15d75233515c8271b88cdd95fbfc651a96eeed31950d6a0

Name:           perl-HTTP-Request-Form
Version:        0.952
Release:        34%{?dist}
Summary:        Construct HTTP::Request objects for form processing
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Request-Form
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBAUER/HTTP-Request-Form-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(URI::URL)

%description
This is an extension of the HTTP::Request suite. It allows easy processing
of forms in a user agent by filling out fields, querying fields, selections
and buttons and pressing buttons. It uses HTML::TreeBuilder generated parse
trees of documents (especially the forms parts extracted with
extract_links) and generates it's own internal representation of forms from
which it then generates the request objects to process the form
application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Request-Form-%{version}

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
%doc Changes README ex
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
