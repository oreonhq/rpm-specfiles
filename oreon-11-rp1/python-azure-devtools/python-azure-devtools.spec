%global source0_hash d42d2934dde08f7cb52c97c567edba14a2353a22efa4eedca0457e4e77fe7045

# The last versioned release of the devtools code is 1.2.1, but upstream
# continues to update it without bumping the version. 😞
%global         srcname         azure-devtools
%global         commit          67d46b9c4292c267c14833b50bb313c077e63cd5
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         short_version   1.2.1

Name:           python-%{srcname}
Version:        %{short_version}~git.4.%{shortcommit}
Release:        16%{?dist}
Summary:        Microsoft Azure Development Tools for SDK
License:        MIT and Apache-2.0
URL:            https://github.com/Azure/azure-sdk-for-python/
# The azure-sdk-for-python repository is huge at > 160MB, but we only need ~
# 100KB of source for this package. Use this script to generate a tarball of the
# source code:
# ./generate-devtools-tarball.sh COMMIT_SHA
Source0:        azure-devtools-%{commit}.tar.gz
# Asked upstream to update the vcrpy requirement. PR in progress.
# https://github.com/Azure/azure-sdk-for-python/pull/20032
Patch0:         python-azure-devtools-requirements-fix.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Development tools for Python-based Azure tools
This package contains tools to aid in developing Python-based Azure code.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -v -p3 -c -n %{srcname}-%{commit}

%build
%pyproject_wheel

%generate_buildrequires
%pyproject_buildrequires -r

%install
%pyproject_install
%pyproject_save_files azure_devtools

# Some provided executables are only used internally in Azure SDK's CI.
rm -f %{buildroot}%{_bindir}/{perfstress,perfstressdebug,systemperf}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
