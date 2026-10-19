%global source0_hash 16274a4102426871cad84ad07db41f82aa8f4d43d95e5947a62e199c2df775c6
%bcond_without tests
Name:           cloud-init
Version:        26.2
Release:        1%{?dist}
Summary:        Cloud instance init scripts
License:        Apache-2.0 OR GPL-3.0-only
URL:            https://github.com/canonical/cloud-init
Source0:        https://github.com/canonical/cloud-init/archive/refs/tags/26.2.tar.gz#/cloud-init-25.3.tar.gz
Source1:        cloud-init-tmpfiles.conf
Patch:          0001-fix-avoid-dependency-cycle-on-Fedora.patch
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       dhcpcd
Requires:       hostname
Requires:       e2fsprogs
Requires:       iproute
Requires:       python3-libselinux
Requires:       %{py3_dist configobj}
Requires:       %{py3_dist jinja2}
Requires:       %{py3_dist jsonpatch}
Requires:       %{py3_dist jsonschema}
Requires:       %{py3_dist oauthlib}
Requires:       %{py3_dist pyyaml}
Requires:       %{py3_dist requests}
Requires:       policycoreutils-python3
Requires:       procps
Requires:       shadow-utils
Requires:       util-linux
Requires:       xfsprogs
Requires:       openssl
Requires:       /usr/bin/nc
%{?systemd_requires}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cloud-init = %{version}-%{release}
# /oreon:deps
%description
Cloud-init is a set of init scripts for cloud instances.  Cloud instances
need special scripts to run during initialization to retrieve and install
ssh keys and to let the user run various scripts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Removing shebang manually because of rpmlint, will update upstream later
sed -i -e 's|#!/usr/bin/python||' cloudinit/cmd/main.py

# Use unittest from the standard library. unittest2 is old and being
# retired in Fedora. See https://bugzilla.redhat.com/show_bug.cgi?id=1794222
find tests/ -type f | xargs sed -i s/unittest2/unittest/
find tests/ -type f | xargs sed -i s/assertItemsEqual/assertCountEqual/

%build

%meson_build
%install
%meson_install
%py3_shebang_fix %{buildroot}%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/var/lib/cloud
mkdir -p $RPM_BUILD_ROOT/run/cloud-init
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d
cp -p tools/21-cloudinit.conf $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d/21-cloudinit.conf
%oreon_autofiles main

%check

%if %{with tests}
%py3_check_import cloudinit
%meson test -C builddir -v
%else
%py3_check_import cloudinit
%endif
%post

%systemd_post cloud-config.service cloud-config.target cloud-final.service cloud-init-main.service cloud-init.target cloud-init-local.service cloud-init-network.service
%preun

%systemd_preun cloud-config.service cloud-config.target cloud-final.service cloud-init-main.service cloud-init.target cloud-init-local.service cloud-init-network.service
%postun

%systemd_postun cloud-config.service cloud-config.target cloud-final.service cloud-init-main.service cloud-init.target cloud-init-local.service cloud-init-network.service
%files

%changelog

%autochangelog
