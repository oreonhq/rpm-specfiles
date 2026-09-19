%global source0_hash 78560b638016ef047fd5937f2d35cca9536fe5b42a03974e173f16671bf5c397

Name:           perl-XML-Generator-PerlData
Version:        0.95
Release:        27%{?dist}
Summary:        Perl extension for generating SAX2 events from nested Perl data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Generator-PerlData
Source0:        https://cpan.metacpan.org/authors/id/K/KH/KHAMPTON/XML-Generator-PerlData-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::SAX::Base) >= 1.02
# Tests
BuildRequires:  perl(Test)
Requires:       perl(XML::SAX::Base) >= 1.02

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::SAX::Base\\)\s*$

%description
XML::Generator::PerlData provides a simple way to generate SAX2 events from
nested Perl data structures, while providing finer-grained control over the
resulting document streams.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Generator-PerlData-%{version}

# README is ISO-8859-1 encoded
iconv -f iso-8859-1 -t utf8 < Changes > Changes.utf8
mv Changes.utf8 Changes

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
