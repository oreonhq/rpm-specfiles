# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           python-sniffio
Version:        1.3.1
Release:        %{autorelease}
Summary:        Sniff out which async library your code is running under
License:        MIT OR Apache-2.0
URL:            https://github.com/python-trio/sniffio
Source0:        %{pypi_source sniffio}
BuildArch:      noarch

%global common_description %{expand:
You're writing a library.  You've decided to be ambitious, and support multiple
async I/O packages, like Trio, and asyncio, and ... You've written a bunch of
clever code to handle all the differences.  But... how do you know which piece
of clever code to run?  This is a tiny package whose only purpose is to let you
detect which async library your code is running under.}

%description %{common_description}

%package -n python3-sniffio
Summary:        %{summary}
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description -n python3-sniffio %{common_description}

%prep
%oreon_sha256
%autosetup -n sniffio-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sniffio

%check
%pytest --verbose

%files -n python3-sniffio -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
