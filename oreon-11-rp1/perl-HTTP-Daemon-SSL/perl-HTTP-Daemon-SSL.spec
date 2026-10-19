%global source0_hash 7eae05422d934c8492dfd3505b774fd6590c99808ce8beb6c57efd261e5dc22e
Name:           perl-HTTP-Daemon-SSL
Version:        1.04
Release:        1%{?dist}
Summary:        Simple http server class with SSL support
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Daemon-SSL
Source0:        https://cpan.metacpan.org/modules/by-module/HTTP/HTTP-Daemon-SSL-%{version}.tar.gz
Patch0:         HTTP-Daemon-SSL-1.04-Adapt-tests-to-IO-Socket-SSL-1.80.patch
Patch1:         HTTP-Daemon-SSL-1.04-Generate-keys-and-certificates-at-test-time.patch
BuildArch:      noarch
Requires:       perl(HTTP::Daemon) >= 1
Requires:       perl(IO::Socket::SSL) >= 0.93
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::Socket::SSL::Utils)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Instances of the HTTP::Daemon::SSL class are HTTP/1.1 servers that listen
on a socket for incoming requests. The HTTP::Daemon::SSL is a sub-class of
IO::Socket::SSL, so you can perform socket operations directly on it too.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Daemon-SSL-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
