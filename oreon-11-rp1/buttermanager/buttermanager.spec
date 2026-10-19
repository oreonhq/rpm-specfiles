%global source0_hash 0f139fc05b8fe150290a21578a5f28f8e0169a81df8c4176d0ec0fe9742fc6f8
Name:           buttermanager
Version:        2.5.2
Release:        1%{?dist}
Summary:        Tool for managing Btrfs snapshots, balancing filesystems and more
License:        GPL-3.0-only
URL:            https://github.com/egara/buttermanager
Source0:        https://github.com/egara/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       btrfs-progs
Requires:       python3-tkinter
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-buttermanager = %{version}-%{release}
# /oreon:deps
%description
ButterManager is a BTRFS tool for managing snapshots, balancing filesystems
and upgrading the system safely.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -Dpm644 packaging/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
sed \
  -e "s/Icon=.*/Icon=%{name}/" \
  -i packaging/%{name}.desktop
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  packaging/%{name}.desktop
%oreon_autofiles main

%files

%changelog

%autochangelog
