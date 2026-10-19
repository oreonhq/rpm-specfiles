%global source0_hash d3218c5eebe00bf77e84a079bca6a923d7219c31fe2911f18e6ba9cd530ca768
%global _python_bytecompile_extra 0
%bcond libreport %{undefined rhel}
Summary:        Helps troubleshoot SELinux problems
Name: setroubleshoot
Version: 3.3.36
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://gitlab.com/setroubleshoot/setroubleshoot
Source0:        https://gitlab.com/-/project/24478376/uploads/51a9cda747130f92860720841a7fd9c9/setroubleshoot-3.3.36.tar.gz
Source1: %{name}.tmpfiles
Source2: %{name}.sysusers
Patch: 0001-browser-Always-show-Report-Bug-button.patch
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
Requires: xdg-utils
%global pkgpythondir  %{python3_sitelib}/%{name}
%global pkgguidir     %{_datadir}/%{name}/gui
%global pkgdatadir    %{_datadir}/%{name}
%global pkglibexecdir %{_prefix}/libexec/%{name}
%global pkgvardatadir %{_localstatedir}/lib/%{name}
%global pkgconfigdir  %{_sysconfdir}/%{name}
%global pkgdatabase   %{pkgvardatadir}/setroubleshoot_database.xml
# oreon:deps
BuildRequires:  (python3-wheel if python3-setuptools < 71)
BuildRequires:  audit-libs-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libcap-ng-devel
BuildRequires:  libnotify-devel
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  polkit-devel
BuildRequires:  python3
BuildRequires:  python3-dasbus
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-libselinux
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
BuildRequires:  xdg-utils
# /oreon:deps
%description
setroubleshoot GUI. Application that allows you to view setroubleshoot-server
messages.
Provides tools to help diagnose SELinux problems. When AVC messages
are generated an alert can be generated that will give information
about the problem and help track its resolution. Alerts can be configured
to user preference. The same tools can be run on existing log files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
install -p -m644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -p -m644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n setroubleshoot-server -f %{oreon_filedir}/setroubleshoot-server.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.36-3
- Prepare for Oreon 11 (RP1)
