%global source0_hash d382aec04fa76299c8a7bbe4bfd7953a08e6edfc5c505cf7740c786a89becef6

# ansible-core in RHEL 8.6 is built against python38. In c8s and the next RHEL
# 8 minor release, it will be built against python39. The testing dependencies
# are not yet packaged for either python version in EPEL 8.
#
# ansible-test in RHEL 9.0 still needs python3-mock, but this
# requirement has been removed in c9s.
# The conditional should be replaced with the line below once RHEL 9.1 is
# released.
# %%if (%%{defined fedora} || 0%%{?rhel} >= 9)
#
%if %{defined fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ansible-collection-community-rabbitmq
Version:        1.6.0
Release:        3%{?dist}
Summary:        RabbitMQ collection for Ansible

# plugins/module_utils/_version.py: Python Software Foundation License version 2
License:        GPL-3.0-or-later and PSF-2.0
URL:            %{ansible_collection_url community rabbitmq}
%global forgeurl https://github.com/ansible-collections/community.rabbitmq
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
# Patch galaxy.yml to exclude unnecessary files from the built collection.
# This is a downstream only patch.
Patch0:         build_ignore.patch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
# Collection specific test dependency
BuildRequires:  glibc-all-langpacks
%endif

BuildArch:      noarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n community.rabbitmq-%{version} -p1
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build
%ansible_collection_build

%install
%ansible_collection_install

%if %{with tests}
%check
%ansible_test_unit
%endif

%files -f %{ansible_collection_filelist}
%license COPYING PSF-license.txt
%doc README.md CHANGELOG.rst

%changelog
%autochangelog
