%global source0_hash 734aff86b6f9cad40e1c4da81f28faf18e0802c76a566d95e5613d4318182fc1

Name:		perl-Data-Validate-IP
Version:	0.31
Release:	9%{?dist}
Summary:	Perl IP address validation routines

License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Data-Validate-IP
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Data-Validate-IP-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(base)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(NetAddr::IP) >= 4
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Socket)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::Taint)
BuildRequires:	perl(warnings)

%description
This module collects IP address validation routines to make input validation,
and untainting easier and more readable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Validate-IP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
