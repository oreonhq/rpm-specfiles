%global source0_hash 3bc1a378aeca1ccc96ed8da0bd27d0ca38ebfe38489766daa0e74d78ca678fe0
Summary:        A set of tools to gather troubleshooting information from a system
Name: sos
Version: 4.12.0
Release:        1%{?dist}
Source0:        https://github.com/sosreport/sos/archive/refs/tags/%{version}.tar.gz#/sos-%{version}.tar.gz
License: GPL-2.0-only
BuildArch: noarch
Url: https://github.com/sosreport/sos
Requires: python3-pexpect
Requires: python3-packaging
Recommends: python3-file-magic
Recommends: python3-requests
Recommends: python3-pyyaml
Obsoletes: sos-collector <= 1.9
Recommends: python3-boto3
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sos = %{version}-%{release}
# /oreon:deps
%description
Sos is a set of tools that gathers information about system
hardware and configuration. The information can then be used for
diagnostic purposes and debugging. Sos is commonly used to help
support technicians and developers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}

%if 0%{?fedora} >= 39 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
%build

%if 0%{?fedora} >= 39 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
%pyproject_wheel
%else
%py3_build
%endif
%check

%install
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
%pyproject_install
%else
%py3_install '--install-scripts=%{_sbindir}'
%endif
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 700 %{buildroot}%{_sysconfdir}/%{name}/cleaner
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/presets.d
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/groups.d
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/extras.d
install -d -m 755 %{buildroot}%{_tmpfilesdir}
install -m 644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -m 644 tmpfiles/tmpfilesd-sos-rh.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
rm -rf %{buildroot}/usr/config/
%find_lang %{name} || echo 0
%oreon_autofiles main

%files

%changelog

%autochangelog
%endif
