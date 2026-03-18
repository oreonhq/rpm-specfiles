Summary: A system tool for maintaining the /etc/rc*.d hierarchy
Name: chkconfig
Version: 1.33
Release: 5%{?dist}
License: GPL-2.0-only
URL: https://github.com/fedora-sysv/chkconfig
Source: https://github.com/fedora-sysv/chkconfig/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# https://github.com/fedora-sysv/chkconfig/pull/157
# https://bugzilla.redhat.com/show_bug.cgi?id=2363937
# ignore 'duplicate' entries in config file (same effective binary)
# avoids issue where package install/update disables service
Patch: 0001-Ignore-alternatives-that-are-binary-identical-to-exi.patch

BuildRequires: gcc gettext libselinux-devel make newt-devel popt-devel pkgconfig(systemd)
# beakerlib might not be available on CentOS Stream any more
%if 0%{?fedora}
BuildRequires: beakerlib
%endif

%global merged_sbin %["%{_sbindir}" == "%{_bindir}"]

Conflicts: initscripts <= 5.30-1

Provides: /sbin/chkconfig

%description
Chkconfig is a basic system utility.  It updates and queries runlevel
information for system services.  Chkconfig manipulates the numerous
symbolic links in /etc/rc.d, to relieve system administrators of some
of the drudgery of manually editing the symbolic links.

%package -n ntsysv
Summary: A tool to set the stop/start of system services in a runlevel
Requires: chkconfig = %{version}-%{release}

%description -n ntsysv
Ntsysv provides a simple interface for setting which system services
are started or stopped in various runlevels (instead of directly
manipulating the numerous symbolic links in /etc/rc.d). Unless you
specify a runlevel or runlevels on the command line (see the man
page), ntsysv configures the current runlevel (5 if you're using X).

%package -n alternatives
Summary: A tool to maintain symbolic links determining default commands
%if %{merged_sbin}
Provides: /usr/sbin/alternatives
Provides: /usr/sbin/update-alternatives
Requires: filesystem(unmerged-sbin-symlinks)
%endif

%description -n alternatives
alternatives creates, removes, maintains and displays information about the
symbolic links comprising the alternatives system. It is possible for several
programs fulfilling the same or similar functions to be installed on a single
system at the same time.

%prep
%autosetup -p1

%build
%make_build RPM_OPT_FLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" MERGED_SBIN=%{merged_sbin}

# tests are executed using tmt and tf on CentOS Stream and RHEL
%if 0%{?fedora}
%check
make check
%endif

%install
rm -rf $RPM_BUILD_ROOT
%make_install MANDIR=%{_mandir} SBINDIR=%{_sbindir}

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
ln -s rc.d/init.d $RPM_BUILD_ROOT/etc/init.d
for n in 0 1 2 3 4 5 6; do
    mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc${n}.d
    ln -s rc.d/rc${n}.d $RPM_BUILD_ROOT/etc/rc${n}.d
done
mkdir -p $RPM_BUILD_ROOT/etc/chkconfig.d

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_sbindir}/chkconfig
%{_sysconfdir}/chkconfig.d
%{_sysconfdir}/init.d
%{_sysconfdir}/rc.d
%{_sysconfdir}/rc.d/init.d
%{_sysconfdir}/rc[0-6].d
%{_sysconfdir}/rc.d/rc[0-6].d
%{_mandir}/*/chkconfig*
%{_prefix}/lib/systemd/systemd-sysv-install

%files -n ntsysv
%defattr(-,root,root)
%{_sbindir}/ntsysv
%{_mandir}/*/ntsysv.8*

%files -n alternatives
%license COPYING
%dir /etc/alternatives
%ghost %dir %attr(755, root, root) /etc/alternatives.admindir
%ghost %dir %attr(755, root, root) /var/lib/alternatives
%{_sbindir}/update-alternatives
%{_sbindir}/alternatives
%{_mandir}/*/update-alternatives*
%{_mandir}/*/alternatives*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.33-5
- Prepare for Oreon 11 (RP1)
