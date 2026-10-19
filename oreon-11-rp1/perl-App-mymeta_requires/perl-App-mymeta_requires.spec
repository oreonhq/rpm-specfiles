%global source0_hash fdedc68b3f86c9538b3dd7d3b02be008e29c95ca1368af0262b88fe0f84dcc83
Name:           perl-App-mymeta_requires
Version:        0.006
Release:        1%{?dist}
Summary:        Extract module requirements from MYMETA files
License:        Apache-2.0 
URL:            https://metacpan.org/release/App-mymeta_requires
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/App-mymeta_requires-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Basename)
Requires:       perl(Pod::Usage)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Getopt::Lucid)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
