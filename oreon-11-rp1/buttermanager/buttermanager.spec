%global source0_hash 0f139fc05b8fe150290a21578a5f28f8e0169a81df8c4176d0ec0fe9742fc6f8

Name:           buttermanager
Version:        2.5.2
Release:        %autorelease
Summary:        Tool for managing Btrfs snapshots, balancing filesystems and more

License:        GPL-3.0-only
URL:            https://github.com/egara/buttermanager
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
Requires:       btrfs-progs
Requires:       python3-tkinter
# Recommends:     grub2-btrfs

%description
ButterManager is a BTRFS tool for managing snapshots, balancing filesystems
and upgrading the system safely.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l buttermanager

install -Dpm644 packaging/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Fix the desktop file
sed \
  -e "s/Icon=.*/Icon=%{name}/" \
  -i packaging/%{name}.desktop

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  packaging/%{name}.desktop

%files -f %{pyproject_files}
%doc README.md doc
%{_bindir}/buttermanager
%{python3_sitelib}/buttermanager*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
%autochangelog
