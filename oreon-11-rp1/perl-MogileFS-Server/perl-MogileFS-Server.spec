%global source0_hash d755bb3a0390537051382406726df96c6bac983de074aa8212dcde1cb3363a30

%global cpan_name MogileFS-Server
Name:       perl-%{cpan_name}
Version:    2.73
Release:    28%{?dist}
Summary:    Server part of the MogileFS distributed file system
# LICENSE:      GPL-1.0-or-later OR Artistic-1.0-Perl
# mogautomount: GPL-1.0-or-later OR Artistic-1.0-Perl
# mogstored:    "Same terms as Perl itself.  Artistic/GPLv2, at your choosing"
# mogilefsd:    "Same terms as Perl itself.  Artistic/GPLv2, at your choosing"
# There are two readings of the "Same terms as Perl itself.  Artistic/GPLv2,
# at your choosing":
#   (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-2.0-only OR Artistic-1.0-Perl)
#   (GPL-1.0-or-later OR Artistic-1.0-Perl) OR (GPL-2.0-only OR Artistic-1.0-Perl)
# Author clarified that he wants "(GPL-1.0-or-later OR Artistic-1.0-Perl)".
# The "GPL-2.0-only" was a mistake.
# MogileFS-Server-license_clarification:        GPL-1.0-or-later OR Artistic-1.0-Perl
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/%{cpan_name}
Source0:    https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/%{cpan_name}-%{version}.tar.gz
Source1:    mogilefsd.service
Source2:    mogstored.service
Source3:    mogilefsd.conf
Source4:    mogstored
Source5:    README.mogilefsd
Source6:    README.mogstored
# License clarification from the author
Source7:    MogileFS-Server-license_clarification
# To be able to split back-ends
Patch0:     %{cpan_name}-2.67-Load-only-selected-Mogstored-HTTPServer-implementati.patch
# Adjust to Apache 2.4
Patch1:     %{cpan_name}-2.67-Apache-2.4-support.patch
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Danga::Socket) >= 1.56
# DBD::mysql not used
# DBD::Pg not used
BuildRequires:  perl(DBD::SQLite) >= 1.13
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
# Fcntl not used at tests
BuildRequires:  perl(fields)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::AIO) >= 1.6
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::HTTP::NB)
BuildRequires:  perl(Net::Netmask)
BuildRequires:  perl(overload)
# Perlbal 1.79 not used at tests
# Perlbal::Socket not used at tests
# Perlbal::TCPListener not used at tests
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syscall) >= 0.22
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
# net-tools for netstat program
# net-tools not used because t/mogstored-shutdown.t is removed
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(MogileFS::Admin)
BuildRequires:  perl(MogileFS::Client)
BuildRequires:  perl-MogileFS-Utils
Provides:       perl-mogilefs-server = %{version}-%{release}
Obsoletes:      perl-mogilefs-server < 2.37

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Danga::Socket|Perlbal)\\)$

%description
Server part of the MogileFS distributed file system.

%package -n mogilefsd
Summary:        MogileFS tracker daemon
Requires:       mogilefsd-storage = %{version}-%{release}
Recommends:     mogilefsd-storage-mysql = %{version}-%{release}
Requires(pre):      glibc-common
%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
Requires(pre):      shadow-utils
%endif
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description -n mogilefsd
This is MogileFS tracker daemon. It supports various storages. After selecting
one, you have to install corresponding storage backend (mogilefsd-storage-*
packages), adjust %{_sysconfdir}/mogilefs/mogilefsd.conf, and configure and
start the storage DBMS before the mogilefsd.service.

%package -n mogilefsd-storage-mysql
Summary:        MySQL storage for MogileFS tracker daemon
Provides:       mogilefsd-storage = %{version}-%{release}

%description -n mogilefsd-storage-mysql
%{summary}.

%package -n mogilefsd-storage-postgres
Summary:        PostgreSQL storage for MogileFS tracker daemon
Provides:       mogilefsd-storage = %{version}-%{release}

%description -n mogilefsd-storage-postgres
%{summary}.

%package -n mogilefsd-storage-sqlite
Summary:        SQLite storage for MogileFS tracker daemon
Provides:       mogilefsd-storage = %{version}-%{release}

%description -n mogilefsd-storage-sqlite
%{summary}.

%package -n mogstored
Summary:        MogileFS storage daemon
Requires:       perl(Mogstored::ChildProcess::DiskUsage)
Requires:       perl(Mogstored::ChildProcess::IOStat)
Requires:       perl(Mogstored::HTTPServer::None)
Requires:       perl(Pod::Usage)
# sysstat for iostat program
Requires:       sysstat
Requires(pre):      glibc-common
%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
Requires(pre):      shadow-utils
%endif
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description -n mogstored
The MogileFS storage daemon mogstored.

%package -n mogstored-backend-apache
Summary:    Apache back-end for mogstored
Requires:   httpd

%description -n mogstored-backend-apache
Apache back-end for mogstored, the MogileFS storage daemon.

%package -n mogstored-backend-lighttpd
Summary:    Lighttpd back-end for mogstored
Requires:   lighttpd

%description -n mogstored-backend-lighttpd
Lighttpd back-end for mogstored, the MogileFS storage daemon.

%package -n mogstored-backend-nginx
Summary:    Nginx back-end for mogstored
Requires:   nginx

%description -n mogstored-backend-nginx
Nginx back-end for mogstored, the MogileFS storage daemon.

%package -n mogstored-backend-none
Summary:    Back-end which allows mogstored to work with unmanaged DAV servers

%description -n mogstored-backend-none
Back-end which allows mogstored to work with unmanaged DAV servers.

