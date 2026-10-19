%global source0_hash e9900c7c510b27d96eeb5ab28afc2780ccce19558f24daf649810514a11f41c8
Name:           perl-Log-Dispatch-Configurator-Any
Version:        1.122640
Release:        1%{?dist}
Summary:        Configurator implementation with Config::Any
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Dispatch-Configurator-Any
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLIVER/Log-Dispatch-Configurator-Any-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Config::Any) >= 0.15
Requires:       perl(Log::Dispatch) >= 2.23
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::Config)
BuildRequires:  perl(Log::Dispatch::Configurator)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl-generators
# /oreon:deps
%description
Log::Dispatch::Config is a wrapper for Log::Dispatch and provides a way to
configure Log::Dispatch objects with configuration files. Somewhat like a lite
version of log4j and Log::Log4perl it allows multiple log destinations. The
standard configuration file format for Log::Dispatch::Config is AppConfig.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Dispatch-Configurator-Any-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
