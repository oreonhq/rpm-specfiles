%global source0_hash 6ae45af565167d3015931ef0f300346c3ba35060f1f512022264b7a0eed1c9dd

Name:           perl-Array-Compare
Version:        4.0.0
Release:        7%{?dist}
Summary:        Perl extension for comparing arrays
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Array-Compare
Source0:        https://cpan.metacpan.org/modules/by-module/Array/Array-Compare-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Feature::Compat::Class)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(warnings)
# Dependencies
# (none)

%description
If you have two arrays and you want to know if they are the same or
different, then Array::Compare will be useful to you.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Array-Compare-%{version}
chmod -c -x lib/Array/Compare.pm

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
%{perl_vendorlib}/Array/
%{_mandir}/man3/Array::Compare.3*

%changelog
%autochangelog
