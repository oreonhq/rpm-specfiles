%global source0_hash 6a450cc4c6281ed1129f32a1c0741f228967feda2e32a2915ff621c36525fcbe

Name:           perl-Test-Filename
Version:        0.03
Release:        28%{?dist}
Summary:        Portable filename comparison
License:        Apache-2.0

URL:            https://metacpan.org/release/Test-Filename
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-Filename-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(warnings)

%description
This simple module provides some handy functions to convert all those path
separators automatically so filename tests will just DWIM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Test-Filename-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README Todo examples
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/Test::Filename*.*

%changelog
%autochangelog
