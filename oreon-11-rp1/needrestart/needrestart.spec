%global source0_hash 42664e0b1b98fef1e5e849118b9985ac951516c4d5eb24a7da15d058da647c90

Name:           needrestart
Version:        3.8
Release:        8%{?dist}
Summary:        Restart daemons after library updates

License:        GPL-2.0-or-later
URL:            https://github.com/liske/%{name}
Source0:        https://github.com/liske/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        debconf__needrestart.templates
Source2:        restart.d__auditd.service
Source3:        yum__plugin.py
Source4:        dnf__plugin.py

BuildArch:         noarch
BuildRequires: make
BuildRequires:     perl
BuildRequires:     perl-generators
BuildRequires:     gettext
BuildRequires:     perl(ExtUtils::MakeMaker)
BuildRequires:     debconf
BuildRequires:     po-debconf
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:     python3-devel
Requires:          python3-dnf
%else
Requires:          yum
Requires:          python2-subprocess32
%endif
Requires:          xz
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:        perl(Debconf::Client::ConfModule)
Recommends:        iucode-tool
%else
Requires:          iucode-tool
%endif

%{?perl_default_filter}

%if 0%{?fedora} || 0%{?rhel} >= 8
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Debconf::Client::ConfModule\\)
%endif

%description
needrestart checks which daemons need to be restarted after library
upgrades. It is inspired by checkrestart from the debian-goodies
package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p 1

%build
%make_build

%install
%make_install
mkdir -p %{buildroot}/%{_mandir}/man1
cp man/needrestart.1 %{buildroot}/%{_mandir}/man1/
%find_lang %{name}
%find_lang needrestart-notify
# useless files
rm -rf %{buildroot}/%{perl_archlib}
# binary install path is hardcoded in the Makefile
# (see https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin)
mkdir -p %{buildroot}/usr/bin
mv %{buildroot}/usr/sbin/%{name} %{buildroot}/usr/bin/%{name}
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1489569
cp %{SOURCE1} %{buildroot}/%{_datadir}/%{name}/needrestart.templates
# workaround for https://github.com/liske/needrestart/issues/75
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}/restart.d/auditd.service
chmod a+x %{buildroot}/%{_sysconfdir}/%{name}/restart.d/auditd.service
%if 0%{?fedora} || 0%{?rhel} >= 8
mkdir -p %{buildroot}/%{_sysconfdir}/dnf/plugins %{buildroot}/%{python3_sitelib}/dnf-plugins
echo -e "[main]\nenabled=1\n" >%{buildroot}/%{_sysconfdir}/dnf/plugins/needrestart.conf
cp %{SOURCE4} %{buildroot}/%{python3_sitelib}/dnf-plugins/needrestart.py
%else
mkdir -p %{buildroot}/%{_sysconfdir}/yum/pluginconf.d %{buildroot}/usr/lib/yum-plugins
echo -e "[main]\nenabled=1\n" >%{buildroot}/%{_sysconfdir}/yum/pluginconf.d/needrestart.conf
cp %{SOURCE3} %{buildroot}/usr/lib/yum-plugins/needrestart.py
%endif
# this calls the rpm command and breaks the RPM DB
# (I guess it's not closed yet in the close_hook)
# we use systemd for all services so this is not needed anyway
rm %{buildroot}/%{_sysconfdir}/%{name}/hook.d/20-rpm
# see https://github.com/liske/needrestart/issues/123
mkdir -p %{buildroot}/%{_sysconfdir}/default
echo "IUCODE_TOOL_EXTRA_OPTIONS=--ignore-broken" >%{buildroot}/%{_sysconfdir}/default/intel-microcode

# About executable files in the /etc directory:
#   The 'README.needrestart' files in /etc/needrestart/restart.d/ and
#   /etc/needrestart/notify.d/ explicitly say the files will only be
#   considered if they are executables. There's nothing said for
#   /etc/needrestart/hook.d/ but I guess this is the same logic.
%files -f %{name}.lang -f needrestart-notify.lang
%license COPYING
%doc README.md README.batch.md README.Cont.md README.Interp.md README.nagios.md README.uCode.md NEWS ChangeLog
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/default/intel-microcode
%{_bindir}/%{name}
%{perl_vendorlib}/*
# %%{_libdir} resolves to /usr/lib64 on 64-bits systems, but the software does not handle this
/usr/lib/%{name}
%{_datadir}/%{name}
%{_datadir}/polkit-1
%{_mandir}/man1/needrestart.1*
%if 0%{?fedora} || 0%{?rhel} >= 8
%config(noreplace) %{_sysconfdir}/dnf/plugins/needrestart.conf
%pycached %{python3_sitelib}/dnf-plugins/needrestart.py
%else
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/needrestart.conf
/usr/lib/yum-plugins
%endif

%changelog
%autochangelog
