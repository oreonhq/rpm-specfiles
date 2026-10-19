%global source0_hash 9f6663b0d019f341587f330fc1c7396c367fb4bddbd4de9c9f11c3fb41acdddd
Name: python-btrfs
Version: 15
Release:        1%{?dist}
Summary:        Python module to inspect btrfs filesystems
License: LGPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL: https://github.com/knorrie/python-btrfs
Source0:        https://github.com/knorrie/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-btrfs = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-btrfs
Summary:        Python module to inspect btrfs filesystems
Suggests: %{name}-doc
%description -n python3-btrfs

%package doc
Summary: %{summary}
%description doc

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
# Remove dangling symlink
rm -f examples/btrfs
# Don't pull additional dependencies in doc
find examples -type f -print0 | xargs -0 chmod 0644

%build

%pyproject_wheel
pushd docs
%make_build html
%make_build text
find build -name .buildinfo -delete
popd
%install
%pyproject_install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 bin/btrfs-balance-least-used %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-orphan-cleaner-progress %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-space-calculator %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-usage-report %{buildroot}%{_bindir}
install -m 0644 man/* %{buildroot}%{_mandir}/man1
%oreon_autofiles python3-btrfs usr/lib/python3*/site-packages/btrfs* usr/lib64/python3*/site-packages/btrfs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/btrfs* usr/lib64/python3*/site-packages/btrfs* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n python3-btrfs -f %{oreon_filedir}/python3-btrfs.list
%files -n python-btrfs-doc -f %{oreon_filedir}/python-btrfs-doc.list

%changelog

%autochangelog
