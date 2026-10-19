%global source0_hash 2dc37ecb1974becdcebdbf7561e7c15a07dbbf20ba21ba16c3593b3038b3afbd
Name:           python-mcp
Version:        2.2.0
Release:        1%{?dist}
Summary:        Model Context Protocol SDK
License:        MIT
URL:            https://modelcontextprotocol.io
Source0:        https://files.pythonhosted.org/packages/source/m/mcp/mcp-%{version}.tar.gz
BuildArch:      noarch
Patch:          replace-uv-dynamic-version-with-hatchling-vcs.diff
Patch1:         remove-pytest-xdist-cli-args.diff
Patch2:         pass_pythonpath_for_subprocess.diff
Patch3:         remove-subject-from-exchange-request-test.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mcp = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mcp
Summary:        Model Context Protocol SDK
# oreon:reqs
Requires:       python3dist(tomli) >= 2.0
# /oreon:reqs
%description -n python3-mcp

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mcp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mcp usr/lib/python3*/site-packages/mcp* usr/lib64/python3*/site-packages/mcp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mcp* usr/lib64/python3*/site-packages/mcp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mcp -f %{oreon_filedir}/python3-mcp.list

%changelog

%autochangelog
