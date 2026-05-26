Name:       rig
Summary:    Monitor a system for events and trigger specific actions
Version:    1.1
Release:    16%{?dist}
Url:        https://github.com/TurboTurtle/rig
Source0:        https://github.com/TurboTurtle/rig/archive/rig-1.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 af9bf8ada657d405a5dca89cbb4831302a99ff04328cfb7e056a98b066534330
%global source0_file rig-1.1.tar.gz
# oreon url source checksums end
License:    GPL-2.0-only
BuildArch:  noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3dist(systemd-python)
BuildRequires: python3dist(psutil)

%description
Rig is a utility designed to watch or monitor specific system resources (e.g.
log files, journals, system activity, etc...) and then take specific action
when the trigger condition is met. Its primary aim is to assist in
troubleshooting and data collection for randomly occurring events.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/rig-1.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "af9bf8ada657d405a5dca89cbb4831302a99ff04328cfb7e056a98b066534330" || { echo "oreon: Source0 SHA256 mismatch for rig-1.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%py3_build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m644 man/en/rig.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
%py3_install

%files
%{_bindir}/rig
%{_mandir}/man1/*

%{python3_sitelib}/rig-*.egg-info/
%{python3_sitelib}/rigging/

%license LICENSE
%doc README.md

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-16
- Import
