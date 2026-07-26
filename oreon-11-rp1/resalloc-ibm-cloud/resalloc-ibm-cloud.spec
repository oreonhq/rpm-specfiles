%global source0_hash ed661ea2c0ce1bd31906c2f2a5ca293255a8e9d5e5cf78cacfc844bca37c9325

%global desc %{expand:
Helper scripts for the Resalloc server (mostly used by Copr build system)
for maintaining VMs in IBM Cloud (starting, stopping, cleaning orphans, etc.).
}

Name:           resalloc-ibm-cloud
Version:        3.4
Release:        2%{?dist}
Summary:        Resource allocator scripts for IBM cloud

License:        GPL-2.0-or-later
URL:            https://github.com/fedora-copr/%{name}
Source0:        %{url}/archive/refs/tags/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       resalloc-helpers
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files resalloc_ibm_cloud

%files -n %{name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%_mandir/man1/resalloc-ibm-cloud*1*
%{_bindir}/resalloc-ibm-cloud-list-deleting-vms
%{_bindir}/resalloc-ibm-cloud-list-deleting-volumes
%{_bindir}/resalloc-ibm-cloud-list-vms
%{_bindir}/resalloc-ibm-cloud-vm
%{_bindir}/resalloc-ibm-cloud-powervs-list-deleting-vms
%{_bindir}/resalloc-ibm-cloud-powervs-list-vms
%{_bindir}/resalloc-ibm-cloud-powervs-vm

%changelog
%autochangelog
