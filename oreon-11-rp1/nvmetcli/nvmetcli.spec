%global source0_hash 51d6d7e2c5ed43c7e9528abff539b6a213c5469c6800af901e88ef254ce3ac16
Name:           nvmetcli
License:        Apache-2.0
Summary:        An adminstration shell for NVMe storage targets
Version:        0.8
Release:        7%{?dist}
URL:            https://ftp.infradead.org/pub/nvmetcli/
Source0:        https://github.com/hreinecke/nvmetcli/archive/refs/heads/master.tar.gz#/nvmetcli-0.8.tar.gz
BuildArch:      noarch
Requires:       python3-configshell python3-kmod python3-six
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%define _sbindir %{_exec_prefix}/sbin
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-units
BuildRequires:  xmlto
# /oreon:deps
%description
This package contains the command line interface to the NVMe over Fabrics
nvmet in the Linux kernel.  It allows configuring the nvmet interactively
as well as saving / restoring the configuration to / from a json file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir nvmetcli-master
%oreon_prep
%build

%{__python3} setup.py build
cd Documentation
make
gzip --stdout nvmetcli.8 > nvmetcli.8.gz
%install
%{__python3} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/nvmet
install -m 644 nvmet.service %{buildroot}%{_unitdir}/nvmet.service
mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 Documentation/nvmetcli.8.gz %{buildroot}%{_mandir}/man8/
%oreon_autofiles main

%post

%systemd_post nvmet.service
%preun

%systemd_preun nvmet.service
%postun

%systemd_postun_with_restart nvmet.service
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8-7
- Import
