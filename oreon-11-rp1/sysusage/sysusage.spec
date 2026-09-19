%global source0_hash 96768244c349f3ff8d011391ed245d81ac3fdeaff4b6fe71b6265189c896e528

%global pkgname sysusage

Name:           sysusage
Version:        5.7
Release:        25%{?dist}
Summary:        System monitoring based on Perl, rrdtool, and sysstat
License:        GPL-3.0-or-later
URL:            https://sysusage.darold.net/
Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{pkgname}-%{version}.tar.gz
Source1:        %{name}-httpd.conf
Source2:        %{name}.cron
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Need them during building to determine the path.
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires:  hostname
BuildRequires:  procps-ng
%else
BuildRequires:  net-tools
BuildRequires:  procps
%endif
BuildRequires:  sysstat
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-rsysusage = %{version}-%{release}
Requires:       crontabs
# For ping plugin (plugin-sample2.pl)
Requires:       perl(Time::HiRes)
Requires:       rrdtool
Requires:       sysstat
BuildArch:      noarch

%description
SysUsage continuously monitor your systems information and generate
periodic graphical reports using rrdtool or JavaScript jqplot library.
All reports are shown through a web interface.

SysUsage grabs all system activities using Sar and system commands allowing
you to keep tracks of your computer or server activity during its life.
It is a great help for performance analysis and resources management. The
threshold notification can alarm you when the system capabilities are
reached by sending SMTP messages or through Nagios reports.

By default it will monitor all you need to know on your server activity, it
is written in Perl and should works on all Unix like platforms. It doesn't
require a Database system like MySQL or PostgreSQL but relies on rrdtool. In
addition you can embedded your own plugins written in any programming language.

Since release 5.0 SysUsage can be run from a centralized place where
collected statistics will be stored and where graphics will be rendered.
Unlike other monitoring tools with lot of administration work, SysUsage is
design to have the least possible things to configure and a high level of admin
system knowledge. Each server can also be self monitored and you just have to
connect your browser to the web interface to know its health level.

SysUsage is design with simplicity in mind. providing all relevant statistics
from the servers within an intuitive web interface and without spending too
much time to configure it, if you know Nagios, you know what I mean. You will
especially like SysUsage for that.

%package        common
Summary:        Common files for %{name}

%description    common
This package provides common files shared between %{name}
and the rsysusage package

%package        httpd
Summary:        Apache configuration for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       httpd

%description    httpd
This package provides the Apache configuration for
applications using an Alias to %{name}.

%package        rsysusage
Summary:        Remote utility for %{name}
Requires:       %{name}-common = %{version}-%{release}
Requires:       sysstat

%description    rsysusage
This package provides the tools needed to run %{name}
on remote servers without needing to install sysusage
and it's dependencies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}

%build
perl Makefile.PL \
    INSTALLDIRS=vendor \
    QUIET=1 \
    BINDIR=%{_bindir} \
    CONFDIR=%{_sysconfdir} \
    PIDDIR=%{_localstatedir}/run \
    BASEDIR=%{_localstatedir}/lib/%{name} \
    PLUGINDIR=%{_datadir}/%{name}/plugins \
    HTMLDIR=%{_localstatedir}/www/%{name} \
    MANDIR=%{_mandir}/man1 \
    DOCDIR=%{_pkgdocdir} \
    DESTDIR='$DESTDIR'

make %{?_smp_mflags}

%install
export DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}

install -pDm644 %{S:1} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -pDm644 %{S:2} \
    %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -pDm644 doc/%{name}.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1

# Remove redundant files.
find %{buildroot} -name perllocal.pod -type f -delete
find %{buildroot} -name .packlist -type f -delete

%files
%doc ChangeLog README TODO
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%{_bindir}/sysusage*
%{_datadir}/%{name}
%{_localstatedir}/www/%{name}
%{_mandir}/man1/%{name}.1*

%files common
%license LICENSE
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%dir %{_localstatedir}/lib/%{name}
%{perl_vendorlib}/SysUsage

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

%files rsysusage
%{_bindir}/rsysusage

%changelog
%autochangelog
