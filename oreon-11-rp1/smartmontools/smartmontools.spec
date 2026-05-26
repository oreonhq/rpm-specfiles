# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 690b83ca331378da9ea0d9d61008c4b22dde391387b9bbad7f29387f2595f76e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# defining macros needed by SELinux
%global with_selinux 1
%global selinuxtype targeted
%global moduletype contrib
%global modulename smartmon

Summary:	Tools for monitoring SMART capable hard disks
Name:		smartmontools
Version:	7.5
Release:	6%{?dist}
Epoch:		1
License:	GPL-2.0-or-later
URL:		https://www.smartmontools.org/
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source2:	smartmontools.sysconf
Source4:	smartdnotify
#semi-automatic update of drivedb.h
%global		UrlSource5	https://sourceforge.net/p/smartmontools/code/HEAD/tree/trunk/smartmontools/drivedb.h?format=raw
Source5:	drivedb.h
Source6:	%{modulename}.te
Source7:	%{modulename}.if
Source8:	%{modulename}.fc
Source9:	smartmontools.tmpfilesd

#fedora/rhel specific
Patch1:		smartmontools-5.38-defaultconf.patch

BuildRequires: make
BuildRequires:	gcc-c++ readline-devel ncurses-devel automake util-linux groff gettext
BuildRequires:	libselinux-devel libcap-ng-devel
BuildRequires:	systemd systemd-devel
# For the _tmpfilesdir macro.
BuildRequires: systemd-rpm-macros

%if 0%{?with_selinux}
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires:	(%{name}-selinux if selinux-policy-%{selinuxtype})
%endif

%if "%{_sbindir}" == "%{_bindir}"
# We rely on filesystem to create the compat symlinks for us
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/smartctl
%endif

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

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
%oreon_verify_sources
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

# update SOURCE5 on maintainer's machine prior commiting, there's no internet connection on builders
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
%endif

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
   # the daemon needs to be restarted for the custom label to be applied
   %systemd_postun_with_restart smartd.service
fi

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
    # the daemon needs to be restarted for the custom label to be removed
    %systemd_postun_with_restart smartd.service
fi
%endif

%preun
%systemd_preun smartd.service

%post
%systemd_post smartd.service

%postun
%systemd_postun_with_restart smartd.service

%files
%doc AUTHORS ChangeLog INSTALL NEWS README
%doc TODO examplescripts smartd.conf
%license COPYING
%dir %{_sysconfdir}/%name
%dir %{_sysconfdir}/%name/smartd_warning.d
%config(noreplace) %{_sysconfdir}/%{name}/smartd.conf
%config(noreplace) %{_sysconfdir}/%{name}/smartd_warning.sh
%config(noreplace) %{_sysconfdir}/sysconfig/smartmontools
%{_unitdir}/smartd.service
%{_sbindir}/smartd
%{_sbindir}/update-smart-drivedb
%{_sbindir}/smartctl
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man?/smart*.*
%{_mandir}/man?/update-smart*.*
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_sharedstatedir}/%{name}

%files selinux
%license COPYING
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.5-6
- Prepare for Oreon 11 (RP1)
