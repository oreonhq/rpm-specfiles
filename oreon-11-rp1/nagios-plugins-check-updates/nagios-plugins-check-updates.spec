%global source0_hash f89367fe476a0328d57f9ef39078582c0b927c5484a7b3c001903e935f62050f
%define plugin check_updates
%define nagiospluginsdir %{_libdir}/nagios/plugins
%define debug_package %{nil}
Name:          nagios-plugins-check-updates
Version:       2.0.6
Release:        1%{?dist}
Summary:        A Nagios plugin to check if Red Hat or Fedora system is up-to-date
License:       GPL-3.0-or-later
URL:           https://github.com/matteocorti/check_updates
Source0:        https://github.com/matteocorti/check_updates/releases/download/v%{version}/check_updates-%{version}.tar.gz
ExcludeArch: %{ix86}
Requires:      nagios-plugins
Requires:      which
Requires:      perl(Monitoring::Plugin)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Monitoring::Plugin)
BuildRequires:  perl(Monitoring::Plugin::Getopt)
BuildRequires:  perl(Monitoring::Plugin::Threshold)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{plugin}-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor \
    INSTALLSCRIPT=%{nagiospluginsdir} \
    INSTALLVENDORSCRIPT=%{nagiospluginsdir}
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.pod" -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
