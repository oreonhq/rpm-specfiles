%global source0_hash c871023a99423f8670a9693d03f72384cf09de905524cca3f8693cb27751bd3c

# For pre-release
%global git_tag %{version}

# Filter auto-generated deps from bundled shell script (which depends on busybox only)
%global __requires_exclude_from ^%{python3_sitelib}/gns3server/compute/docker/resources/.*$

Name:           gns3-server
Version:        2.2.57
Release:        1%{?dist}
Summary:        Graphical Network Simulator 3

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://gns3.com
Source0:        https://github.com/GNS3/gns3-server/archive/v%{git_tag}/%{name}-%{git_tag}.tar.gz
Source1:        gns3.service
Patch0:         0001-changing-busybox-udhcpc-script-path.patch
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?systemd_requires}
BuildRequires: systemd
BuildRequires: python3-sphinx
BuildRequires: make

Requires(post): edk2-ovmf
Recommends: docker busybox util-linux-script
Recommends: qemu-kvm swtpm
Requires: ubridge >= 0.9.14
Requires: cpulimit

%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple
workstations to powerful routers.

This is the server package which provides an HTTP REST API for the client (GUI).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
%description doc
%{name}-doc package contains documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n %{name}-%{git_tag}

# Relax requirements
sed -i -r 's/==/>=/g' requirements.txt
sed -i -r 's/distro>=1.9.*/distro>=1.5.0/' requirements.txt
sed -i -r 's/psutil>=7.2.1/psutil>=5.8.0/' requirements.txt
sed -i -r 's/aiofiles>=25.1.0,<26.0/aiofiles>=0.7/' requirements.txt
sed -i -r 's/aiohttp>=3.13.3,<3.14/aiohttp>=3.9.3/' requirements.txt
sed -i -r 's/aiohttp-cors>=0.8.1,<0.9/aiohttp-cors>=0.7.0/' requirements.txt
sed -i -r 's/Jinja2>=3.1.6,<3.2/jinja2>=2.11.3/' requirements.txt
sed -i -r 's/jsonschema>=4.25.1,<4.26/jsonschema>=3.2.0/' requirements.txt
sed -i -r 's/platformdirs>=2.4.0,<3/platformdirs>=2.4.0/' requirements.txt
sed -i -r 's/py-cpuinfo>=9.0.0,<10.0/py-cpuinfo>=8.0.0/' requirements.txt
sed -i -r "s/async-timeout>=5.0.1,<5.1/async-timeout>=4.0.2; python_version < '3.11'/" requirements.txt
sed -i -r 's/sentry-sdk.*//g' requirements.txt
sed -i -r 's/truststore.*//g' requirements.txt

# Create a sysusers.d config file
cat >gns3-server.sysusers.conf <<EOF
u gns3 - 'gns3 server' /var/lib/gns3 -
EOF

%build
%py3_build

%install
%py3_install

# Remove shebang
find %{buildroot}/%{python3_sitelib}/ -name '*.py' -print \
   -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} \;
# Remove empty file
rm -f %{buildroot}/%{python3_sitelib}/gns3server/symbols/.gitkeep

# Build the doc1834283s
%{make_build} -C docs html
/bin/rm -f docs/_build/html/.buildinfo

## Systemd service part
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
mkdir -p  %{buildroot}%{_sharedstatedir}/gns3

# Don't bundle OVMF_CODE.fd OVMF_VARS.fd with the package
rm -fv %{buildroot}/%{python3_sitelib}/gns3server/disks/OVMF_CODE.fd
rm -fv %{buildroot}/%{python3_sitelib}/gns3server/disks/OVMF_VARS.fd

%if 0%{?fedora} >= 42
install -m0644 -D gns3-server.sysusers.conf %{buildroot}%{_sysusersdir}/gns3-server.conf
%endif

%check

%files
%license LICENSE
%doc README.md AUTHORS CHANGELOG
%{python3_sitelib}/gns3_server*.egg-info/
%ghost %{python3_sitelib}/gns3server/disks/OVMF_CODE.fd
%ghost %{python3_sitelib}/gns3server/disks/OVMF_VARS.fd
%{python3_sitelib}/gns3server/
%{_bindir}/gns3server
%{_bindir}/gns3vmnet
%{_bindir}/gns3loopback
%{_unitdir}/gns3.service
%dir %attr(0755,gns3,gns3) %{_sharedstatedir}/gns3
%if 0%{?fedora} >= 42
%{_sysusersdir}/gns3-server.conf
%endif

%files doc
%license LICENSE
%doc docs/_build/html

%if 0%{?fedora} < 42
%pre
getent group gns3 >/dev/null || groupadd -r gns3
getent passwd gns3 >/dev/null || \
       useradd -r -g gns3 -d /var/lib/gns3 -s /sbin/nologin \
               -c "gns3 server" gns3
exit 0
%endif

%post
[ -d "/var/lib/gns3" ] && chown -R gns3:gns3 %{_sharedstatedir}/gns3
%systemd_post gns3.service

# Replace bundled OVMF_CODE.fd OVMF_VARS.fd with Fedora ones
cp -fp %{_datadir}/edk2/ovmf/OVMF_CODE.fd %{python3_sitelib}/gns3server/disks/OVMF_CODE.fd
cp -fp %{_datadir}/edk2/ovmf/OVMF_VARS.fd %{python3_sitelib}/gns3server/disks/OVMF_VARS.fd

%preun
%systemd_preun gns3.service

%postun
%systemd_postun_with_restart gns3.service

%changelog
%autochangelog
