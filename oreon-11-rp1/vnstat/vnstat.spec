%global source0_hash c9fe19312d1ec3ddfbc4672aa951cf9e61ca98dc14cad3d3565f7d9803a6b187

Summary: Console-based network traffic monitor
Name: vnstat
Version: 2.13
Release: 2%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://humdi.net/vnstat/
Source0: http://humdi.net/vnstat/vnstat-%{version}.tar.gz
Patch0: vnstat.service.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: make
BuildRequires: gcc
BuildRequires: gd-devel
BuildRequires: systemd
BuildRequires: sqlite-devel

%description
vnStat is a console-based network traffic monitor that keeps a log of daily
network traffic for the selected interface(s). vnStat isn't a packet sniffer.
The traffic information is analyzed from the /proc file-system, so vnStat can
be used without root permissions. See the web-page for few 'screenshots'.

%package vnstati
Summary: Image output support for vnstat
Recommends: %{name} = %{version}-%{release}

%description vnstati
The purpose of vnstati is to provide image output support for statistics
collected using vnstat. The image file format is limited to png. All basic
outputs of vnStat are supported excluding live traffic features. The image can
be outputted either to a file or to standard output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

# disable maximum bandwidth setting and change pidfile location
sed -i -e "s,/var/run/,/run/vnstat/,g; \
	s,MaxBandwidth 100,MaxBandwidth 0,g;" \
	cfg/vnstat.conf

# Create a sysusers.d config file
cat >vnstat.sysusers.conf <<EOF
u vnstat - 'vnStat user' %{_localstatedir}/lib/%{name} -
EOF

%build
%{configure}
%{__make} %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" all

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_unitdir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_tmpfilesdir}

%{__mkdir_p} %{buildroot}/run/
%{__install} -d -m 0700 %{buildroot}/run/%{name}/

%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__install} -p -m 644 examples/systemd/vnstat.service $RPM_BUILD_ROOT%{_unitdir}/
%{__rm} -rf examples/init.d
%{__rm} -rf examples/systemd
%{__rm} -rf examples/launchd
%{__rm} -rf examples/upstart

%{__cat} >> $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf << END
D /run/vnstat 0700 vnstat vnstat
END

install -m0644 -D vnstat.sysusers.conf %{buildroot}%{_sysusersdir}/vnstat.conf

%post
%systemd_post vnstat.service

%preun
%systemd_preun vnstat.service

%postun
%systemd_postun_with_restart vnstat.service

%files
%license COPYING
%doc CHANGES FAQ README INSTALL examples
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man1/vnstat.1*
%{_mandir}/man5/vnstat.conf.5*
%{_mandir}/man8/vnstatd.8*
%{_bindir}/vnstat
%{_sbindir}/vnstatd
%attr(-,vnstat,vnstat)%dir /run/%{name}/
%attr(-,vnstat,vnstat)%{_localstatedir}/lib/%{name}
%{_sysusersdir}/vnstat.conf

%files vnstati
%license COPYING
%{_mandir}/man1/vnstati.1*
%{_bindir}/vnstati

%changelog
%autochangelog
