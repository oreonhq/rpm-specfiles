# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6ddcac2a081f8b7b9642c09406bc6a4290128fce5f471cddd165960bb9119e5c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pypi_name protobuf
%global pypi_version 6.33.5

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %{autorelease}
Summary:        Protocol Buffers

License:        BSD-3-Clause
URL:            https://protobuf.dev
Source0:        %{pypi_source}

Patch:          protobuf-unbundle-upb-and-utf8_range.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  protobuf-devel = %{pypi_version}
BuildRequires:  upb-static = %{pypi_version}

%description
Protocol buffers are Google's language-neutral,
platform-neutral, extensible mechanism for serializing
structured data – think XML, but smaller, faster, and
simpler. You define how you want your data to be
structured once, then you can use special generated
source code to easily write and read your structured
data to and from a variety of data streams and using
a variety of languages.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Conflicts:      python3-%{pypi_name} < 4~~

%description -n python3-%{pypi_name}
Protocol buffers are Google's language-neutral,
platform-neutral, extensible mechanism for serializing
structured data – think XML, but smaller, faster, and
simpler. You define how you want your data to be
structured once, then you can use special generated
source code to easily write and read your structured
data to and from a variety of data streams and using
a variety of languages.

%prep
%oreon_sha256
%autosetup -p1 -n %{pypi_name}-%{pypi_version}
rm -rf %{pypi_name}.egg-info
rm -rf upb utf8_range

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l google

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
