%global source0_hash 21840b7da403774d8d7a7008f1dd3e27ffbd60a4abf12eb7b5593bed519530c9

# manually read from Makefile
%global _deepin_version 25

Name:           deepin-desktop-base
Version:        2025.11.25
Release:        %autorelease
Summary:        Base component for Deepin
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-desktop-base
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        distribution.info

BuildArch:      noarch

BuildRequires:  make

Requires:       fedora-logos

%description
This package provides some components for Deepin desktop environment.

- deepin logo
- deepin desktop version
- login screen background image
- language information

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix data path
sed -i 's|/usr/lib|%{_datadir}|' Makefile

%build
VERSION=%{_deepin_version}
RELEASE=
sed -e "s|@@VERSION@@|$VERSION|g" -e "s|@@RELEASE@@|$RELEASE|g" files/lsb-release.in > files/lsb-release
sed -e "s|@@VERSION@@|$VERSION|g" -e "s|@@RELEASE@@|$RELEASE|g" files/desktop-version.in > files/desktop-version

%install
%make_install

install -Dm644 %{SOURCE1} -t %{buildroot}%{_datadir}/deepin

# Remove Deepin distro's lsb-release
rm %{buildroot}/etc/lsb-release

# Don't override systemd timeouts
rm -r %{buildroot}/etc/systemd

# Make a symlink for deepin-version
ln -sv %{_datadir}/deepin/desktop-version %{buildroot}%{_sysconfdir}/deepin-version

# Install os-version and rename to uos-version
install -Dm644 files/os-version-amd %{buildroot}%{_sysconfdir}/dde-version

# Remove apt-specific templates
rm -r %{buildroot}%{_datadir}/python-apt

# Remove empty distro info directory
rm -r %{buildroot}%{_datadir}/distro-info

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/appstore.json
%{_sysconfdir}/deepin-version
%{_sysconfdir}/dde-version
%{_datadir}/deepin/
%{_datadir}/i18n/i18n_dependent.json
%{_datadir}/i18n/language_info.json
%{_datadir}/plymouth/deepin-logo.png

%changelog
%autochangelog
