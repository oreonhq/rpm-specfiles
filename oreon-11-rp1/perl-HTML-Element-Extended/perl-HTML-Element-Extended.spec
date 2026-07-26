%global source0_hash f3ef1af108f27fef15ebec66479f251ce08aa49bd00b0462c9c80c86b4b6b32b

Name:           perl-HTML-Element-Extended
Version:        1.18
Release:        36%{?dist}
Summary:        Various HTML::Element extensions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Element-Extended
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSISK/HTML-Element-Extended-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Element) >= 3.01
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(vars)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTML::Element\\)$

%description
This package contains various extensions for HTML::Element.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Element-Extended-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
