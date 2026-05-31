%global source0_hash d3218c5eebe00bf77e84a079bca6a923d7219c31fe2911f18e6ba9cd530ca768

# Disable automatic compilation of Python files in extra directories
%global _python_bytecompile_extra 0

%bcond libreport %{undefined rhel}

Summary: Helps troubleshoot SELinux problems
Name: setroubleshoot
Version: 3.3.36
Release: 3%{?dist}
License: GPL-2.0-or-later
URL: https://gitlab.com/setroubleshoot/setroubleshoot
Source0: https://gitlab.com/-/project/24478376/uploads/51a9cda747130f92860720841a7fd9c9/setroubleshoot-3.3.36.tar.gz
Source1: %{name}.tmpfiles
Source2: %{name}.sysusers
# git format-patch -N 3.3.36
# for j in 00*patch; do printf "Patch: %s\n" $j; done
Patch: 0001-browser-Always-show-Report-Bug-button.patch
BuildRequires: gcc
BuildRequires: make
BuildRequires: libcap-ng-devel
BuildRequires: intltool gettext python3 python3-devel python3-setuptools python3-pip
BuildRequires: (python3-wheel if python3-setuptools < 71)
BuildRequires: desktop-file-utils libnotify-devel libselinux-devel polkit-devel
BuildRequires: audit-libs-devel >= 3.0.1
BuildRequires: python3-libselinux python3-dasbus python3-gobject gtk3-devel
# for the _tmpfilesdir macro
BuildRequires: systemd-rpm-macros
BuildRequires: git-core
Requires: %{name}-server = %{version}-%{release}
Requires: gtk3, libnotify
%if %{with libreport}
Recommends: libreport-gtk >= 2.2.1-2, python3-libreport
%endif
Requires: python3-gobject, python3-dasbus
Requires(post): desktop-file-utils
Requires(post): dbus
Requires(postun): desktop-file-utils
Requires(postun): dbus

BuildRequires: xdg-utils
Requires: xdg-utils

%global pkgpythondir  %{python3_sitelib}/%{name}
%global pkgguidir     %{_datadir}/%{name}/gui
%global pkgdatadir    %{_datadir}/%{name}
%global pkglibexecdir %{_prefix}/libexec/%{name}
%global pkgvardatadir %{_localstatedir}/lib/%{name}
%global pkgconfigdir  %{_sysconfdir}/%{name}
%global pkgdatabase   %{pkgvardatadir}/setroubleshoot_database.xml

%description
setroubleshoot GUI. Application that allows you to view setroubleshoot-server
messages.
Provides tools to help diagnose SELinux problems. When AVC messages
are generated an alert can be generated that will give information
about the problem and help track its resolution. Alerts can be configured
to user preference. The same tools can be run on existing log files.

