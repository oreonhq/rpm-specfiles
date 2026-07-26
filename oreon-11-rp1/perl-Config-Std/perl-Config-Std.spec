%global source0_hash b7709ff663bd279d264ab9c2f51e9e9588479a3367a8c4cfc18659c2a11480fe

# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname Config-Std

Summary:        Perl module to load and save configuration files in a standard format
Name:           perl-Config-Std
Version:        0.903
Release:        24%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{pkgname}
Source:         https://cpan.metacpan.org/authors/id/B/BR/BRICKER/%{pkgname}-%{version}.tar.gz
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Std)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests only
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  perl(TAP::Harness)
%else
BuildRequires:  perl(TAP::Harness) >= 3.31
%endif
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildArch:      noarch

%description
A perl module to load and save configuration files in a standard format.
The configuration language is deliberately simple and limited, and the
module works hard to preserve as much information (section order, comments
etc.) as possible when a configuration file is updated.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -delete
%endif
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%if 0%{?rhel} && 0%{?rhel} <= 7
make test HARNESS_OPTIONS=j1
%else
make test
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Config/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
