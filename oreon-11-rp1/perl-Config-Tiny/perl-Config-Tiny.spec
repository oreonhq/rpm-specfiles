%global source0_hash b2f7345619b3b8e636dd39ea010731c9dc2bfb8f022bcbd86ae6ad17866e110d
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without perl_Config_Tiny_enables_extra_test
Name:		perl-Config-Tiny
Version:	2.30
Release:        7%{?dist}
Summary:        Perl module for reading and writing .ini style configuration files
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Config-Tiny
Source0:        https://cpan.metacpan.org/modules/by-module/Config/Config-Tiny-%{version}.tgz
BuildArch:	noarch
%if %{with perl_Config_Tiny_enables_extra_test}
%if 0%{!?perl_bootstrap:1}
%endif
%endif
Provides:       perl(Config::Tiny)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(UNIVERSAL::isa)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%if %{with perl_Config_Tiny_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))" AUTOMATED_TESTING=1
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
