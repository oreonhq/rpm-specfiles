%global source0_hash 75b3b8ec8efe687677b63f0a10eef966e01f60735c56656ce75cbb44caba335a

Name:           perl-Class-Accessor-Lite
Version:        0.08
Release:        33%{?dist}
Summary:        Minimalistic variant of Class::Accessor
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Accessor-Lite
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Class-Accessor-Lite-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

# Remove bundled inc::Module::Install
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)

%description
The module is a variant of Class::Accessor. It is fast and requires
less typing, has no dependencies to other modules, and does not mess
up the @ISA.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Accessor-Lite-%{version}
rm -r inc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
