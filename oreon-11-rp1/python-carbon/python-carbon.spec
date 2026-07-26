%global source0_hash 1916df4d51f4260baee0d0665aae8c75e3350f0fcb826e26514c0abfe2d74f15

%global srcname carbon

%global desc %{expand: \
Carbon is one of the components of Graphite, and is responsible for
receiving metrics over the network and writing them down to disk using
a storage back-end.}

Name:           python-%{srcname}
Version:        1.1.10
Release:        17%{?dist}

Summary:        Back-end data caching and persistence daemon for Graphite
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/graphite-project/carbon

Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

Source10:       carbon-aggregator.1
Source11:       carbon-cache.1
Source13:       carbon-relay.1
Source14:       validate-storage-schemas.1
Source20:       %{name}.logrotate

Source30:       carbon-aggregator.service
Source31:       carbon-cache.service
Source32:       carbon-relay.service
Source33:       carbon-aggregator@.service
Source34:       carbon-cache@.service
Source35:       carbon-relay@.service

Source43:       %{name}.sysconfig

# Set sane default filesystem paths.
Patch1:         %{name}-0.10.0-Set-sane-defaults.patch
# Fix path to storage-schemas.conf.
Patch2:         %{name}-0.9.13-Fix-path-to-storage-schemas.conf.patch
# Python 3.12 support https://github.com/graphite-project/carbon/issues/946
Patch3:         %{name}-1.1.10-Py3.12-support.patch

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-protobuf
BuildRequires:	python3-whisper
BuildRequires:	pyproject-rpm-macros
BuildRequires:	systemd
%py_provides python3-%{pypi_name}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:	logrotate
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# ugly prefix hack..
export GRAPHITE_NO_PREFIX=True
sed -i -e '/data_files=install_files,/d' setup.py
cat << EOF >> setup.cfg
[install]
install-lib=
EOF

# txAMQP is orphaned in 2020
sed -i "s/, 'txAMQP'//" setup.py
sed -i '/txAMQP/d' requirements.txt
# shebangs shebang..
sed -i '1s|^#!/usr/bin/env python|#!/usr/bin/python3|' lib/carbon/amqp_listener.py
sed -i '1s|^#!/usr/bin/env python|#!/usr/bin/python3|' lib/carbon/amqp_publisher.py
# disable tests which use mmh3 hash
sed -i "s|plugin == 'rules'|plugin == 'rules' or plugin.startswith('fast-')|" lib/carbon/tests/test_routers.py
# Disable internal log rotation.
sed -i -e 's/ENABLE_LOGROTATION.*/ENABLE_LOGROTATION = False/g' conf/carbon.conf.example
# Skip Ceres database test, not actively maintained
rm lib/carbon/tests/test_database.py

