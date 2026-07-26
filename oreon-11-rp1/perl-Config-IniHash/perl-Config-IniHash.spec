%global source0_hash 9406cbb12388132cf2947b0827f2756753e7ad8db7ac29ac5db9182261570b9c

Name:           perl-Config-IniHash
Version:        3.01.01
Release:        39%{?dist}
Summary:        Perl extension for reading and writing INI files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-IniHash
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JENDA/Config-IniHash-%{version}.tar.gz
BuildArch:      noarch

# core
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
# cpan
BuildRequires:  perl(Hash::Case)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Hash::WithDefaults) >= 0.04

# not automagically picked up
Requires:       perl(Hash::Case)
Requires:       perl(Hash::WithDefaults) >= 0.04

%{?perl_default_filter}

%description
This module reads and writes INI files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-IniHash-%{version}

sed -i 's/\r//' README Changes

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
