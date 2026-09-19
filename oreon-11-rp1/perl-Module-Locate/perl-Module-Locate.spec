%global source0_hash a1b6bbf9c25e851effbf9654ecf29469d99e975be376946dfde93773d5ae61dc

Name:           perl-Module-Locate
Version:        1.80
Release:        29%{?dist}
Summary:        Locate Perl modules in the same fashion as "require" and "use"
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Locate
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Module-Locate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(overload)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88

%description
Using "locate()", return the path that "require" would find for a given
module or file name (it can also return a file handle if a reference in @INC
has been used).  This means you can test for the existence, or find the
path for, modules without having to evaluate the code they contain.

This module also comes with accompanying utility functions that are used
within the module itself (except for "get_source") and are available for
import.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Locate-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Module/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
