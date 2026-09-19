%global source0_hash c86b8095de3fe36dc53edda8b146318420a4425572863f8704e8529fc8ff6492

%global cpan_name DateTime-Format-Duration

Name:           perl-%{cpan_name}
Version:        1.04
Release:        30%{?dist}
Summary:        Format and parse DateTime::Durations
# Old FSF address reported to upstream as CPAN RT #82055
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
# Upstream links images to the Internet, we package them into %%{_docdir}
Patch0:         DateTime-Format-Duration-1.04-Link-images-to-local-documentation.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Params::Validate)
# Tests:
BuildRequires:  perl(DateTime)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(Data::Dumper)

%description
This module formats and parses DateTime::Duration objects as well as other
durations representations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{cpan_name}-%{version}
%patch -P0 -p1
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING docs README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
