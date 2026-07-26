%global source0_hash 691c519a58427ea8b3abb83a2550a49d5ff71d73172c6cd76a1b4b1497e1c8a6

Name:           perl-SNMP-Simple
Version:        0.02
Release:        39%{?dist}
Summary:        Shortcuts for SNMP

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SNMP-Simple
Source0:        https://cpan.metacpan.org/authors/id/I/IA/IAN/SNMP-Simple-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(SNMP)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
# Module::Signature is useless
# Socket is useless
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%{?perl_default_filter}

%description
This module provides shortcuts when performing repetitive information-retrieval
tasks with SNMP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SNMP-Simple-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
