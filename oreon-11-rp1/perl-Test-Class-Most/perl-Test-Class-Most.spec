%global source0_hash 634cded86bba5dde07ced72ffb8a46705ff93aa844b98e96bde05540234c7dff

Name:           perl-Test-Class-Most
Version:        0.08
Release:        29%{?dist}
Summary:        Test classes the easy way
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Class-Most
Source0:        https://cpan.metacpan.org/authors/id/O/OV/OVID/Test-Class-Most-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Test::Class) >= 0.38
BuildRequires:  perl(Test::Most) >= 0.31
# Test
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Class::Load)
BuildRequires:  perl(Test::More)
Requires:       perl(Test::Class) >= 0.38
Requires:       perl(Test::Most) >= 0.31

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Test::Class\\)\s*$

Provides:       perl(Test::Class::Most)
%description
Using the module helps to reduce boilerplate when writing tests based on
Test::Class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Class-Most-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
