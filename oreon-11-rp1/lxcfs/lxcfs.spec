%global source0_hash 386339ba4cde289b0f6df4fe7a614caa1e45dd91bc0200b4aff6c51bf9d5ef9e

Name:		  lxcfs
Version:	  6.0.6
Release:	  1%{?dist}
Summary:	  FUSE based filesystem for LXC
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	  Apache-2.0
URL:		  https://linuxcontainers.org/lxcfs
Source:		  https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	  meson
BuildRequires:	  gcc
BuildRequires:	  python3-jinja2
BuildRequires:	  gawk
BuildRequires:	  make
BuildRequires:	  fuse3-devel
BuildRequires:	  help2man
BuildRequires:	  systemd
Requires(post):	  systemd
Requires(preun):  systemd
Requires(postun): systemd
# for /usr/share/lxc/config/common.conf.d:
Requires:	  lxc-templates

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

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%doc AUTHORS
# empty:
#doc ChangeLog NEWS README
%license COPYING
%{_bindir}/lxcfs
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lxc.mount.hook
%{_datadir}/%{name}/lxc.reboot.hook
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}.service
%{_datadir}/lxc/config/common.conf.d/00-lxcfs.conf
%dir %{_sharedstatedir}/%{name}

%changelog
%autochangelog
