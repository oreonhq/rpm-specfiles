%global source0_hash b912d426e9aeba5491a5e502e7c5c039c5daa575428ac9bdc82afff39ec6f07a

Name:           perl-PHP-Serialization
Version:        0.34
Release:        43%{?dist}
Summary:        Converts between PHP's serialize() output and the equivalent Perl structure
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PHP-Serialization
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/PHP-Serialization-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::More)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)

Provides:       perl(PHP::Serialization)
Provides:       perl(PHP::Serialization)
%description
Provides a simple, quick means of serializing perl memory structures
(including object data!) into a format that PHP can deserialize() and
access, and vice versa.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n PHP-Serialization-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
