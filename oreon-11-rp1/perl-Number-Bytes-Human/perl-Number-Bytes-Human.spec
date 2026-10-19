%global source0_hash 5fc79c49b0b40df780479c43696381343e2b6ad1fe52859f60bc65b66ebe6f2c
Name:           perl-Number-Bytes-Human
Version:        0.11
Release:        1%{?dist}
Summary:        Convert byte count to human readable format
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Number-Bytes-Human
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Number-Bytes-Human-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
