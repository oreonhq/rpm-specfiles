%global source0_hash 44ea2a3af1050df0ac26ee8fb00cf8c7358ed98a900159b8756ee2c7979c34bc

Name:           spacenavd
Version:        1.3.1
Release:        3%{?dist}
Summary:        A free, compatible alternative for 3Dconnexion's input drivers

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://spacenav.sourceforge.net/
Source0:        https://github.com/FreeSpacenav/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Direct logs to systemd journal
Patch:          https://github.com/FreeSpacenav/spacenavd/commit/3c31924598630db24c5a972fcf53c8ddc0f3ad4a.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel

BuildRequires:  sed
BuildRequires:  systemd
%{?systemd_requires}

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

# Install systemd unit file
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 contrib/systemd/spacenavd.service %{buildroot}%{_unitdir}

%post
%systemd_post spacenavd.service

%preun
%systemd_preun spacenavd.service

%postun
%systemd_postun_with_restart spacenavd.service

%files
%doc AUTHORS doc/* README.md
%license COPYING
%{_bindir}/*
%{_unitdir}/%{name}.service

%changelog
%autochangelog
