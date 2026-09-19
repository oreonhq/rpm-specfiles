%global source0_hash 706360e57a85cf5c0de1cc6502d0366e876df7b42a2e60192861a273750fa603

Name:           perl-Date-Leapyear
Version:        1.72
Release:        46%{?dist}
Summary:        Is a particular year a leap year?
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-Leapyear
Source0:        https://cpan.metacpan.org/modules/by-module/Date/Date-Leapyear-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
Date::Leapyear exports one function - isleap - which returns 1 or 0 if a
year is leap, or not, respectively.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Date-Leapyear-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
#make test

%files
%doc LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
