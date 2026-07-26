%global source0_hash 01b2db074e4ceffc1a92a7ea1c098291460deabfa2332be584ed895ecdf38065

Name:           perl-Sys-Statistics-Linux
Version:        0.66
Release:        39%{?dist}
Summary:        Front-end module to collect system statistics
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-Statistics-Linux
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLOONIX/Sys-Statistics-Linux-%{version}.tar.gz
# https://bugzilla-attachments.redhat.com/attachment.cgi?id=1937394
Patch0:         linux-5.5-diskstats.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::HiRes)

%{?perl_default_filter}

%description
Sys::Statistics::Linux is a front-end module and gather different linux
system information like processor workload, memory usage, network and disk
statistics and a lot more. Refer the documentation of the distribution
modules to get more information about all possible statistics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sys-Statistics-Linux-%{version}
%patch -P0

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc ChangeLog README
%license LICENCE
%{perl_vendorlib}/Sys*
%{_mandir}/man3/Sys*

%changelog
%autochangelog
