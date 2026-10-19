%global source0_hash edf25ee020a5263ffbef9eef5a8c14392bf74e78b3d5c8bc64d9343dd9a82605
Name: htop
Version: 3.5.3
Release:        1%{?dist}
Summary:        Interactive process viewer
License: GPL-2.0-or-later
URL: https://htop.dev/
Source0:        https://github.com/htop-dev/htop/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  hwloc-devel
BuildRequires:  libcap-devel
BuildRequires:  libnl3-devel
BuildRequires:  libtool
BuildRequires:  lm_sensors-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  python
# /oreon:deps
%description
htop is an interactive text-mode process viewer for Linux, similar to
top(1).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vfi
%configure \
	--enable-openvz \
	--enable-vserver \
	--enable-hwloc \
	--enable-unicode \
	--enable-sensors \
	--enable-delayacct \
	--enable-capabilities
%make_build
%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
