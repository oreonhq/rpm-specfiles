%global source0_hash none

Name:           nvmetcli
License:        Apache-2.0
Summary:        An adminstration shell for NVMe storage targets
Version:        0.8
Release:        7%{?dist}
URL:            https://ftp.infradead.org/pub/nvmetcli/
Source:         https://ftp.infradead.org/pub/nvmetcli/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  python3-devel python3-setuptools systemd-units asciidoc xmlto
Requires:       python3-configshell python3-kmod python3-six
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%define _sbindir %{_exec_prefix}/sbin

%description
This package contains the command line interface to the NVMe over Fabrics
nvmet in the Linux kernel.  It allows configuring the nvmet interactively
as well as saving / restoring the configuration to / from a json file.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

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

%post
%systemd_post nvmet.service

%preun
%systemd_preun nvmet.service

%postun
%systemd_postun_with_restart nvmet.service

%files
%{python3_sitelib}/*
%dir %{_sysconfdir}/nvmet
%{_sbindir}/nvmetcli
%{_unitdir}/nvmet.service
%doc README
%license COPYING
%{_mandir}/man8/nvmetcli.8.gz

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8-7
- Import
