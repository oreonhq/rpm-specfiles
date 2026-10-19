%global source0_hash d382aec04fa76299c8a7bbe4bfd7953a08e6edfc5c505cf7740c786a89becef6
%bcond_with tests
Name:           ansible-collection-community-rabbitmq
Version:        1.7.0
Release:        1%{?dist}
Summary:        RabbitMQ collection for Ansible
License:        GPL-3.0-or-later and PSF-2.0
URL:            %{ansible_collection_url community rabbitmq}
%global forgeurl https://github.com/ansible-collections/community.rabbitmq
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         build_ignore.patch
%if %{with tests}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  ansible-packaging
BuildRequires:  ansible-packaging-tests
BuildRequires:  glibc-all-langpacks
# /oreon:deps
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
%oreon_autofiles main
%if %{with tests}
%check

%ansible_test_unit
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
