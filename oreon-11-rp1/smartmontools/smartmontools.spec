%global source0_hash 690b83ca331378da9ea0d9d61008c4b22dde391387b9bbad7f29387f2595f76e
%global with_selinux 1
%global selinuxtype targeted
%global moduletype contrib
%global modulename smartmon
Summary:        Tools for monitoring SMART capable hard disks
Name:		smartmontools
Version:	7.5
Release:        1%{?dist}
Epoch:		1
License:	GPL-2.0-or-later
URL:		https://www.smartmontools.org/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source2:	smartmontools.sysconf
Source4:	smartdnotify
%global		UrlSource5	https://sourceforge.net/p/smartmontools/code/HEAD/tree/trunk/smartmontools/drivedb.h?format=raw
Source5:	drivedb.h
Source6:	%{modulename}.te
Source7:	%{modulename}.if
Source8:	%{modulename}.fc
Source9:	smartmontools.tmpfilesd
Patch1:		smartmontools-5.38-defaultconf.patch
%if 0%{?with_selinux}
Requires:	(%{name}-selinux if selinux-policy-%{selinuxtype})
%endif
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/smartctl
%endif
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  groff
BuildRequires:  libcap-ng-devel
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  readline-devel
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  util-linux
# /oreon:deps
%description
The smartmontools package contains two utility programs (smartctl
and smartd) to control and monitor storage systems using the Self-
Monitoring, Analysis and Reporting Technology System (SMART) built
into most modern ATA and SCSI hard disks. In many cases, these
utilities will provide advanced warning of disk degradation and
failure.

%if 0%{?with_selinux}
%package selinux
Summary:	SELinux policies for smartmontools
BuildArch:	noarch
Requires:	selinux-policy-%{selinuxtype}
Requires(post):	selinux-policy-%{selinuxtype}
BuildRequires:	selinux-policy-devel
%{?selinux_requires}
%description selinux
Custom SELinux policy module for smartmontools
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q 
%patch -P1 -p1 -b .defaultconf
cp %{SOURCE5} .
%if 0%{?with_selinux}
mkdir selinux
cp -p %{SOURCE6} %{SOURCE7} %{SOURCE8} selinux/
%endif

%build

autoreconf -i
%configure --with-selinux --with-libcap-ng=yes --with-libsystemd --with-systemdsystemunitdir=%{_unitdir} --sysconfdir=%{_sysconfdir}/%{name}/ --with-systemdenvfile=%{_sysconfdir}/sysconfig/%{name}
%make_build update-smart-drivedb
./update-smart-drivedb -s - -u sf drivedb.h ||:
cp drivedb.h %{SOURCE5} ||:
%make_build CXXFLAGS="$RPM_OPT_FLAGS -fpie" LDFLAGS="-pie -Wl,-z,relro,-z,now"
%if 0%{?with_selinux}
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif
%install
%make_install
rm -f examplescripts/Makefile*
chmod a-x -R examplescripts/*
install -D -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/smartmontools
install -D -p -m 755 %{SOURCE4} $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/smartdnotify
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/smartd_warning.d
install -p -D -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
rm -rf $RPM_BUILD_ROOT/etc/{rc.d,init.d}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}
%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if 0%{?with_selinux}
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}
if [ "$1" -le "1" ]; then # First install
   %systemd_postun_with_restart smartd.service
fi
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
    %systemd_postun_with_restart smartd.service
fi
%endif
%preun

%systemd_preun smartd.service
%post

%systemd_post smartd.service
%postun

%systemd_postun_with_restart smartd.service
%files -f %{oreon_filedir}/main.list
%files -n smartmontools-selinux -f %{oreon_filedir}/smartmontools-selinux.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.5-6
- Prepare for Oreon 11 (RP1)
