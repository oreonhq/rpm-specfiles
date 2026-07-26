%global source0_hash 9d57ad8504aa6399ac15ff469892c768649f3f59e6ac97ce2ae248f787d45023

Name:           perl-POE-Component-Logger
Version:        1.10
Release:        41%{?dist}
Summary:        A POE logging class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Logger
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOLMEN/POE-Component-Logger-%{version}.tar.gz
# Added . to default path in test, CPAN RT#116620
Patch0:         POE-Component-Logger-1.10-Fix-default-path-in-tests.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Log::Dispatch::Config) >= 0.10
BuildRequires:  perl(Log::Dispatch::Configurator)
BuildRequires:  perl(Log::Dispatch::Output)
BuildRequires:  perl(POE) >= 0.11
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)

%description
POE::Component::Logger provides a simple logging component that uses
Log::Dispatch::Config to drive it, allowing you to log to multiple places at
once (e.g. to STDERR and Syslog at the same time) and also to flexibly define
your logger's output.

It is very simple to use, because it creates a Logger::log method (yes, this
is namespace corruption, so shoot me). If you don't like this, feel free to
post directly to your logger as follows:

  $kernel->post('logger', 'log', "An error occurred: $!");

All logging is done in the background, so don't expect immediate output -
the output will only occur after control goes back to the kernel so it can
process the next event.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Logger-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} +
chmod -R u+w %{buildroot}/*

%check
make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
