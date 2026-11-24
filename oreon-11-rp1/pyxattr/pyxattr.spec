# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 68477027e6d3310669f98aaef15393bfcd9b2823d7a7f00a6f1d91a3c971ae64
%global source1_hash 4ad89609c7cfc1faf3ee60cf2c78560bf89d409ccad84ed96e0fce1faf663542
%global source2_hash 0cdba4240cac049e5fdd6cff8cf2785c9fb2d69563f414b3d57c1324c42215b1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           pyxattr
Summary:        Extended attributes library wrapper for Python
Version:        0.7.2
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://pyxattr.k1024.org/
Source0:        %{URL}/downloads/%{name}-%{version}.tar.gz
Source1:        %{URL}/downloads/%{name}-%{version}.tar.gz.asc
Source2:        https://k1024.org/files/key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  libattr-devel
BuildRequires:  python3-devel
BuildRequires:  gnupg2
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Python extension module wrapper for libattr. It allows to query, list,
add and remove extended attributes from files and directories.}

%description %_description

%package -n python3-%{name}
Summary: %{summary}

%description -n python3-%{name} %_description

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l xattr

%check
%pyproject_check_import

export TEST_IGNORE_XATTRS=security.selinux
export PYTHONPATH=%{buildroot}%{python3_sitearch}:$PYTHONPATH
python3 -m pytest tests %{?copr_projectname:-k 'not (binary_payload or create_on_existing or empty_value or large_value or many_ops or mixed_access or set_get_remove)'}

%files -n python3-%{name} -f %{pyproject_files}
%doc NEWS README.md

%changelog
%autochangelog
