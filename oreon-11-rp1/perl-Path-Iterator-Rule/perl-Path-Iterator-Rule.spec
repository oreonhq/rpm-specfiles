%global source0_hash f3b062c68e07c76f68de5bc33877cfe9e078b6351a61ba1650e33e09f51ecb29

Name:           perl-Path-Iterator-Rule
Version:        1.015
Release:        12%{?dist}
Summary:        Iterative, recursive file finder
License:        Apache-2.0

URL:            https://metacpan.org/release/Path-Iterator-Rule
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Path-Iterator-Rule-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(autodie)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Number::Compare)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(re)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Filename)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Glob)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)

%description
This module iterates over files and directories to identify ones matching a
user-defined set of rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Path-Iterator-Rule-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/Path::Iterator::Rule.3pm*
%{_mandir}/man3/PIR.3pm*

%changelog
%autochangelog
