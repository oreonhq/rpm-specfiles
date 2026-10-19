%global source0_hash 4bba86a1021122d727a746cd98d8e8123b29a14029330cc68c989df095e55b37
Name:           perl-Paper-Specs
Version:        0.10
Release:        38%{?dist}
Summary:        Size and layout information for paper stock, forms, and labels
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Paper-Specs
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONALLEN/Paper-Specs-%{version}.tar.gz
Patch0:         %{name}-0.10-fix_Avery_5393.patch
BuildArch:      noarch
Provides:       perl(Paper::Specs)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl-generators
# /oreon:deps
%description
This package provides features such as:
- Layout PDF and PostScript documents
- Obtain page size information
- Support page sizes you didn't know about

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Paper-Specs-%{version}
%patch -P0 -p1 

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
