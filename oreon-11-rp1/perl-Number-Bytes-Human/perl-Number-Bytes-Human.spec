%global source0_hash 5fc79c49b0b40df780479c43696381343e2b6ad1fe52859f60bc65b66ebe6f2c

Name:           perl-Number-Bytes-Human
Version:        0.11
Release:        28%{?dist}
Summary:        Convert byte count to human readable format

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Number-Bytes-Human
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Number-Bytes-Human-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.18

%description
This module is designed to format byte counts to usual readable
format, like '2.0K', '3.1G', '100B'. It was inspired in the -h option of 
Unix utilities like du, df and ls for "human-readable" output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Number-Bytes-Human-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

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
