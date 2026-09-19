%global source0_hash e0996c3d1c9b443bc644cf0bc55b92f5df2da8a16796d4fccbae94d2e4c6c0ea

Name:           perl-Test-Type
Version:        1.3.0
Release:        28%{?dist}
Summary:        Functions to validate data types in test files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Type
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUBERTG/Test-Type-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Validate::Type)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
The Test::Type module provides functions that allow you to validate data types
in test files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Type-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes ignore.txt LICENSE README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
