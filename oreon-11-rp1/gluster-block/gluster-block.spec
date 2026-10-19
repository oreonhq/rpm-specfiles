%global source0_hash 60b7e97f36dc1ad8cceb38ce1de1489803cb16d892b67a1e858161dac4a2772d
Summary:        Gluster block storage utility
Name:             gluster-block
Version:          0.5
Release:        18%{?dist}
License:          GPL-2.0-only OR LGPL-3.0-or-later
URL:              https://github.com/gluster/gluster-block
Source0:        https://github.com/gluster/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:         tcmu-runner >= 1.1.3
Requires:         targetcli >= 2.1.fb49
Requires:         python3-rtslib >= 2.1.fb69
Requires:         rpcbind
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  git
BuildRequires:  help2man
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(glusterfs-api)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  rpcgen
BuildRequires:  systemd
# /oreon:deps
%description
gluster-block is a CLI utility, which aims at making gluster backed block
storage creation and maintenance as simple as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

echo %{version} > VERSION
./autogen.sh
%configure
%make_build
%install
%make_install
touch %{buildroot}%{_sharedstatedir}/gluster-block/gb_upgrade.status
%oreon_autofiles main

%post

%systemd_post gluster-block-target.service gluster-blockd.service
%preun

%systemd_preun gluster-block-target.service gluster-blockd.service
%postun

%systemd_postun_with_restart gluster-block-target.service gluster-blockd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
