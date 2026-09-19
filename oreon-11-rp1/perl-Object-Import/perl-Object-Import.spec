%global source0_hash 2b7e6cf57d58f29be0175df139c7ce6c8a5f6ae420f56551d719ebfbcc6bd533

Name:           perl-Object-Import
Version:        1.006
Release:        5%{?dist}
Summary:        Import methods of an object as functions to a package
License:        GPL-3.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Object-Import/
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/Object-Import-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make perl-interpreter perl-generators coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Math::BigInt) >= 1.59
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(warnings)

%description
This module lets you call methods of a certain object more easily by
exporting them as functions to a package. The exported functions are not
called as methods and do not receive an object argument, but instead the
object is fixed at the time you import them with this module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Object-Import-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README TODO
%license ARTISTIC GPL
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
