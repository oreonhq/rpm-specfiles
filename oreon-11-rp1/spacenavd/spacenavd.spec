%global source0_hash 44ea2a3af1050df0ac26ee8fb00cf8c7358ed98a900159b8756ee2c7979c34bc
Name:           spacenavd
Version:        1.3.1
Release:        1%{?dist}
Summary:        A free, compatible alternative for 3Dconnexion's input drivers
License:        GPL-3.0-or-later
URL:            http://spacenav.sourceforge.net/
Source0:        https://github.com/FreeSpacenav/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch:          https://github.com/FreeSpacenav/spacenavd/commit/3c31924598630db24c5a972fcf53c8ddc0f3ad4a.patch
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  systemd
# /oreon:deps
%description
Spacenavd, is a free software replacement user-space driver (daemon), for
3Dconnexion's space-something 6dof input devices. It's compatible with the
original 3dxsrv proprietary daemon provided by 3Dconnexion, and works
perfectly with any program that was written for the 3Dconnexion driver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i 's:/usr/local/bin:%{_bindir}:' contrib/systemd/spacenavd.service

%build

%configure
sed -i "s/CFLAGS =/CFLAGS +=/g" Makefile
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 contrib/systemd/spacenavd.service %{buildroot}%{_unitdir}
%oreon_autofiles main

%post

%systemd_post spacenavd.service
%preun

%systemd_preun spacenavd.service
%postun

%systemd_postun_with_restart spacenavd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
