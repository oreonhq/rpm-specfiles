%global source0_hash ff7d78a42f5410ec019442cf54360d61cb97355deb045f116a76e3a4c8a3a0a7

Name:           perl-Module-Depends
Version:        0.16
Release:        23%{?dist}
Summary:        Identify the dependencies of a distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Depends
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Module-Depends-%{version}.tar.gz
# Restore compatibility with Perl 5.26.0, CPAN RT#119324, CPAN RT#115053
Patch0:         Module-Depends-0.15-Fix-escaping-literal-curly-brackates-in-a-regexp.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Accessor::Chained)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(inc::Module::Install) >= 0.67
# Inline::MakeMaker not used
# Module::Build not used
BuildRequires:  perl(Test::More)
Requires:       perl(warnings)

%description
Module::Depends extracts module dependencies from an unpacked
distribution tree.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Depends-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