# Use the standard library instead of a backport
sed -i -e 's/^import mock/from unittest import mock/' \
       -e 's/^from mock import /from unittest.mock import /' \
    lib/carbon/tests/*.py

%generate_buildrequires
%pyproject_buildrequires -r

# Create a sysusers.d config file
cat >python-carbon.sysusers.conf <<EOF
u carbon - 'Carbon cache daemon' %{_localstatedir}/lib/carbon -
EOF

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname} twisted

rm -rf %{buildroot}%{_localstatedir}/lib/carbon/*
mkdir -p %{buildroot}%{_localstatedir}/lib/carbon/lists
mkdir -p %{buildroot}%{_localstatedir}/lib/carbon/rrd
mkdir -p %{buildroot}%{_localstatedir}/lib/carbon/whisper

# default config
mkdir -p %{buildroot}%{_sysconfdir}/carbon
install -D -p -m0644 conf/carbon.conf.example \
    %{buildroot}%{_sysconfdir}/carbon/carbon.conf
install -D -p -m0644 conf/storage-aggregation.conf.example \
    %{buildroot}%{_sysconfdir}/carbon/storage-aggregation.conf
install -D -p -m0644 conf/storage-schemas.conf.example \
    %{buildroot}%{_sysconfdir}/carbon/storage-schemas.conf

# man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE10} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE11} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE13} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE14} %{buildroot}%{_mandir}/man1

# log files
mkdir -p %{buildroot}%{_localstatedir}/log/carbon
install -D -p -m0644 %{SOURCE20} \
    %{buildroot}%{_sysconfdir}/logrotate.d/python3-%{srcname}

# init scripts
install -D -p -m0644 %{SOURCE30} \
    %{buildroot}%{_unitdir}/carbon-aggregator.service
install -D -p -m0644 %{SOURCE31} \
    %{buildroot}%{_unitdir}/carbon-cache.service
install -D -p -m0644 %{SOURCE32} \
    %{buildroot}%{_unitdir}/carbon-relay.service
install -D -p -m0644 %{SOURCE33} \
    %{buildroot}%{_unitdir}/carbon-aggregator@.service
install -D -p -m0644 %{SOURCE34} \
    %{buildroot}%{_unitdir}/carbon-cache@.service
install -D -p -m0644 %{SOURCE35} \
    %{buildroot}%{_unitdir}/carbon-relay@.service

# remove .py suffix
for i in %{buildroot}%{_bindir}/*.py; do
    mv ${i} ${i%%.py}
done

# fix permissions
chmod 755 %{buildroot}%{python3_sitelib}/carbon/amqp_listener.py
chmod 755 %{buildroot}%{python3_sitelib}/carbon/amqp_publisher.py

install -m0644 -D python-carbon.sysusers.conf %{buildroot}%{_sysusersdir}/python-carbon.conf

%post -n python3-%{srcname}
%systemd_post carbon-aggregator.service
%systemd_post carbon-cache.service
%systemd_post carbon-relay.service

%preun -n python3-%{srcname}
%systemd_preun carbon-aggregator.service
%systemd_preun carbon-cache.service
%systemd_preun carbon-relay.service

%postun -n python3-%{srcname}
%systemd_postun_with_restart carbon-aggregator.service
%systemd_postun_with_restart carbon-cache.service
%systemd_postun_with_restart carbon-relay.service

%check
%pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%doc conf/ examples/ distro/redhat/init.d/

%dir %{_sysconfdir}/carbon
%config(noreplace) %{_sysconfdir}/carbon/carbon.conf
%config(noreplace) %{_sysconfdir}/carbon/storage-aggregation.conf
%config(noreplace) %{_sysconfdir}/carbon/storage-schemas.conf

%config(noreplace) %{_sysconfdir}/logrotate.d/python3-%{srcname}

%attr(0755,carbon,carbon) %dir %{_localstatedir}/lib/carbon
%attr(0755,carbon,carbon) %dir %{_localstatedir}/lib/carbon/lists
%attr(0755,carbon,carbon) %dir %{_localstatedir}/lib/carbon/rrd
%attr(0755,carbon,carbon) %dir %{_localstatedir}/lib/carbon/whisper
%attr(0755,carbon,carbon) %dir %{_localstatedir}/log/carbon

%{_bindir}/carbon-aggregator
%{_bindir}/carbon-aggregator-cache
%{_bindir}/carbon-cache
%{_bindir}/carbon-relay
%{_bindir}/validate-storage-schemas

%{_mandir}/man1/carbon-aggregator.1*
%{_mandir}/man1/carbon-cache.1*
%{_mandir}/man1/carbon-relay.1*
%{_mandir}/man1/validate-storage-schemas.1*

%{_unitdir}/carbon-aggregator.service
%{_unitdir}/carbon-cache.service
%{_unitdir}/carbon-relay.service
%{_unitdir}/carbon-aggregator@.service
%{_unitdir}/carbon-cache@.service
%{_unitdir}/carbon-relay@.service
%{_sysusersdir}/python-carbon.conf

%changelog
%autochangelog
