%global source0_hash 1683d717e75d79cd663308d51cef28e12d2c52496cb6ef50f5709192ac90e0c5
Name:           perl-Net-FTPServer
Version:        1.125
Release:        34%{?dist}
Summary:        Secure, extensible and configurable Perl FTP server
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Net-FTPServer
Source0:        https://cpan.metacpan.org/authors/id/R/RY/RYOCHIN/Net-FTPServer-%{version}.tar.gz
Patch0:         Net-FTPServer-1.125-Increase-default-memory-limit.patch
BuildArch:      noarch
Requires:       perl(Archive::Zip)
Requires:       perl(Authen::PAM)
Requires:       perl(BSD::Resource)
Requires:       perl(Digest::MD5)
Requires:       perl(File::Sync)
Requires:       perl(IO::Scalar) >= 1.126
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(IO::Scalar\\)$
# oreon:deps
BuildRequires:  /usr/bin/compress
BuildRequires:  /usr/bin/uudecode
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Authen::PAM)
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Sync)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
install -m 644 -D etc/ftpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/ftpd.conf
[ ! -d $RPM_BUILD_ROOT%{_sbindir} ] \
    && mv -f $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_sbindir}
%oreon_autofiles perl-ftpd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-ftpd -f %{oreon_filedir}/perl-ftpd.list

%changelog

%autochangelog
