%global source0_hash 38ed7eb7b91aeed153887483e49a9a807a2e8962ab227cc6fdb5ea4dc41df128

Name:           perl-Modern-Perl
Version:        1.20250607
Release:        3%{?dist}
Summary:        Enable all of the features of Modern Perl with one command
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Modern-Perl
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(feature)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(mro)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.98
# Dependencies
# (none)

%description
Modern Perl often relies on the presence of several core and CPAN pragmas
and modules.  Wouldn't it be nice to use them all with a single command?

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Modern-Perl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Modern/
%{perl_vendorlib}/odern/
%{_mandir}/man3/Modern::Perl.3*
%{_mandir}/man3/odern::Perl.3*

%changelog
%autochangelog
