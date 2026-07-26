%global source0_hash 64aa477ebf153710e4cd1251a0fa6f964ac34fcd3d9993e299e28064f9eec589

Name:           perl-PostScript
Version:        0.06
Release:        49%{?dist}
Summary:        PostScript Perl module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PostScript
Source0:        https://cpan.metacpan.org/modules/by-module/PostScript/PostScript-%{version}.tar.gz
Patch0:         perl-PostScript-0.06-example.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Perl package that generates PostScript files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PostScript-%{version}
%patch -P0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

rm -f $RPM_BUILD_ROOT/%{perl_vendorlib}/PostScript/example.pl

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc example.pl example.txt psoutput.ps README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
