%global source0_hash 538e9575423a8185d8c9f1b92e71e21e44bb9414deb060adb9467a0bad490898
Name:           perl-Class-Autouse
Version:        2.02
Release:        1%{?dist}
Summary:        Run-time class loading on first method call
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Autouse
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-Autouse-%{version}.tar.gz
%bcond_with     xt_tests
BuildArch:      noarch
%if %{with xt_tests}
%endif
# oreon:deps
BuildRequires:  //bin/perl
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(prefork)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Class::Autouse allows you to specify a class the will only load when a
method of that class is called. For large classes that might not be used
during the running of a program, such as Date::Manip, this can save you
large amounts of memory, and decrease the script load time.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Autouse-%{version}

%build

AUTOMATED_TESTING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%if %{with xt_tests}
AUTOMATED_TESTING=1 PERL_DL_NONLAZY=1 %{__perl} "-MExtUtils::Command::MM" "-e" "test_harness(0, 'inc', 'blib/lib', 'blib/arch')" xt/*/*.t
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
