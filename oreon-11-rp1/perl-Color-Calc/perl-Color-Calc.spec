%global source0_hash 6bd35735ca1208e1628f962c1be9b0bc48762097b09017cfe32ce9d0858c76c1

Name:           perl-Color-Calc
Version:        1.074
Release:        33%{?dist}
Summary:        Simple calculations with RGB colors
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Color-Calc
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/Color-Calc-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(attributes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Graphics::ColorNames)
BuildRequires:  perl(Graphics::ColorNames::HTML)
BuildRequires:  perl(Graphics::ColorNames::WWW)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
Requires:       perl(Graphics::ColorNames::WWW)

%{?perl_default_filter}

%description
The Color::Calc module implements simple calculations with RGB colors. This
can be used to create a full color scheme from a few colors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Color-Calc-%{version}
iconv --from=ISO-8859-1 --to=UTF-8 README > README.utf-8
mv README.utf-8 README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
