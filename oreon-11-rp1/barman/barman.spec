%global source0_hash 568418ccc5a1b6fdbddb1f916afa3590c78b836c966ab76b1afcf44d247a58e1
Name:       barman
Version:    3.20.1
Release:        1%{?dist}
Summary:        Backup and Recovery Manager for PostgreSQL
License:    GPL-3.0-only
URL:        http://www.pgbarman.org/
BuildArch:  noarch
Source0:        https://github.com/EnterpriseDB/barman/archive/release/%{version}/%{name}-release-%{version}.tar.gz
Source1:    %{name}.cron
Source2:    %{name}.logrotate
Requires:       cronie
Requires:       logrotate
Requires:       rsync >= 3.0.4
Requires:       %{py3_dist argcomplete}
Requires:       %{py3_dist barman}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv_build) < 0.13
BuildRequires:  python3dist(uv_build) >= 0.11.17
Requires:       python3-barman = %{version}-%{release}
# /oreon:deps
%package -n       python3-barman+argcomplete
Summary:        Metapackage for python3-barman argcomplete extras
Requires:       python3-barman = %{version}-%{release}
Provides:       python3dist(barman[argcomplete]) = %{version}-%{release}

%description -n python3-barman+argcomplete
Metapackage for python3-barman argcomplete extras.

%package -n       python3-barman+aws-snapshots
Summary:        Metapackage for python3-barman aws-snapshots extras
Requires:       python3-barman = %{version}-%{release}
Provides:       python3dist(barman[aws-snapshots]) = %{version}-%{release}

%description -n python3-barman+aws-snapshots
Metapackage for python3-barman aws-snapshots extras.

%package -n       python3-barman+azure
Summary:        Metapackage for python3-barman azure extras
Requires:       python3-barman = %{version}-%{release}
Provides:       python3dist(barman[azure]) = %{version}-%{release}

%description -n python3-barman+azure
Metapackage for python3-barman azure extras.

%package -n       python3-barman+azure-snapshots
Summary:        Metapackage for python3-barman azure-snapshots extras
Requires:       python3-barman = %{version}-%{release}
Requires:       python3dist(azure-mgmt-compute) >= 38.0.0
Provides:       python3dist(barman[azure-snapshots]) = %{version}-%{release}

%description -n python3-barman+azure-snapshots
Metapackage for python3-barman azure-snapshots extras.

%package -n       python3-barman+cloud
Summary:        Metapackage for python3-barman cloud extras
Requires:       python3-barman = %{version}-%{release}
Provides:       python3dist(barman[cloud]) = %{version}-%{release}

%description -n python3-barman+cloud
Metapackage for python3-barman cloud extras.

%package -n       python3-barman+google
Summary:        Metapackage for python3-barman google extras
Requires:       python3-barman = %{version}-%{release}
Requires:       python3dist(google-cloud-storage) >= 3.12
Requires:       python3dist(google-cloud-storage) < 3.14
Provides:       python3dist(barman[google]) = %{version}-%{release}

%description -n python3-barman+google
Metapackage for python3-barman google extras.

%package -n       python3-barman+google-snapshots
Summary:        Metapackage for python3-barman google-snapshots extras
Requires:       python3-barman = %{version}-%{release}
Provides:       python3dist(barman[google-snapshots]) = %{version}-%{release}

%description -n python3-barman+google-snapshots
Metapackage for python3-barman google-snapshots extras.

%package -n       python3-barman+snappy
Summary:        Metapackage for python3-barman snappy extras
Requires:       python3-barman = %{version}-%{release}
Requires:       python3dist(cramjam) >= 2.7.0
Provides:       python3dist(barman[snappy]) = %{version}-%{release}

%description -n python3-barman+snappy
Metapackage for python3-barman snappy extras.

%package -n       python3-barman+zstandard
Summary:        Metapackage for python3-barman zstandard extras
Requires:       python3-barman = %{version}-%{release}
Provides:       python3dist(barman[zstandard]) = %{version}-%{release}

%description -n python3-barman+zstandard
Metapackage for python3-barman zstandard extras.

%package -n       python3-barman+lz4
Summary:        Metapackage for python3-barman lz4 extras
Requires:       python3-barman = %{version}-%{release}
Provides:       python3dist(barman[lz4]) = %{version}-%{release}

%description -n python3-barman+lz4
Metapackage for python3-barman lz4 extras.

%description
Barman (Backup and Recovery Manager) is an open-source administration tool for
disaster recovery of PostgreSQL servers written in Python.

It allows your organization to perform remote backups of multiple servers in
business critical environments to reduce risk and help DBAs during the recovery
phase.

%package cli
Summary:    Client Utilities for Barman
Requires:   %{py3_dist barman}
%description cli
Client utilities for the integration of Barman in PostgreSQL clusters.

%package -n python3-barman
Summary:    Shared libraries for Barman
%{?python_provide:%python_provide python3-%{name}}
# oreon:reqs
Requires:       python3dist(psycopg2) >= 2.4.2
# /oreon:reqs
%description -n python3-barman
Python libraries used by Barman.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-release-%{version}

# Change shebang in all relevant executable files in this directory and all subdirectories
find -type f -executable -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -p -m 644 docs/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -p -m 644 docs/%{name}.d/* %{buildroot}%{_sysconfdir}/%{name}/conf.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -p -m 644 scripts/%{name}.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}
sed -i 's|/etc/%{name}.d|/etc/%{name}/conf.d|g' %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -m0644 -D barman.sysusers.conf %{buildroot}%{_sysusersdir}/barman.conf
%oreon_autofiles barman-cli usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-barman usr/lib/python3*/site-packages/barman* usr/lib64/python3*/site-packages/barman* usr/bin/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/barman* usr/lib64/python3*/site-packages/barman* usr/bin/*

%files
%files -n barman-cli -f %{oreon_filedir}/barman-cli.list
%files -n python3-barman -f %{oreon_filedir}/python3-barman.list

%changelog

%autochangelog
