%global source0_hash 4c480818e9839cf03ca9c9cecfe4bc864a779cca742a3479a47d33f40579ff90
%global oname rtslib-fb
%bcond_with apidocs
Name:             python-rtslib
License:          Apache-2.0
Summary:        API for Linux kernel LIO SCSI target
Version:          2.2.4
Release:        1%{?dist}
URL:              https://github.com/open-iscsi/%{oname}
Source0:        https://github.com/open-iscsi/rtslib-fb/archive/v%{version}/rtslib-fb-2.2.4.tar.gz#/python-rtslib-2.2.4.tar.gz
Patch0:           0001-disable-xen_pvscsi.patch
BuildArch:        noarch
%if %{with apidocs}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rtslib = %{version}-%{release}
# /oreon:deps
%description

%if %{with apidocs}
%package doc
Summary:        Documentation for python-rtslib
Requires:       python3-rtslib = %{version}-%{release}
%description doc
API documentation for rtslib, to configure the generic Linux SCSI
multiprotocol kernel target.
%endif

%package -n python3-rtslib
Summary:        API for Linux kernel LIO SCSI target
BuildRequires:  python3-devel
BuildRequires:  python3-kmod
Requires:       python3-kmod
%if ! %{with apidocs}
Obsoletes:      %{name}-doc < %{version}-%{release}
%endif
# oreon:reqs
Requires:       python3dist(pyudev) >= 0.18
# /oreon:reqs
%description -n python3-rtslib
API for generic Linux SCSI kernel target.

%package -n target-restore
Summary:          Systemd service for targetcli/rtslib
Requires:         python3-rtslib = %{version}-%{release}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%description -n target-restore
Systemd service to restore the LIO kernel target settings
on system restart.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{oname}-%{version}
%patch -P0 -p1

%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%if %{with apidocs}
mkdir -p doc/html
epydoc --no-sourcecode --html -n rtslib -o doc/html rtslib/*.py
%endif
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/target/backup
mkdir -p %{buildroot}%{_localstatedir}/target/pr
mkdir -p %{buildroot}%{_localstatedir}/target/alua
install -m 644 systemd/target.service %{buildroot}%{_unitdir}/target.service
install -m 644 doc/targetctl.8 %{buildroot}%{_mandir}/man8/
install -m 644 doc/saveconfig.json.5 %{buildroot}%{_mandir}/man5/
%oreon_autofiles python3-rtslib usr/lib/python3*/site-packages/rtslib* usr/lib64/python3*/site-packages/rtslib* usr/bin/*
%oreon_autofiles target-restore usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/rtslib* usr/lib64/python3*/site-packages/rtslib* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%post -n target-restore

%systemd_post target.service
%preun -n target-restore

%systemd_preun target.service
%postun -n target-restore

%systemd_postun_with_restart target.service
%files
%files -n python3-rtslib -f %{oreon_filedir}/python3-rtslib.list
%files -n target-restore -f %{oreon_filedir}/target-restore.list

%changelog

%autochangelog
