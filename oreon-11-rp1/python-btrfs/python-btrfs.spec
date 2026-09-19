%global source0_hash 9f6663b0d019f341587f330fc1c7396c367fb4bddbd4de9c9f11c3fb41acdddd

Name: python-btrfs
Version: 15
Release: 6%{?dist}
Summary: Python module to inspect btrfs filesystems
# Automatically converted from old format: LGPLv3+ and MIT - review is highly recommended.
License: LGPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL: https://github.com/knorrie/python-btrfs
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-sphinx

%global _description %{expand:
The primary goal of this module is to be able to inspect the internals of an
existing filesystem for educational purposes.

The python module acts as a wrapper around the low level kernel calls and btrfs
data structures, presenting them as python objects with interesting attributes
and references to other objects.}

%description %_description

%package -n python3-btrfs
Summary: %{summary}
Suggests: %{name}-doc

%description -n python3-btrfs %_description

%package doc
Summary: %{summary}

%description doc %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
# Remove dangling symlink
rm -f examples/btrfs
# Don't pull additional dependencies in doc
find examples -type f -print0 | xargs -0 chmod 0644

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs
%make_build html
%make_build text
find build -name .buildinfo -delete
popd

%install
%pyproject_install
%pyproject_save_files -l btrfs
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 bin/btrfs-balance-least-used %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-orphan-cleaner-progress %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-space-calculator %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-usage-report %{buildroot}%{_bindir}
install -m 0644 man/* %{buildroot}%{_mandir}/man1

%files -n python3-btrfs -f %{pyproject_files}
%license COPYING.LESSER
%{_bindir}/*
%{_mandir}/man1/*

%files doc
%doc CHANGES README.md examples
%doc docs/build/html docs/build/text
%license COPYING.LESSER

%changelog
%autochangelog
