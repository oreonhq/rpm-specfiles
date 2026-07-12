%global source0_hash 791f4203ba7c0f7d8380bc01bec20215f7c8bc70d7ed03e552eee44541abe94e

Name:           perl-Sub-Exporter-ForMethods
Version:        0.100055
Release:        9%{?dist}
Summary:        Helper routines for using Sub::Exporter to build methods
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sub-Exporter-ForMethods
Source0:        https://cpan.metacpan.org/modules/by-module/Sub/Sub-Exporter-ForMethods-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter) >= 0.978
BuildRequires:  perl(Sub::Util)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies:

Provides:       perl(Sub::Exporter::ForMethods)
%description
This package provides helper routines for using Sub::Exporter to build methods
that won't be removed by namespace::autoclean.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sub-Exporter-ForMethods-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Sub/
%{_mandir}/man3/Sub::Exporter::ForMethods.3*

%changelog
%autochangelog
