%global source0_hash a5176dbd2d20cc749568a5f41949bc6549926b55ba3985e72d1bbfc4f5c539d8

%global collection_namespace community
%global collection_name kubernetes

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        2.0.1
Release:        14%{?dist}
Summary:        Kubernetes Collection for Ansible

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/community.kubernetes/archive/%{version}/%{name}-%{version}.tar.gz

# See message in %%description.
Provides:       deprecated()

BuildRequires:  ansible-packaging

BuildArch:      noarch

%description
%{summary}.
This collection has been deprecated in favor of
ansible-collection-kubernetes-core. Users should change their collection names
from `community.kubernetes.X` to `kubernetes.core.X` and replace this package
with ansible-collection-kubernetes-core.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{collection_namespace}.%{collection_name}-%{version}
rm -vr .github .yamllint codecov.yml setup.cfg
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
find -type f -name '.gitignore' -print -delete

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license LICENSE
%doc README.md CHANGELOG.rst
%{ansible_collection_files}

%changelog
%autochangelog
