%global source0_hash e1d2d89677981166abc5bb6e5ecc6471f001f13eb56d5be9544d8047dc08a592

Name:           perl-Cache
Version:        2.11
Release:        32%{?dist}
Summary:        The Cache interface
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Cache
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Cache-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DB_File) >= 1.72
BuildRequires:  perl(Date::Parse) >= 2.24
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl) >= 1.03
BuildRequires:  perl(fields)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::NFSLock) >= 1.2
BuildRequires:  perl(File::Path) >= 1
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Heap::Elem)
BuildRequires:  perl(Heap::Fibonacci) >= 0.01
BuildRequires:  perl(IO::File) >= 1.08
BuildRequires:  perl(IO::Handle) >= 1.21
BuildRequires:  perl(IO::String) >= 1.02
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Storable) >= 1
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol) >= 1.02
BuildRequires:  perl(Test::More) >= 0.45
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::TrailingSpace)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)

Requires:  perl(IO::Handle) >= 1.21

%{?perl_default_filter}

%description
The Cache modules are designed to assist a developer in persisting data 
for a specified period of time. Often these modules are used in web 
applications to store data locally to save repeated and redundant 
expensive calls to remote machines or databases.

The Cache interface is implemented by derived classes that store cached 
data in different manners (such as as files on a filesystem, or in memory).

%package -n perl-Cache-Tester
Summary:        Test utility for perl Cache implementations
Requires:       %{name} = %{version}-%{release}

%description -n perl-Cache-Tester
This module is used to run tests against an instance of a Cache implementation
to ensure that it operates as required by the Cache specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cache-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes design.dia LICENSE README
%exclude %{perl_vendorlib}/Cache/Tester.pm
%exclude %{_mandir}/man3/Cache::Tester.3*
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files -n perl-Cache-Tester
%{perl_vendorlib}/Cache/Tester.pm
%{_mandir}/man3/Cache::Tester.3*

%changelog
%autochangelog
