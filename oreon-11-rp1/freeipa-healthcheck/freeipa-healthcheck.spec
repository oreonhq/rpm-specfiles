%global source0_hash a1cb4f11ea89015e20c4cd21c32189457af633e9915de56a5a333a9cea99e6a7
%global prefix freeipa
%global productname FreeIPA
%global alt_prefix ipa
%global debug_package %{nil}
%global python3dir %{_builddir}/python3-%{name}-%{version}-%{release}
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%global alt_name %{alt_prefix}-healthcheck
%bcond_without tests
Name:           %{prefix}-healthcheck
Version:        0.19
Release:        1%{?dist}
Summary:        Health check tool for FreeIPA
BuildArch:      noarch
License:        GPL-3.0-or-later
URL:            https://github.com/freeipa/freeipa-healthcheck
Source0:        https://github.com/freeipa/freeipa-healthcheck/archive/%{version}.tar.gz
Source1:        ipahealthcheck.conf
Patch0001:      0001-Remove-ipaclustercheck.patch
Patch0002:      0002-Migrate-from-pkg_resources.patch
Patch0003:      0003-IPAFileCheck-also-allow-640-for-kra-debug-log.patch
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{prefix}-server
Requires:       python3-ipalib
Requires:       python3-ipaserver
Requires:       python3-lib389 >= 1.4.2.14-1
Requires:       anacron
Requires:       logrotate
Requires(post): systemd-units
Requires:       %{name}-core = %{version}-%{release}
%{?systemd_requires}
%if %{with tests}
%endif
Provides:       %{alt_name} = %{version}
Conflicts:      %{alt_name}
Obsoletes:      %{alt_name} < %{version}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-freeipa-healthcheck = %{version}-%{release}
# /oreon:deps
%description
The %{productname} health check tool provides a set of checks to
proactively detect defects in a FreeIPA cluster.

%package -n %{name}-core
Summary: Core plugin system for healthcheck
Provides:       %{alt_name}-core = %{version}
Conflicts:      %{alt_name}-core
Obsoletes:      %{alt_name}-core < %{version}
%description -n %{name}-core
Core plugin system for healthcheck, usable standalone with other
packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir freeipa-healthcheck-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_sysconfdir}/ipahealthcheck
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/ipahealthcheck
mkdir -p %{buildroot}/%{_unitdir}
install -p -m644 %{_builddir}/freeipa-healthcheck-%{version}/systemd/ipa-healthcheck.service %{buildroot}%{_unitdir}
install -p -m644 %{_builddir}/freeipa-healthcheck-%{version}/systemd/ipa-healthcheck.timer %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/%{_libexecdir}/ipa
install -p -m755 %{_builddir}/freeipa-healthcheck-%{version}/systemd/ipa-healthcheck.sh %{buildroot}%{_libexecdir}/ipa/
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m644 %{_builddir}/freeipa-healthcheck-%{version}/logrotate/ipahealthcheck %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}/%{_localstatedir}/log/ipa/healthcheck
mkdir -p %{buildroot}/%{_mandir}/man8
mkdir -p %{buildroot}/%{_mandir}/man5
install -p -m644 %{_builddir}/freeipa-healthcheck-%{version}/man/man8/ipa-healthcheck.8  %{buildroot}%{_mandir}/man8/
install -p -m644 %{_builddir}/freeipa-healthcheck-%{version}/man/man5/ipahealthcheck.conf.5  %{buildroot}%{_mandir}/man5/
(cd %{buildroot}/%{python3_sitelib}/ipahealthcheck && find . -type f  | \
    grep -v '^./core' | \
    grep -v 'opt-1' | \
    sed -e 's,\.py.*$,.*,g' | sort -u | \
    sed -e 's,\./,%%{python3_sitelib}/ipahealthcheck/,g' ) >healthcheck.list
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

PYTHONPATH=src PATH=$PATH:$RPM_BUILD_ROOT/usr/bin pytest-3 tests/test_*
%endif
%post

%systemd_post ipa-healthcheck.service
%preun

%systemd_preun ipa-healthcheck.service
%postun

%systemd_postun_with_restart ipa-healthcheck.service
%files
%files -n freeipa-healthcheck-core -f %{oreon_filedir}/freeipa-healthcheck-core.list

%changelog

%autochangelog

