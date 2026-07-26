%global source0_hash 49a1522d6857e60b2e1efec0a27fcbf9d0adf3362dbef6348821d5cfdfa6eff5

%global tardate 20210704
%global tarrev  34341a53
%global tarname TracMonotone-%{version}.dev%{tardate}

Name:           trac-monotone-plugin
Version:        0.0.15
Release:        0.18.%{tardate}mtn%{tarrev}%{?dist}
Summary:        Monotone version control plugin for Trac
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://tracmtn.1erlei.de/
# Source comes from mtn right now:
#  mtn clone -r %%{tarrev} monotone.ca net.venge.monotone.trac-plugin tracmtn
#  cd tracmtn; python3 setup.py sdist --formats bztar
Source:         %{tarname}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-setuptools
Requires:       trac >= 1.5
Requires:       monotone >= 1.1

%description
This Trac plugin provides support for the Monotone SCM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{tarname}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l tracmtn

%files -f %{pyproject_files}
%doc README

%changelog
%autochangelog
