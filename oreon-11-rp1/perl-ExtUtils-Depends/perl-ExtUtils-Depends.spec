%global source0_hash 02b9a46450050ce19b325b23e46bb4ec644229d7f2d95044f67a86d8efacdc29

Name:           perl-ExtUtils-Depends
Version:        0.8002
Release:        3%{?dist}
Summary:        Easily build XS extensions that depend on XS extensions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-Depends
Source0:        https://cpan.metacpan.org/modules/by-module/ExtUtils/ExtUtils-Depends-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.44
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Requires:       perl(DynaLoader)
Requires:       perl(File::Spec::Functions)

Provides:       perl(ExtUtils::Depends)
Provides:       perl(ExtUtils::Depends)
%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other Perl extensions. This means
that a Perl extension is treated like a shared library that provides
also a C and an XS interface besides the Perl one.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ExtUtils-Depends-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/ExtUtils/
%{_mandir}/man3/ExtUtils::Depends.3*

%changelog
%autochangelog
