%global source0_hash d01a2d2ed78ddea793abb06d5dd572c038d2efdd239c97208f5e584cd80bd088
%global _deepin_version 25
Name:           deepin-desktop-base
Version:        2026.09.04
Release:        1%{?dist}
Summary:        Base component for Deepin
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-desktop-base
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        distribution.info
BuildArch:      noarch
Requires:       fedora-logos
# oreon:deps
BuildRequires:  make
# /oreon:deps
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
rm %{buildroot}/etc/lsb-release
rm -r %{buildroot}/etc/systemd
ln -sv %{_datadir}/deepin/desktop-version %{buildroot}%{_sysconfdir}/deepin-version
install -Dm644 files/os-version-amd %{buildroot}%{_sysconfdir}/dde-version
rm -r %{buildroot}%{_datadir}/python-apt
rm -r %{buildroot}%{_datadir}/distro-info
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
