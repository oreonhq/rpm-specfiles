%global source0_hash cf55bc36259edf0fd6af9ad2bac81b31dc5b56a162c660590ecb969c7c1674b2

Name:           perl-Authen-Simple-Passwd
Version:        0.6
Release:        44%{?dist}
Summary:        Simple Passwd authentication
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Authen-Simple-Passwd
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/Authen-Simple-Passwd-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Authen::Simple) >= 0.3
BuildRequires:  perl(Module::Build)

# Required by the tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)

# For improved tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%description
Authenticate against a passwd file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Authen-Simple-Passwd-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 ./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
