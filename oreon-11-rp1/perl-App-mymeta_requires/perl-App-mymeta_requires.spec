%global source0_hash fdedc68b3f86c9538b3dd7d3b02be008e29c95ca1368af0262b88fe0f84dcc83

Name:           perl-App-mymeta_requires
Version:        0.006
Release:        28%{?dist}
Summary:        Extract module requirements from MYMETA files
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0 
URL:            https://metacpan.org/release/App-mymeta_requires
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/App-mymeta_requires-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Lucid)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Pod::Usage)
# Tests:
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.92
Requires:       perl(File::Basename)
Requires:       perl(Pod::Usage)

%description
This tool extracts CPAN module requirements as recorded in a MYMETA.json or
MYMETA.yml file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-mymeta_requires-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
# CONTRIBUTING.mkdn is a dummy text
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
