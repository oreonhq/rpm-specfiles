%global source0_hash cf55bc36259edf0fd6af9ad2bac81b31dc5b56a162c660590ecb969c7c1674b2
Name:           perl-Authen-Simple-Passwd
Version:        0.6
Release:        1%{?dist}
Summary:        Simple Passwd authentication
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Authen-Simple-Passwd
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/Authen-Simple-Passwd-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Authen::Simple)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

TEST_POD=1 ./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
