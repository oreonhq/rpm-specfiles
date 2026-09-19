%global source0_hash eddd7a15448497f3dc6e63ffb9f86e9fb0af355173e0fc89e2b178d6860e5c6f

# The SDK tools have never had a versioned release, but they are updated
# frequently in the upstream repository.
%global         srcname         azure-sdk-tools
%global         commit          67d46b9c4292c267c14833b50bb313c077e63cd5
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         short_version   0.0.0

Name:           python-%{srcname}
Version:        %{short_version}~git.4.%{shortcommit}
Release:        17%{?dist}
Summary:        Specific tools for Azure SDK for Python testing
License:        MIT and Apache-2.0
URL:            https://github.com/Azure/azure-sdk-for-python/
# The azure-sdk-for-python repository is huge at > 160MB, but we only need ~
# 100KB of source for this package. Use this script to generate a tarball of the
# source code:
# ./generate-devtools-tarball.sh COMMIT_SHA
Source0:        azure-sdk-tools-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Specific tools for Azure SDK for Python testing}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1
Provides:       python3dist(%{srcname}) == %{version}-%{release}
%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p3 -c -n %{srcname}-%{commit}

%build
# Some tools are only used for the Azure SDK CI system and there's no need
# to package those.
rm -rf packaging_tools pypi_tools

# There's a dangling empty setup.py in the devtools_testutils directory.
rm -f devtools_testutils/setup.py

%pyproject_wheel

%install
%pyproject_install

# BZ 2048083: The package metadata causes a provides for version 0.0.0.
rm -rf %{buildroot}%{python3_sitelib}/azure_sdk_tools-0.0.0.dist-info

# Some provided executables are only used internally in Azure SDK's CI.
rm -f %{buildroot}/%{_bindir}/{auto_codegen,auto_package,generate_package,generate_sdk,sdk_generator,sdk_package}

%files -n python3-%{srcname}
%doc changelog_generics.md
%license LICENSE
%{python3_sitelib}/devtools_testutils
%{python3_sitelib}/testutils

%changelog
%autochangelog
