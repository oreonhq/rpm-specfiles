%global source0_hash d7b7a1fd7fcce0168d44fb8876918fe8a9af49ae0eb8b09625b67b18d71f5e81

Name:           perl-Test-TempDir-Tiny
Version:        0.018
Release:        21%{?dist}
Summary:        Temporary directories that stick around when tests fail
License:        Apache-2.0
URL:            https://metacpan.org/release/Test-TempDir-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-TempDir-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.2
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.2308
# Tests
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Capture::Tiny) >= 0.12
Requires:       perl(B)

%description
This module works with Test::More to create temporary directories that
stick around if tests fail.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-TempDir-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
