%global source0_hash 66181df7aa68e2786faf6895c88b18b95c800a8e4e6fb4c07fd176410a3c73f4

Name:           perl-Hash-MultiValue
Summary:        Store multiple values per key
Version:        0.16
Release:        34%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/Hash-MultiValue-%{version}.tar.gz
URL:            https://metacpan.org/release/Hash-MultiValue
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(threads)
BuildRequires:  perl(UNIVERSAL::ref)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Hash::MultiValue is an object (and a plain hash reference) that may
contain multiple values per key.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-MultiValue-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
