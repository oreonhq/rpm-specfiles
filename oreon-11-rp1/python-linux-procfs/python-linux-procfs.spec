%global source0_hash 3a15e97b5e19279978e9aab5567416d76b8101f2cc82f95aca0f6f2dade4fbd7
%global without_python3 1
Name: python-linux-procfs
Version: 0.7.4
Release:        1%{?dist}
License: GPL-2.0-only
Summary:        Linux /proc abstraction classes
Source0:        https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
URL: https://www.kernel.org/pub/software/libs/python/python-linux-procfs
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-linux-procfs = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-linux-procfs
Summary: %summary
%{?python_provide:%python_provide python3-linux-procfs}
%description -n python3-linux-procfs

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-linux-procfs usr/lib/python3*/site-packages/linux_procfs* usr/lib64/python3*/site-packages/linux_procfs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/linux_procfs* usr/lib64/python3*/site-packages/linux_procfs* usr/bin/*

%files
%files -n python3-linux-procfs -f %{oreon_filedir}/python3-linux-procfs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.4-2
- Prepare for Oreon 11 (RP1)