%package -n mogstored-backend-perlbal
Summary:    Perlbal back-end for mogstored
Requires:   perl(IO::AIO) >= 1.6
Requires:   perl(Perlbal) >= 1.79

%description -n mogstored-backend-perlbal
Perlbal back-end for mogstored, the MogileFS storage daemon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{cpan_name}-%{version}
cp -p %{SOURCE5} %{SOURCE6} %{SOURCE7} .
# Remove test that interfere with a system service
rm t/mogstored-shutdown.t
perl -i -ne 'print $_ unless m{^t\/mogstored-shutdown\.t}' MANIFEST

# Create sysusers.d config files
cat >mogilefsd.sysusers <<EOF
u mogilefsd - 'MogileFS tracker daemon' - -
EOF
cat >mogstored.sysusers <<EOF
u mogstored - 'MogileFS storage daemon' - -
EOF

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

install -d -m0755 %{buildroot}%{_unitdir}
install -p -m0644 %{SOURCE1} %{SOURCE2} %{buildroot}%{_unitdir}

install -d -m0755 %{buildroot}%{_sysconfdir}/mogilefs
install -p -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/mogilefs

install -d -m0755 %{buildroot}%{_sysconfdir}/sysconfig
install -p -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig

install -d -m0770 %{buildroot}%{_localstatedir}/mogdata

install -m0644 -D mogilefsd.sysusers %{buildroot}%{_sysusersdir}/mogilefsd.conf
install -m0644 -D mogstored.sysusers %{buildroot}%{_sysusersdir}/mogstored.conf

%check
# SQLite back-end fails in mock. MySQL or PostgreSQL in mock is also no-go.
# make test MOGTEST_DBTYPE=SQLite
# Disabling network tests.
make test

%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
%pre -n mogilefsd
getent group mogilefsd >/dev/null || groupadd -r mogilefsd
getent passwd mogilefsd >/dev/null || \
    useradd -r -g mogilefsd -d / -s /sbin/nologin \
        -c "MogileFS tracker daemon" mogilefsd
exit 0
%endif

%post -n mogilefsd
%systemd_post mogilefsd.service

%preun -n mogilefsd
%systemd_preun mogilefsd.service

%postun -n mogilefsd
%systemd_postun_with_restart mogilefsd.service

%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
%pre -n mogstored
getent group mogstored >/dev/null || groupadd -r mogstored
getent passwd mogstored >/dev/null || \
    useradd -r -g mogstored -d / -s /sbin/nologin \
        -c "MogileFS storage daemon" mogstored
exit 0
%endif

%post -n mogstored
%systemd_post mogstored.service

%preun -n mogstored
%systemd_preun mogstored.service

%postun -n mogstored
%systemd_postun_with_restart mogstored.service

%files -n mogilefsd
%license LICENSE MogileFS-Server-license_clarification
%doc CHANGES doc examples
%doc TODO README.mogilefsd
%{_bindir}/mogilefsd
%{_bindir}/mogdbsetup
%{_mandir}/man1/mogilefsd.*
%{_mandir}/man3/MogileFS::*.*
%exclude %{_mandir}/man3/MogileFS::Store::*
%{perl_vendorlib}/MogileFS
%exclude %{perl_vendorlib}/MogileFS/Store/*
%dir %{_sysconfdir}/mogilefs
%config(noreplace) %attr(0640,root,mogilefsd) %{_sysconfdir}/mogilefs/mogilefsd.conf
%{_unitdir}/mogilefsd.service
%{_sysusersdir}/mogilefsd.conf

%files -n mogilefsd-storage-mysql
%{_mandir}/man3/MogileFS::Store::MySQL.*
%{perl_vendorlib}/MogileFS/Store/MySQL.pm

%files -n mogilefsd-storage-postgres
%{_mandir}/man3/MogileFS::Store::Postgres.*
%{perl_vendorlib}/MogileFS/Store/Postgres.pm

%files -n mogilefsd-storage-sqlite
%{_mandir}/man3/MogileFS::Store::SQLite.*
%{perl_vendorlib}/MogileFS/Store/SQLite.pm

%files -n mogstored
%license LICENSE MogileFS-Server-license_clarification
%doc README.mogstored
%{_bindir}/mogstored
%{_bindir}/mogautomount
%{_mandir}/man1/mogstored.*
%{_mandir}/man1/mogautomount.*
%dir %{perl_vendorlib}/Mogstored
%{perl_vendorlib}/Mogstored/ChildProcess*
%{perl_vendorlib}/Mogstored/FIDStatter.pm
%{perl_vendorlib}/Mogstored/HTTPServer.pm
%{perl_vendorlib}/Mogstored/SideChannel*
%{perl_vendorlib}/Mogstored/TaskQueue.pm
%config(noreplace) %{_sysconfdir}/sysconfig/mogstored
%{_unitdir}/mogstored.service
%dir %attr(-,mogstored,mogstored) %{_localstatedir}/mogdata
%{_sysusersdir}/mogstored.conf

%files -n mogstored-backend-apache
%{perl_vendorlib}/Mogstored/HTTPServer/Apache.pm

%files -n mogstored-backend-lighttpd
%{perl_vendorlib}/Mogstored/HTTPServer/Lighttpd.pm

%files -n mogstored-backend-nginx
%{perl_vendorlib}/Mogstored/HTTPServer/Nginx.pm

%files -n mogstored-backend-none
%{perl_vendorlib}/Mogstored/HTTPServer/None.pm

%files -n mogstored-backend-perlbal
%{perl_vendorlib}/Mogstored/HTTPServer/Perlbal.pm

%changelog
%autochangelog
