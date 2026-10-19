%global source0_hash 691c519a58427ea8b3abb83a2550a49d5ff71d73172c6cd76a1b4b1497e1c8a6
Name:           perl-SNMP-Simple
Version:        0.02
Release:        1%{?dist}
Summary:        Shortcuts for SNMP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SNMP-Simple
Source0:        https://cpan.metacpan.org/authors/id/I/IA/IAN/SNMP-Simple-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(SNMP)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
