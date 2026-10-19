%global source0_hash 89a5ac0e98cfae6aad26d00e0e977affe810865ebccd4c4cf9422f980ade5624
Name:		  lxcfs
Version:	  7.0.0
Release:        1%{?dist}
Summary:        FUSE based filesystem for LXC
License:	  Apache-2.0
URL:		  https://linuxcontainers.org/lxcfs
Source0:        https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz
Requires(post):	  systemd
Requires(preun):  systemd
Requires(postun): systemd
Requires:	  lxc-templates
# oreon:deps
BuildRequires:  fuse3-devel
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  python3-jinja2
BuildRequires:  systemd
# /oreon:deps
%description
LXCFS is a small FUSE filesystem written with the intention of making
Linux containers feel more like a virtual machine. It started as a
side-project of LXC but is usable by any runtime.

LXCFS will take care that the information provided by crucial files in
procfs are container aware such that the values displayed (e.g. in
/proc/uptime) really reflect how long the container is running and not
how long the host is running.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
