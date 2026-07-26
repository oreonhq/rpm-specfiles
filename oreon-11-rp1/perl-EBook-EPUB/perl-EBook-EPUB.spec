%global source0_hash 0d718e238d8d3023975665bec92d824c5419f631c7d552c990a33ebb2186bf64

Name:           perl-EBook-EPUB
Version:        0.6
Release:        40%{?dist}
Summary:        Perl module for generating EPUB documents
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/EBook-EPUB
Source0:        https://cpan.metacpan.org/authors/id/O/OT/OTY/EBook-EPUB-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::Writer)
BuildRequires:  perl(version)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
This module permits creating EPUB documents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n EBook-EPUB-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
