%global source0_hash b54de378b6524fc3c59334b9089aa583d8b373488141fad025d88a7e0f80391f

Name:             ansible-pcp
Version:          2.4.2
Release:          3%{?dist}
Summary:          Ansible Metric collection for Performance Co-Pilot
License:          MIT
URL:              https://github.com/performancecopilot/ansible-pcp
Source:        https://github.com/performancecopilot/ansible-pcp/archive/v2.4.2/ansible-pcp-2.4.2.tar.gz
BuildArch:        noarch

%if %{defined rhel}
%global collection_namespace redhat
%global collection_name rhel_metrics
%global ansible_collection_files %{_datadir}/ansible/collections/ansible_collections/%{collection_namespace}
%else
%global collection_namespace performancecopilot
%global collection_name metrics
%endif

%if 0%{?rhel} >= 8
Requires: (ansible-core >= 2.11.0 or ansible >= 2.9.0)
%endif

%if 0%{?rhel} >= 9
BuildRequires:  ansible-core
%global ansible_collection_build ansible-galaxy collection build .
%global ansible_collection_install ansible-galaxy collection install -n -p %{buildroot}%{_datadir}/ansible/collections %{collection_namespace}-%{collection_name}-%{version}.tar.gz
%endif

%if %{defined fedora}
BuildRequires:  ansible-packaging
BuildRequires:  ansible-packaging-tests
# There's ansible-lint errors that need to be addressed
# BuildRequires: python3-ansible-lint
%endif

%description
A collection containing roles for Performance Co-Pilot (PCP) and related
software such as Grafana and Valkey.

The collection is made up of several Ansible roles, including:

%{collection_namespace}.%{collection_name}.pcp
A role for core PCP capabilities, configuring live performance analysis
with a large base set of metrics from the kernel and system services, as
well as data recording and rule inference.

%{collection_namespace}.%{collection_name}.keyserver
A role for configuring a local key server (Valkey/Redis), suitable for
use with a Performance Co-Pilot archive repository (for single or many
hosts) and fast, scalable querying of metrics.

%{collection_namespace}.%{collection_name}.grafana
A role for configuring a local Grafana server, providing web frontend
visuals for Performance Co-Pilot metrics, both live and historically.
Data sources for Vector (live), Valkey (historical) and interactive
bpftrace (eBPF) scripts can be configured by this role.  The PCP REST
API service (from the core pcp role) should be configured in order to
use this role.

%{collection_namespace}.%{collection_name}.bpftrace
A role that extends the core PCP role, providing metrics from bpftrace
scripts using Linux eBPF facilities.  Configuring authentication of a
local user capable of running bpftrace scripts via the PCP agent is a
key task of this role.

%{collection_namespace}.%{collection_name}.elasticsearch
A role that extends the core PCP role, providing metrics from a live
ElasticSearch instance for PCP analysis or exporting of PCP metric
values (and metadata) to ElasticSearch for the indexing and querying
of performance data.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
%if 0%{?rhel}
rm -vr roles/repository tests/*repository* tests/*/*repository* docs/repository
%endif
sed -i \
    -e 's/^name: .*/name: %{collection_name}/g' \
    -e 's/^namespace: .*/namespace: %{collection_namespace}/g' \
    galaxy.yml
find . -name \*.yml -o -name \*.md | while read file; do
    sed -i \
        -e 's/performancecopilot.metrics/%{collection_namespace}.%{collection_name}/g' \
    $file
done

%build
# NOTE: Even though ansible-core is in 8.6, it is only available
# at *runtime*, not at *buildtime* - so we can't have
# ansible-core as a build_dep on RHEL8
%if %{defined rhel} && 0%{?rhel} <= 8
tar -cf %{_tmppath}/%{collection_namespace}-%{collection_name}-%{version}.tar.gz .
%else
%ansible_collection_build
%endif

%install
%if %{defined rhel} && 0%{?rhel} <= 8
mkdir -p %{buildroot}%{ansible_collection_files}/%{collection_name}
cd %{buildroot}%{ansible_collection_files}/%{collection_name}
tar -xf %{_tmppath}/%{collection_namespace}-%{collection_name}-%{version}.tar.gz
%else
%ansible_collection_install
%endif

%check
# There's outstanding ansible-lint failures that need to be addressed.
# %%if %%{defined fedora}
%if 0
ansible-lint `find roles -name \*.yml`
%endif

%files
%doc README.md
%license LICENSE
%{ansible_collection_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.2-3
- Prepare for Oreon 11 (RP1)
