%global source0_hash 179e1d8a8106d7a18cd0718c7c53a066b4b557350c29eb5e08eb2ccecb00f16c

Name:           Perlbal
Version:        1.80
Release:        66%{?dist}
Summary:        Reverse-proxy load balance and web-server
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perlbal
Source0:        http://www.laqee.unal.edu.co/CPAN/authors/id/D/DO/DORMANDO/Perlbal-1.80.tar.gz
Source1:        perlbal.service
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  systemd
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Danga::Socket) >= 1.59
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(fields)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
# IO::Socket::SSL 0.98 not used at tests
# lib not used at tests
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
# Net::CIDR::Lite not used at tests
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
# Symbol not used at tests
BuildRequires:  perl(Sys::Syscall)
BuildRequires:  perl(Time::HiRes)
# URI not used at tests
# URI::QueryParam not used at tests
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional run-time:
# Cache::Memcached::Async not used at tests
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(IO::AIO) >= 1.6
# IO::Socket::INET6 not used at tests
BuildRequires:  perl(Net::Netmask)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Perlbal::XS::HTTPHeaders) >= 0.20
%endif
BuildRequires:  perl(Sys::Syslog)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.94
# Optional tests:
BuildRequires:  perl(Benchmark)

Requires:       perl(File::Temp)
Requires:       perl(IO::Select)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Net::CIDR::Lite)
# Optional run-time:
Requires:       perl(BSD::Resource)
Requires:       perl(IO::AIO) >= 1.6
%if !%{defined perl_bootstrap}
Requires:       perl(Perlbal::XS::HTTPHeaders) >= 0.20
%endif

Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description
Perlbal is a single-threaded event-based server supporting HTTP load 
balancing, web serving, and a mix of the two. Perlbal can act as either a web 
server or a reverse proxy. 

One of the defining things about Perlbal is that almost everything can be 
configured or reconfigured on the fly without needing to restart the software. 
A basic configuration file containing a management port enables you to easily 
perform operations on a running instance of Perlbal. 

Perlbal can also be extended by means of per-service (and global) plugins that 
can override many parts of request handling and behavior.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

install -D -p -m 0644 conf/webserver.conf %{buildroot}%{_sysconfdir}/perlbal/perlbal.conf
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_unitdir}/perlbal.service
mkdir -p doc/examples
mv conf/* doc/examples

%check
make test

%post
%systemd_post perlbal.service

%preun
%systemd_preun perlbal.service

%postun
%systemd_postun_with_restart perlbal.service

%files
%dir %{_sysconfdir}/perlbal
%config(noreplace) %{_sysconfdir}/perlbal/perlbal.conf
%{_unitdir}/perlbal.service
%doc CHANGES README doc/*
%{perl_vendorlib}/*
%{_bindir}/perlbal
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
