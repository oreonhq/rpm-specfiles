%global source0_hash be600beb2f762f0116025e05490d399e724f668bef84025a7c421bb266688bdb
Name:           python-spdx-tools
Version:        0.8.5
Release:        1%{?dist}
Summary:        SPDX parser and tools.
License:        Apache-2.0
URL:            https://github.com/spdx/tools-python
Source0:        https://files.pythonhosted.org/packages/source/s/spdx_tools/spdx_tools-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Update-excepted-typecheck-error-after-beartype-updat.patch
Patch:          0002-relationship_writer-properly-access-__annotations__-.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-spdx-tools = %{version}-%{release}
# /oreon:deps
%package -n       python3-spdx-tools+test
Summary:        Metapackage for python3-spdx-tools test extras
Requires:       python3-spdx-tools = %{version}-%{release}
Provides:       python3dist(spdx-tools[test]) = %{version}-%{release}

%description -n python3-spdx-tools+test
Metapackage for python3-spdx-tools test extras.

%package -n       python3-spdx-tools+code_style
Summary:        Metapackage for python3-spdx-tools code_style extras
Requires:       python3-spdx-tools = %{version}-%{release}
Provides:       python3dist(spdx-tools[code_style]) = %{version}-%{release}

%description -n python3-spdx-tools+code_style
Metapackage for python3-spdx-tools code_style extras.

%package -n       python3-spdx-tools+graph_generation
Summary:        Metapackage for python3-spdx-tools graph_generation extras
Requires:       python3-spdx-tools = %{version}-%{release}
Provides:       python3dist(spdx-tools[graph_generation]) = %{version}-%{release}

%description -n python3-spdx-tools+graph_generation
Metapackage for python3-spdx-tools graph_generation extras.

%package -n       python3-spdx-tools+development
Summary:        Metapackage for python3-spdx-tools development extras
Requires:       python3-spdx-tools = %{version}-%{release}
Provides:       python3dist(spdx-tools[development]) = %{version}-%{release}

%description -n python3-spdx-tools+development
Metapackage for python3-spdx-tools development extras.

%description

%package -n     python3-spdx-tools
Summary:        SPDX parser and tools.
%description -n python3-spdx-tools

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir spdx_tools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-spdx-tools usr/lib/python3*/site-packages/spdx_tools* usr/lib64/python3*/site-packages/spdx_tools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/spdx_tools* usr/lib64/python3*/site-packages/spdx_tools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-spdx-tools -f %{oreon_filedir}/python3-spdx-tools.list

%changelog

%autochangelog
