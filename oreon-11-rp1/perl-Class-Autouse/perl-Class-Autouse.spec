%global source0_hash 538e9575423a8185d8c9f1b92e71e21e44bb9414deb060adb9467a0bad490898

Name:           perl-Class-Autouse
Version:        2.02
Release:        2%{?dist}
Summary:        Run-time class loading on first method call
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Autouse
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-Autouse-%{version}.tar.gz

# Upstream does its very best to prevent us from running them.
%bcond_with     xt_tests

BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(List::Util) >= 1.18
BuildRequires:  perl(prefork)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.94

# for xt tests
%if %{with xt_tests}
BuildRequires:  perl(blib)
BuildRequires:  perl(Encode)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::CleanNamespaces) >= 0.15
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::Kwalitee) >= 1.21
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::Mojibake)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Portability::Files)
%endif

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

%check
%{__make} test
%if %{with xt_tests}
# Manually invoke xt-tests
AUTOMATED_TESTING=1 PERL_DL_NONLAZY=1 %{__perl} "-MExtUtils::Command::MM" "-e" "test_harness(0, 'inc', 'blib/lib', 'blib/arch')" xt/*/*.t
%endif

%files
%doc Changes CONTRIBUTING
%license LICENSE
%{perl_vendorlib}/Class
%{_mandir}/man3/Class::Autouse*

%changelog
%autochangelog
