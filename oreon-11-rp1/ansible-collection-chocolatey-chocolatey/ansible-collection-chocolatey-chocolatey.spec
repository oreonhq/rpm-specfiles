%global source0_hash d157639c8c938443e390ce95bd4cc5c371b1aad6c986e18b7d50bde1713f39da

Name:           ansible-collection-chocolatey-chocolatey
Version:        1.5.3
Release:        5%{?dist}
Summary:        Ansible collection for Chocolatey

License:        GPL-3.0-or-later
URL:            %{ansible_collection_url chocolatey chocolatey}
Source:         https://github.com/chocolatey/chocolatey-ansible/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible-packaging

BuildArch:      noarch

%description
The collection includes the modules required to configure Chocolatey, as well
as manage packages on Windows using Chocolatey.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n chocolatey-ansible-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
sed -i -e 's/{{ REPLACE_VERSION }}/%{version}/' chocolatey/galaxy.yml
cat >> chocolatey/galaxy.yml << EOF
build_ignore:
  # Remove unnecessary development files from the built package.
  - tests
  - azure-pipelines.yml
  - .gitignore
  # Licenses and docs are installed with %%doc and %%license
  - LICENSE
  - README.md
EOF

%build
cd chocolatey
%ansible_collection_build

%install
cd chocolatey
%ansible_collection_install

# No unit tests

%files -f %{ansible_collection_filelist}
%license LICENSE
%doc README.md

%changelog
%autochangelog
