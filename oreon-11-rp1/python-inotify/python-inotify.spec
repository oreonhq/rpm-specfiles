%global source0_hash 9c998a5d7606ca835065cdabc013ae6c66eb9ea76a00a1e3bc6e0cfe2b4f71f4
%global oname  pyinotify
Summary:        Monitor filesystem events with Python under Linux
Name:          python-inotify
Version:       0.9.6
Release:        1%{?dist}
License:       MIT
URL:           https://github.com/seb-m/pyinotify
Source0:        http://seb.dbzteam.org/pub/pyinotify/releases/pyinotify-%{version}.tar.gz
Patch:         pyinotify-0.9.6-epoint.patch
Patch:         pyinotify-python-3.12-fix.patch
BuildArch:     noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-inotify = %{version}-%{release}
# /oreon:deps
%description

%package    -n python%{python3_pkgversion}-inotify
Summary:        Monitor filesystem events with Python under Linux
%description -n python%{python3_pkgversion}-inotify

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{oname}-%{version}
sed -i '1c#! %{__python3}' python3/pyinotify.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/inotify* usr/lib64/python3*/site-packages/inotify* usr/bin/*

%check

%pyproject_check_import
%py3_check_import pyinotify
%files
%files -n python3-inotify -f %{oreon_filedir}/python3-inotify.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.6-43
- Prepare for Oreon 11 (RP1)
