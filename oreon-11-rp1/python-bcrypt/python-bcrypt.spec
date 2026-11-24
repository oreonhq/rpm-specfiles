# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3a3fd2204178b6d2adcf09cb4f6426ffef54762577a7c9b54c159008cb288c18
%global source1_hash 50e2b2197d20d04e01e33821ced9623a3d472470a2b9f3b2f74b21f489cb4bc0
%global source2_hash 4175ae75116d9e1da3169ffd4b8f76ef6a83c098aba728024e3b83566afd7af4
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global modname bcrypt
%global sum     Modern password hashing for your software and your servers

Name:               python-bcrypt
Version:            4.3.0
Release:        %{autorelease}
Summary:            %{sum}

License:            Apache-2.0 AND LicenseRef-Fedora-Public-Domain
URL:                https://pypi.python.org/pypi/bcrypt
Source0:            %pypi_source bcrypt
Source1:            bcrypt-%{version}-vendor.tar.xz
Source2:            bcrypt-%{version}-Cargo.lock

Patch:          python-bcrypt-4.3.0-pyo3.patch

%description
%{sum}.

%package -n python3-%{modname}
Summary:            %{sum}
License:            %{shrink:
    Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND
    BSD-3-Clause AND
    MIT AND
    (Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires:      cargo-rpm-macros

%description -n python3-%{modname}
%{sum}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%autosetup -n %{modname}-%{version} -p1
cp -f %{SOURCE2} src/_bcrypt/Cargo.lock
tar -C src/_bcrypt -xf %{SOURCE1}
mkdir -p src/_bcrypt/.cargo
cat > src/_bcrypt/.cargo/config.toml << 'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
export RUSTFLAGS="%build_rustflags --cfg pyo3_unsafe_allow_subinterpreters"
export CARGO_NET_OFFLINE=true
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l bcrypt

%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
