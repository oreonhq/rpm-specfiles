%global source0_hash ceac1bb5543e23dab2519513c626e3ffe65a177b8e1ed9e56a030d4551d45190

Name:           perl-Data-Page-Pageset
Version:        1.02
Release:        30%{?dist}
Summary:        Change long page list to be shorter and well navigate
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Page-Pageset
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHUNZI/Data-Page-Pageset-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Page) >= 2
BuildRequires:  perl(POSIX)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Exception)

# rpm misses this
Requires:       perl(Data::Page) >= 2

%description
Pages number can be very high, and it is not comfortable to show user from
the first page to the last page list. Sometimes we need split the page list
into some sets to shorten the page list.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Page-Pageset-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
