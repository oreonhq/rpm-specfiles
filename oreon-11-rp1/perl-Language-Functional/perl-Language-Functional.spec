%global source0_hash ca6f49eacbbebea5d1a10bc62d7141070afdb4b443a3118269e08f252efed777

Name:           perl-Language-Functional
Version:        0.05
Release:        40%{?dist}
Summary:        Module which makes Perl slightly more functional
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Language-Functional
Source0:        https://cpan.metacpan.org/authors/id/L/LB/LBROCARD/Language-Functional-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Tie::Array)

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(InfiniteList\\)

%description
Perl already contains some functional-like functions, such as map and grep.
The purpose of this module is to add other functional-like functions to
Perl, such as foldl and foldr, as well as the use of infinite lists.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Language-Functional-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
