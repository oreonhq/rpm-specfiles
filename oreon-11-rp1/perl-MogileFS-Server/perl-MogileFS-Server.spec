%global source0_hash d755bb3a0390537051382406726df96c6bac983de074aa8212dcde1cb3363a30
%global cpan_name MogileFS-Server
Name:       perl-%{cpan_name}
Version:    2.73
Release:        1%{?dist}
Summary:        Server part of the MogileFS distributed file system
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/%{cpan_name}-%{version}.tar.gz
Source1:    mogilefsd.service
Source2:    mogstored.service
Source3:    mogilefsd.conf
Source4:    mogstored
Source5:    README.mogilefsd
Source6:    README.mogstored
Source7:    MogileFS-Server-license_clarification
Patch0:     %{cpan_name}-2.67-Load-only-selected-Mogstored-HTTPServer-implementati.patch
Patch1:     %{cpan_name}-2.67-Apache-2.4-support.patch
BuildArch:  noarch
Provides:       perl-mogilefs-server = %{version}-%{release}
Obsoletes:      perl-mogilefs-server < 2.37
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Danga::Socket|Perlbal)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Danga::Socket)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::AIO)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MogileFS::Admin)
BuildRequires:  perl(MogileFS::Client)
BuildRequires:  perl(Net::HTTP::NB)
BuildRequires:  perl(Net::Netmask)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syscall)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-MogileFS-Utils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Server part of the MogileFS distributed file system.

%package -n mogilefsd
Summary:        MogileFS tracker daemon
Requires:       mogilefsd-storage = %{version}-%{release}
Recommends:     mogilefsd-storage-mysql = %{version}-%{release}
Requires(pre):      glibc-common
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
Requires:       sysstat
Requires(pre):      glibc-common
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
%oreon_autofiles mogilefsd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mogilefsd-storage-mysql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mogilefsd-storage-postgres usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mogilefsd-storage-sqlite usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mogstored usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mogstored-backend-apache usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mogstored-backend-lighttpd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mogstored-backend-nginx usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mogstored-backend-none usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mogstored-backend-perlbal usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%post -n mogilefsd

%systemd_post mogilefsd.service
%preun -n mogilefsd

%systemd_preun mogilefsd.service
%postun -n mogilefsd

%systemd_postun_with_restart mogilefsd.service
%post -n mogstored

%systemd_post mogstored.service
%preun -n mogstored

%systemd_preun mogstored.service
%postun -n mogstored

%systemd_postun_with_restart mogstored.service
%files -f %{oreon_filedir}/main.list
%files -n mogilefsd -f %{oreon_filedir}/mogilefsd.list
%files -n mogilefsd-storage-mysql -f %{oreon_filedir}/mogilefsd-storage-mysql.list
%files -n mogilefsd-storage-postgres -f %{oreon_filedir}/mogilefsd-storage-postgres.list
%files -n mogilefsd-storage-sqlite -f %{oreon_filedir}/mogilefsd-storage-sqlite.list
%files -n mogstored -f %{oreon_filedir}/mogstored.list
%files -n mogstored-backend-apache -f %{oreon_filedir}/mogstored-backend-apache.list
%files -n mogstored-backend-lighttpd -f %{oreon_filedir}/mogstored-backend-lighttpd.list
%files -n mogstored-backend-nginx -f %{oreon_filedir}/mogstored-backend-nginx.list
%files -n mogstored-backend-none -f %{oreon_filedir}/mogstored-backend-none.list
%files -n mogstored-backend-perlbal -f %{oreon_filedir}/mogstored-backend-perlbal.list

%changelog

%autochangelog
