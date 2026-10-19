%global source0_hash 63e453603da165bc6d1c4ca0b55eda3d2204f040c59304a47782c5aa7886565c
Name:           perl-Net-Statsd
Version:        0.12
Release:        1%{?dist}
Summary:        Sends statistics to the stats daemon over UDP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Statsd
Source0:        https://cpan.metacpan.org/authors/id/C/CO/COSIMO/Net-Statsd-%{version}.tar.gz
Patch0:         Net-Statsd-0.12-Make-benchmark.pl-an-example.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
