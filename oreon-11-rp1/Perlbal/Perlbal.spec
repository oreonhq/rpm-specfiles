%global source0_hash 179e1d8a8106d7a18cd0718c7c53a066b4b557350c29eb5e08eb2ccecb00f16c
Name:           Perlbal
Version:        1.80
Release:        66%{?dist}
Summary:        Reverse-proxy load balance and web-server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perlbal
Source0:        http://www.laqee.unal.edu.co/CPAN/authors/id/D/DO/DORMANDO/Perlbal-1.80.tar.gz
Source1:        perlbal.service
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
Requires:       perl(File::Temp)
Requires:       perl(IO::Select)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Net::CIDR::Lite)
Requires:       perl(BSD::Resource)
Requires:       perl(IO::AIO) >= 1.6
%if !%{defined perl_bootstrap}
Requires:       perl(Perlbal::XS::HTTPHeaders) >= 0.20
%endif
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Danga::Socket)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(IO::AIO)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Net::Netmask)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Perlbal::XS::HTTPHeaders)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sys::Syscall)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  systemd
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%post

%systemd_post perlbal.service
%preun

%systemd_preun perlbal.service
%postun

%systemd_postun_with_restart perlbal.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
