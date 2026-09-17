%global source0_hash c22c2016b32f6c6b0f47a82c166d5aca47f29877b2fb31027d3dda74f99756a6

%global collection_namespace community
%global collection_name libvirt

# Only run tests where test deps are available
%if 0%{?fedora} || 0%{?rhel} >= 9
%bcond_without     tests
%else
%bcond_with        tests
%endif

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Manages virtual machines supported by libvirt
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/community.libvirt/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  ansible-packaging
# The new ansible-core, specifically, is required for the 'build_ignore:' patch
# and ansible-test to work properly; hence we cannot rely on ansible-packaging,
# which might pull in ansible 2.9
BuildRequires:  ansible-core
BuildRequires:  coreutils
BuildRequires:  findutils
%if %{with tests}
BuildRequires:  glibc-langpack-en
Buildrequires:  python3-devel
BuildRequires:  ansible-packaging-tests
%endif

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n community.libvirt-%{version}

# Exclude some files from being installed
cat << 'EOF' >> galaxy.yml
build_ignore:
- .azure-pipelines
- .github
- .gitignore
- .package_note-%{name}*
- .pyproject-builddir
- changelogs/fragments/.keep
- tests
EOF

# Drop shellbangs from python files
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build
%ansible_collection_build

%install
%ansible_collection_install

%check
%if %{with tests}
%ansible_test_unit
%endif

%files
%license COPYING
%doc CHANGELOG.rst CONTRIBUTING.md README.md
%{ansible_collection_files}

%changelog
%autochangelog
