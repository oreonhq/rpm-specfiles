%global source0_hash 058b7232be08ca3bbb7a2dac6184e6469c19d21248910fe9f3494045573469b8
Name:           perl-RDF-Prefixes
Version:        0.005
Release:        27%{?dist}
Summary:        Simple way to turn URIs into QNames
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/RDF-Prefixes
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/RDF-Prefixes-%{version}.tar.gz
BuildArch:      noarch
Suggests:       perl(Carp)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module generates pretty prefixes, reducing
"http://purl.org/dc/terms" to "dc" rather than something too generic like like
"ns01", and provides a context for keeping track of name spaces already used,
so that when "http://purl.org/dc/elements/1.1/" is encountered, it won't stomp
on the previous definition of "dc".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n RDF-Prefixes-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
