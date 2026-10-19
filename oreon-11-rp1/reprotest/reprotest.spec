%global source2_hash 7d0051d4b6a72cef4e00ae84b75795cc5076ae88ed6d2d920290a21281363e0d
%global source1_hash 48d7c5f5497db3113b736519b0abb82a276cbbeb21db8107ea6ed8444f94204a
%global source0_hash 3224867191f9c2cdeca5dc3acf8bf34a4ad1fedf235e697c86872d7f2a384b7b
Name:           reprotest
Version:        0.7.32
Release:        1%{?dist}
Summary:        Build packages and check them for reproducibility
URL:            https://salsa.debian.org/reproducible-builds/%{name}
License:        GPL-3.0-or-later
Source0:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}_%{version}.tar.xz
Source1:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}_%{version}.tar.xz.asc
Source2:        https://salsa.debian.org/reproducible-builds/reproducible-website/-/raw/master/reproducible-builds-developers-keys.asc
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-rstr
Requires:       diffoscope
Requires:       disorderfs
Requires:       faketime
Requires:       fakeroot
Requires:       glibc-all-langpacks
Requires:       rpm-build
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-reprotest = %{version}-%{release}
# /oreon:deps
%description
reprotest builds the same source code twice in different environments, and
then checks the binaries produced by each build for differences. If any are
found, then diffoscope (or if unavailable then diff) is used to display them
in detail for later analysis.

It supports different types of environment such as a "null" environment (i.e.
doing the builds directly in /tmp) or various other virtual servers, for
example schroot, ssh, qemu, and several others.

reprotest is developed as part of the "reproducible builds" Debian project.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
