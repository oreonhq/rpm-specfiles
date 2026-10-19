%global source0_hash 437cfdada284e3c10e7439cdbd0c3180d897f5a218cf156ebfcd170df40b3bc9
Name:           python-rpm-generators
Summary:        Dependency generators for Python RPMs
Version:        14
Release:        1%{?dist}
Url:            https://src.fedoraproject.org/rpms/python-rpm-generators
Source0:        https://raw.githubusercontent.com/rpm-software-management/rpm/102eab50b3d0d6546dfe082eac0ade21e6b3dbf1/COPYING
Source1:        python.attr
Source2:        pythondist.attr
Source3:        pythonname.attr
Source4:        pythondistdeps.py
Source5:        pythonbundles.py
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND (LicenseRef-Fedora-Public-Domain OR LGPL-2.1-or-later OR GPL-2.0-or-later)
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
%{summary}.

%package -n python3-rpm-generators
Summary:        Dependency generators for Python RPMs
Requires:       python3-packaging
Requires:       rpm > 4.15.90-0
Requires:       python-srpm-macros >= 3.10-15
%description -n python3-rpm-generators
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c -T
cp -a %{sources} .

%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} *.attr
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} *.py
%oreon_autofiles python3-rpm-generators usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-rpm-generators -f %{oreon_filedir}/python3-rpm-generators.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 14-15
- Prepare for Oreon 11 (RP1)
