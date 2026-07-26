%global source0_hash d2b03119cedbf76f63f377aa5c1711979611e7e5e2f8ad6a7c8cb837a1557127

Name:           btrfs-heatmap
Version:        9
Release:        14%{?dist}
Summary:        Visualize the layout of data on your btrfs filesystem over time

License:        MIT
URL:            https://github.com/knorrie/btrfs-heatmap
Source0:        https://github.com/knorrie/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       python3-btrfs >= 10
Suggests:       %{name}-doc = %{version}-%{release}

%description
The btrfs heatmap script creates a visualization of how a btrfs filesystem is
utilizing the underlying disk space of the block devices that are added to it.

%package doc
Summary:        Documentation for %{name}

%description doc
The btrfs heatmap script creates a visualization of how a btrfs filesystem is
utilizing the underlying disk space of the block devices that are added to it.

This package contains the documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Remove execution bit from doc
find doc -type f -print0 | xargs -0 chmod 0644

%build

%install
install -D -p -m 0755 btrfs-heatmap %{buildroot}%{_bindir}/btrfs-heatmap
install -D -p -m 0644 man/btrfs-heatmap.1 %{buildroot}%{_mandir}/man1/btrfs-heatmap.1

%files
%license COPYING
%{_bindir}/btrfs-heatmap
%{_mandir}/man1/btrfs-heatmap.1*

%files doc
%doc README.md CHANGES doc
%license COPYING

%changelog
%autochangelog
