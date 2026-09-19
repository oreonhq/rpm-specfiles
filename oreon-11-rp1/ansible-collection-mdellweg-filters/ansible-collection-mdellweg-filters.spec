%global source0_hash ffce4488a915c08b53fe419bc6e6a329a43173d54e939b8ed2cd63a061da6350

Name:           ansible-collection-mdellweg-filters
Version:        0.0.6
Release:        5%{?dist}
Summary:        An Ansible collection of random filters I missed at some point

License:        GPL-3.0-or-later
URL:            %{ansible_collection_url mdellweg filters}
Source:         https://github.com/mdellweg/ansible_filters/archive/v%{version}/mdwellweg.filters-%{version}.tar.gz
# build_ignore development files, tests, and docs
Patch:          build_ignore.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ansible_filters-%{version}

%build
%ansible_collection_build

%install
%ansible_collection_install

%check
echo 'localhost ansible_connection=local' >hosts.ini
export \
    ANSIBLE_COLLECTIONS_PATH=%{buildroot}%{ansible_collections_dir} \
    ANSIBLE_INVENTORY=hosts.ini
ansible-playbook $(find tests/playbooks/*.yaml -not -name 'jq.yaml')

%files -f %{ansible_collection_filelist}
%license LICENSE
%doc README.md

%changelog
%autochangelog
