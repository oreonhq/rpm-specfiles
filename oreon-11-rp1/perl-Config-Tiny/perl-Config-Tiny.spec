%global source0_hash b2f7345619b3b8e636dd39ea010731c9dc2bfb8f022bcbd86ae6ad17866e110d

# Run extra tests
%if 0%{?rhel}
%bcond_with perl_Config_Tiny_enables_extra_test
%else
%bcond_without perl_Config_Tiny_enables_extra_test
%endif

Name:		perl-Config-Tiny
Version:	2.30
Release:	7%{?dist}
Summary:	Perl module for reading and writing .ini style configuration files
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Config-Tiny
Source0:	https://cpan.metacpan.org/modules/by-module/Config/Config-Tiny-%{version}.tgz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(strict)
# Test Suite
BuildRequires:	perl(File::Spec) >= 3.30
BuildRequires:	perl(File::Temp) >= 0.22
BuildRequires:	perl(Test::More) >= 1.001002
BuildRequires:	perl(UNIVERSAL::isa)
BuildRequires:	perl(utf8)
%if %{with perl_Config_Tiny_enables_extra_test}
# Extra Tests
BuildRequires:	perl(Test::CPAN::Meta) >= 0.17
# Test::MinimumVersion → Perl::MinimumVersion → Perl::Critic → Config::Tiny
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(Test::MinimumVersion) >= 0.101080
%endif
BuildRequires:	perl(Test::Pod) >= 1.44
%endif
# Dependencies
# (none)

Provides:       perl(Config::Tiny)
%description
Config::Tiny is a Perl module designed for reading and writing .ini
style configuration files. It is designed for simplicity and ease of
use, and thus only supports the most basic operations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Config-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
%if %{with perl_Config_Tiny_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))" AUTOMATED_TESTING=1
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Config/
%{_mandir}/man3/Config::Tiny.3*

%changelog
%autochangelog
