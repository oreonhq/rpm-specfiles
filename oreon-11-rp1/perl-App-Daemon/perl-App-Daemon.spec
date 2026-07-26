%global source0_hash 474e9b87a6bd9d327affe47a0648f94638c876bb1aa419691be3d81c47a4dbd7

Name:           perl-App-Daemon
Version:        0.22
Release:        33%{?dist}
Summary:        Start an Application as a Daemon
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-Daemon
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHILLI/App-Daemon-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Log::Log4perl) >= 1.0
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Proc::ProcessTable)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Sysadm::Install) >= 0.37
BuildRequires:  perl(Test::More)
Requires:       perl(Log::Log4perl) >= 1.0
Requires:       perl(Proc::ProcessTable)

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Log::Log4perl\\)$

%description
App::Daemon helps running an application as a daemon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-Daemon-%{version}
chmod 644 eg/*
sed -i -e 's!/usr/local!/usr!' eg/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
