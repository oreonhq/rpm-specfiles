%global source0_hash 60557f93d091ac0b22717059b3b67986d2a2f34259e8111eea7ec38c043bd3e8

Name:           ansible-collection-containers-podman
Version:        1.16.3
Release:        10%{?dist}
Summary:        Podman Ansible collection for Podman containers

License:        GPL-3.0-or-later
URL:            %{ansible_collection_url containers podman}
Source:         https://github.com/containers/ansible-podman-collections/archive/%{version}.tar.gz

BuildRequires:  ansible-packaging

BuildArch:      noarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ansible-podman-collections-%{version}
sed -i -e 's/version:.*/version: %{version}/' galaxy.yml
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
rm -vr changelogs/ ci/ contrib/ tests/ ./galaxy.yml.in .github/ .gitignore docs/

%build
%ansible_collection_build

%install
%ansible_collection_install

%files -f %{ansible_collection_filelist}
%license COPYING
%doc README.md

%changelog
%autochangelog
