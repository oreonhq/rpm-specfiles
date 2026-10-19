%global source0_hash b836a0eb9dd5efa34c330b8e6d078cead0debceea0a00354cb4d63d223fe29b7
%global collection_namespace community
%global collection_name libvirt
%bcond_with        tests
Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        2.3.0
Release:        1%{?dist}
Summary:        Manages virtual machines supported by libvirt
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url}
Source0:        https://github.com/ansible-collections/community.libvirt/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ansible-core
BuildRequires:  ansible-packaging
BuildRequires:  ansible-packaging-tests
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-langpack-en
BuildRequires:  python3-devel
# /oreon:deps
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
%oreon_autofiles main

%check

%if %{with tests}
%ansible_test_unit
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
