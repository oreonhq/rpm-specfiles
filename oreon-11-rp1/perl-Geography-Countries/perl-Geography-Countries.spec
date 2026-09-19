%global source0_hash 48c42e40e8281ba7c981743a854c48e6def2d51eb0925ea6c96e25c74497f20f

Name:           perl-Geography-Countries
Version:        2009041301
Release:        44%{?dist}
Summary:        2-letter, 3-letter, and numerical codes for countries
License:        MIT
URL:            https://metacpan.org/release/Geography-Countries
Source0:        https://cpan.metacpan.org/modules/by-module/Geography/Geography-Countries-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
# (no additional dependencies)
# Dependencies

%description
This module maps country names, and their 2-letter, 3-letter and numerical 
codes, as defined by the ISO-3166 maintenance agency, and defined by the UNSD.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Geography-Countries-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README TODO
%{perl_vendorlib}/Geography/
%{_mandir}/man3/Geography::Countries.3*

%changelog
%autochangelog
