%global source0_hash 63e453603da165bc6d1c4ca0b55eda3d2204f040c59304a47782c5aa7886565c

Name:           perl-Net-Statsd
Version:        0.12
Release:        29%{?dist}
Summary:        Sends statistics to the stats daemon over UDP
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Statsd
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Statsd-%{version}.tar.gz
# bin/benchmark.pl is a bad name for installation into path
Patch0:         Net-Statsd-0.12-Make-benchmark.pl-an-example.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::Socket)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)

%description
This module implements a client for a statsd statistics collection server, such
as the one in use at Etsy.com.

You want to use this module to track statistics in your Perl application, such
as how many times a certain event occurs (user logins in a web application, or 
database queries issued), or you want to time and then graph how long certain 
events take, like database queries execution time or time to download a certain
file, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Statsd-%{version}
# leaving README.pod as is results in a non-meaningful manpage as Net::README
mkdir pod
mv README.pod pod
# the following commands prevents benchmark.pl example from installing
%patch -P0 -p1
mkdir examples
mv bin/benchmark.pl examples

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README examples pod
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
