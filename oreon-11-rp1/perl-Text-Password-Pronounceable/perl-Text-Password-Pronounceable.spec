%global source0_hash c186a50256e0bedfafb17e7ce157e7c52f19503bb79e18ebf06255911f6ead1a

Name:       perl-Text-Password-Pronounceable 
Version:    0.30
Release:    40%{?dist}
License:    Artistic-1.0-Perl 
Summary:    Generate pronounceable passwords 
Source0:    https://cpan.metacpan.org/authors/id/T/TS/TSIBLEY/Text-Password-Pronounceable-%{version}.tar.gz
Url:        https://metacpan.org/release/Text-Password-Pronounceable
BuildArch:  noarch
BuildRequires: coreutils
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(inc::Module::Install)
BuildRequires: perl(Module::Install::Metadata)
BuildRequires: perl(Module::Install::WriteAll)
BuildRequires: sed
# Run-time:
BuildRequires: perl(Carp)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Tests:
BuildRequires: perl(Test::More)
# Optional tests:
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::Pod::Coverage) >= 1.00

%description
This module generates pronounceable passwords, based on the English
digraphs by D. Edwards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Password-Pronounceable-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
