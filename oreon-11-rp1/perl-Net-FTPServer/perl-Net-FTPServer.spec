%global source0_hash 1683d717e75d79cd663308d51cef28e12d2c52496cb6ef50f5709192ac90e0c5

Name:           perl-Net-FTPServer
Version:        1.125
Release:        34%{?dist}
Summary:        Secure, extensible and configurable Perl FTP server
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Net-FTPServer
Source0:        https://cpan.metacpan.org/authors/id/R/RY/RYOCHIN/Net-FTPServer-%{version}.tar.gz
# Increase default data segment size limit, bug #1381649
Patch0:         Net-FTPServer-1.125-Increase-default-memory-limit.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Scalar) >= 1.126
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(vars)
# Optional run-time:
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Authen::PAM)
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Sync)
# Tests:
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  %{_bindir}/uudecode
BuildRequires:  %{_bindir}/compress
# Optional run-time:
Requires:       perl(Archive::Zip)
Requires:       perl(Authen::PAM)
Requires:       perl(BSD::Resource)
Requires:       perl(Digest::MD5)
Requires:       perl(File::Sync)
Requires:       perl(IO::Scalar) >= 1.126

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(IO::Scalar\\)$

%description
Net::FTPServer is a secure, extensible and configurable FTP server
written in Perl.

This package contains the Perl modules. Install the perl-ftpd package for
the server executables.

%package -n perl-ftpd
Summary:        Secure, extensible and configurable Perl FTP server
Requires:       %{name} = %{version}-%{release}

%description -n perl-ftpd
Net::FTPServer is a secure, extensible and configurable FTP server
written in Perl.

This package contains server executables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-FTPServer-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT

# Daemon configuration file
install -m 644 -D etc/ftpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/ftpd.conf

# Want the daemon in sbin rather than bin
[ ! -d $RPM_BUILD_ROOT%{_sbindir} ] \
    && mv -f $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_sbindir}

%check
make test

%files
%doc AUTHORS Changes COPYING README TODO doc/
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::FTPServer.3pm*
%{_mandir}/man3/Net::FTPServer::DBeg1::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::DBeg1::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::DBeg1::IOBlob.3pm*
%{_mandir}/man3/Net::FTPServer::DBeg1::Server.3pm*
%{_mandir}/man3/Net::FTPServer::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::Full::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::Full::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::Full::Server.3pm*
%{_mandir}/man3/Net::FTPServer::Handle.3pm*
%{_mandir}/man3/Net::FTPServer::InMem::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::InMem::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::InMem::Server.3pm*
%{_mandir}/man3/Net::FTPServer::Proxy::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::Proxy::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::Proxy::Server.3pm*
%{_mandir}/man3/Net::FTPServer::RO::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::RO::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::RO::Server.3pm*

%files -n perl-ftpd
%config(noreplace) %{_sysconfdir}/ftpd.conf
%{_sbindir}/dbeg1-ftpd.pl
%{_sbindir}/ftpd.pl
%{_sbindir}/inmem-ftpd.pl
%{_sbindir}/proxy-ftpd.pl
%{_sbindir}/ro-ftpd.pl

%changelog
%autochangelog
