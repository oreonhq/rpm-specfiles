%global source3_hash 7d69c1cd2baa011e39bd7550bf58087b081807985334aa8ce0270531a7e5ea24
%global source1_hash e9cf240c9c020399da5b87a9f696a8ecb038fbcd49b366dd16c1a4f316a14e5d
%global source0_hash 441f36715e5fed477ceb5fd8ed9ac6ebad2a6041aad90e7af0498a2a35965770
%bcond tests %{undefined rhel}
Name:           ansible-collection-dellemc-openmanage
Version:        10.0.3
Release:        1%{?dist}
Summary:        Dell OpenManage collection for Ansible
License:        GPL-3.0-only AND BSD-2-Clause
URL:            %{ansible_collection_url dellemc openmanage}
Source0:        https://github.com/dell/dellemc-openmanage-ansible-modules/releases/download/v%{version}/dellemc-openmanage-%{version}.tar.gz
Source1:        https://github.com/dell/dellemc-openmanage-ansible-modules/releases/download/v%{version}/dellemc-openmanage-%{version}.tar.gz.sign
Source2:        gpgkey-42550ABD1E80D7C1BC0BAD851285491434D8786F.gpg
Source3:        https://raw.githubusercontent.com/dell/dellemc-openmanage-ansible-modules/v%{version}/galaxy.yml
Patch0:          build_ignore.patch
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       xorriso
Requires:       syslinux
Requires:       isomd5sum
Requires:       wget
Requires:       python3dist(omsdk)
Requires:       python3dist(netaddr)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ansible-collection-dellemc-openmanage = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -N -c -n dellemc-openmanage-%{version}
cp '%{SOURCE3}' galaxy.yml
%autopatch -p1

# Remove shebangs on non-executable files
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

# Remove empty files
find . -type f -empty ! -name __init__.py -print -delete

%if %{with tests}
%build

%ansible_collection_build
%install
%ansible_collection_install
%oreon_autofiles main

%check

%if %{with tests}
%ansible_test_unit
%endif
%files

%changelog

%autochangelog
%endif