%files
%{pkgguidir}
%config(noreplace) %{_sysconfdir}/xdg/autostart/*
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.metainfo.xml
%{_datadir}/dbus-1/services/org.fedoraproject.sealert.service
%{_datadir}/icons/hicolor/*/*/*
%dir %attr(0755,root,root) %{pkgpythondir}
%{pkgpythondir}/browser.py
%{pkgpythondir}/__pycache__/browser.cpython*
%{pkgpythondir}/gui_utils.py
%{pkgpythondir}/__pycache__/gui_utils.cpython*
%{_bindir}/seapplet


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p 1 -S git

%build
%configure PYTHON=%{__python3} --enable-seappletlegacy=no --with-auditpluginsdir=/etc/audit/plugins.d
make

%install
%make_install PREFIX=/usr PIP_NO_BUILD_ISOLATION=0
desktop-file-install --vendor="" --dir=%{buildroot}%{_datadir}/applications %{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{pkgvardatadir}
mkdir -p %{buildroot}%{_rundir}/setroubleshoot
touch %{buildroot}%{pkgdatabase}
touch %{buildroot}%{pkgvardatadir}/email_alert_recipients
rm -rf %{buildroot}/usr/share/doc/
# create /run/setroubleshoot on boot
install -p -m644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -p -m644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf


%find_lang %{name}

%package server
Summary: SELinux troubleshoot server

Requires: %{name}-plugins >= 3.3.10
Requires: audit >= 3.0.1
Requires: audit-libs-python3
Requires: libxml2-python3
Requires: rpm-python3
Requires: libselinux-python3  >= 2.1.5-1
Requires: policycoreutils-python-utils
BuildRequires: intltool gettext python3
BuildRequires: python3-devel
Requires: systemd-python3 >= 206-1
Requires: python3-gobject-base >= 3.11
Requires: dbus
Requires: python3-dbus python3-dasbus
Requires: polkit

%description server
Provides tools to help diagnose SELinux problems. When AVC messages
are generated an alert can be generated that will give information
about the problem and help track its resolution. Alerts can be configured
to user preference. The same tools can be run on existing log files.


%post server
/usr/bin/auditctl --signal reload >/dev/null 2>&1 || :

%postun server
/usr/bin/auditctl --signal reload >/dev/null 2>&1 || :

%files server -f %{name}.lang
%{_bindir}/sealert
%{_sbindir}/sedispatch
%{_sbindir}/setroubleshootd
%{python3_sitelib}/setroubleshoot*.dist-info
%dir %attr(0755,root,root) %{pkgconfigdir}
%dir %{pkgpythondir}
%dir %{pkgpythondir}/__pycache__
%{pkgpythondir}/Plugin.py
%{pkgpythondir}/__init__.py
%{pkgpythondir}/access_control.py
%{pkgpythondir}/analyze.py
%{pkgpythondir}/audit_data.py
%{pkgpythondir}/avc_audit.py
%{pkgpythondir}/config.py
%{pkgpythondir}/email_alert.py
%{pkgpythondir}/errcode.py
%{pkgpythondir}/html_util.py
%{pkgpythondir}/rpc.py
%{pkgpythondir}/serverconnection.py
%{pkgpythondir}/rpc_interfaces.py
%{pkgpythondir}/server.py
%{pkgpythondir}/signature.py
%{pkgpythondir}/util.py
%{pkgpythondir}/uuid.py
%{pkgpythondir}/xml_serialize.py
%{pkgpythondir}/__pycache__/Plugin.cpython*
%{pkgpythondir}/__pycache__/__init__.cpython*
%{pkgpythondir}/__pycache__/access_control.cpython*
%{pkgpythondir}/__pycache__/analyze.cpython*
%{pkgpythondir}/__pycache__/audit_data.cpython*
%{pkgpythondir}/__pycache__/avc_audit.cpython*
%{pkgpythondir}/__pycache__/config.cpython*
%{pkgpythondir}/__pycache__/email_alert.cpython*
%{pkgpythondir}/__pycache__/errcode.cpython*
%{pkgpythondir}/__pycache__/html_util.cpython*
%{pkgpythondir}/__pycache__/rpc.cpython*
%{pkgpythondir}/__pycache__/rpc_interfaces.cpython*
%{pkgpythondir}/__pycache__/server.cpython*
%{pkgpythondir}/__pycache__/serverconnection.cpython*
%{pkgpythondir}/__pycache__/signature.cpython*
%{pkgpythondir}/__pycache__/util.cpython*
%{pkgpythondir}/__pycache__/uuid.cpython*
%{pkgpythondir}/__pycache__/xml_serialize.cpython*
%dir %{pkgdatadir}
%{pkgdatadir}/SetroubleshootFixit.py
%{pkgdatadir}/SetroubleshootPrivileged.py
%config(noreplace) %{pkgconfigdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.fedoraproject.Setroubleshootd.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.fedoraproject.SetroubleshootPrivileged.conf
%attr(0700,setroubleshoot,setroubleshoot) %dir %{pkgvardatadir}
%ghost %attr(0600,setroubleshoot,setroubleshoot) %{pkgdatabase}
%ghost %attr(0600,setroubleshoot,setroubleshoot) %{pkgvardatadir}/email_alert_recipients
%{_mandir}/man1/seapplet.1*
%{_mandir}/man8/sealert.8*
%{_mandir}/man8/sedispatch.8*
%{_mandir}/man8/setroubleshootd.8*
%config /etc/audit/plugins.d/sedispatch.conf
%{_unitdir}/setroubleshootd.service
%{_datadir}/dbus-1/system-services/org.fedoraproject.Setroubleshootd.service
%{_datadir}/dbus-1/system-services/org.fedoraproject.SetroubleshootPrivileged.service
%{_datadir}/polkit-1/actions/org.fedoraproject.setroubleshootfixit.policy
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.fedoraproject.SetroubleshootFixit.conf
%{_datadir}/dbus-1/system-services/org.fedoraproject.SetroubleshootFixit.service
%attr(0644,root,root) %{_tmpfilesdir}/%{name}.conf
%attr(0644,root,root) %{_sysusersdir}/%{name}.conf
%attr(0711,setroubleshoot,setroubleshoot) %dir %{_rundir}/setroubleshoot
%doc AUTHORS COPYING ChangeLog DBUS.md NEWS README TODO

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.36-3
- Prepare for Oreon 11 (RP1)
