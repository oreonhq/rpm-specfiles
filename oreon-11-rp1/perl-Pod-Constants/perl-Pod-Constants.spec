%global source0_hash efabb3cb5174e738e0223a8bb5ea0d5a2182714bf34199dde6d9264fbfc84fda

Name:           perl-Pod-Constants
Version:        0.19
Release:        29%{?dist}
Summary:        Include constants from POD
License:        Artistic-2.0

URL:            https://metacpan.org/release/Pod-Constants
Source0:        https://cpan.metacpan.org/authors/id/M/MG/MGV/Pod-Constants-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Pod::Constants allows you to extract data from your POD at run-time, meaning
you can do things like declare constants in POD and not have to update two
places at once every time you make a change.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Pod-Constants-%{version}

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
%{_mandir}/man3/Pod::Constants.*

%changelog
%autochangelog
