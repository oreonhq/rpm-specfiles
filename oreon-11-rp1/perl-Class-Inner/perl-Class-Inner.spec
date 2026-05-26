Name:           perl-Class-Inner
Version:        0.200001
Release:        43%{?dist}
Summary:        A perlish implementation of Java like inner classes

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Inner
SOurce0:        https://cpan.metacpan.org/authors/id/A/AR/ARUNBEAR/Class-Inner-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 2b14b6a301412aa73fff8fe2e275c755828de2e4c5463ffc73b184c2d33b8cdc
%global source0_file Class-Inner-0.200001.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
Yet another implementation of an anonymous class with per object overrideable
methods, but with the added attraction of sort of working dispatch to the
parent class's method.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Class-Inner-0.200001.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2b14b6a301412aa73fff8fe2e275c755828de2e4c5463ffc73b184c2d33b8cdc" || { echo "oreon: Source0 SHA256 mismatch for Class-Inner-0.200001.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Class-Inner-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test



%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.200001-43
- Prepare for Oreon 11 (RP1)
