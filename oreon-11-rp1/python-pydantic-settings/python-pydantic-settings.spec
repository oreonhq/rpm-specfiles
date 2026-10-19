%global source0_hash 694b793e84f766ba76a90ebdefc01d0a9a045dab0382bee70393da93712ad117
Name:           python-pydantic-settings
Version:        2.15.0
Release:        1%{?dist}
Summary:        Settings management using Pydantic
License:        MIT
URL:            https://github.com/pydantic/pydantic-settings
Source0:        https://files.pythonhosted.org/packages/source/p/pydantic_settings/pydantic_settings-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pydantic-settings = %{version}-%{release}
# /oreon:deps
%package -n       python3-pydantic-settings+yaml
Summary:        Metapackage for python3-pydantic-settings yaml extras
Requires:       python3-pydantic-settings = %{version}-%{release}
Requires:       python3dist(pyyaml) >= 6.0.1
Provides:       python3dist(pydantic-settings[yaml]) = %{version}-%{release}

%description -n python3-pydantic-settings+yaml
Metapackage for python3-pydantic-settings yaml extras.

%package -n       python3-pydantic-settings+toml
Summary:        Metapackage for python3-pydantic-settings toml extras
Requires:       python3-pydantic-settings = %{version}-%{release}
Requires:       python3dist(tomli) >= 2.0.1
Provides:       python3dist(pydantic-settings[toml]) = %{version}-%{release}

%description -n python3-pydantic-settings+toml
Metapackage for python3-pydantic-settings toml extras.

%package -n       python3-pydantic-settings+azure-key-vault
Summary:        Metapackage for python3-pydantic-settings azure-key-vault extras
Requires:       python3-pydantic-settings = %{version}-%{release}
Requires:       python3dist(azure-keyvault-secrets) >= 4.8.0
Requires:       python3dist(azure-identity) >= 1.16.0
Provides:       python3dist(pydantic-settings[azure-key-vault]) = %{version}-%{release}

%description -n python3-pydantic-settings+azure-key-vault
Metapackage for python3-pydantic-settings azure-key-vault extras.

%package -n       python3-pydantic-settings+aws-secrets-manager
Summary:        Metapackage for python3-pydantic-settings aws-secrets-manager extras
Requires:       python3-pydantic-settings = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.35.0
Provides:       python3dist(pydantic-settings[aws-secrets-manager]) = %{version}-%{release}

%description -n python3-pydantic-settings+aws-secrets-manager
Metapackage for python3-pydantic-settings aws-secrets-manager extras.

%package -n       python3-pydantic-settings+gcp-secret-manager
Summary:        Metapackage for python3-pydantic-settings gcp-secret-manager extras
Requires:       python3-pydantic-settings = %{version}-%{release}
Requires:       python3dist(google-cloud-secret-manager) >= 2.23.1
Provides:       python3dist(pydantic-settings[gcp-secret-manager]) = %{version}-%{release}

%description -n python3-pydantic-settings+gcp-secret-manager
Metapackage for python3-pydantic-settings gcp-secret-manager extras.

%description

%package -n     python3-pydantic-settings
Summary:        Settings management using Pydantic
# oreon:reqs
Requires:       python3dist(pydantic) >= 2.7.0
Requires:       python3dist(python-dotenv) >= 0.21.0
Requires:       python3dist(typing-inspection) >= 0.4.0
# /oreon:reqs
%description -n python3-pydantic-settings

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pydantic_settings-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pydantic-settings usr/lib/python3*/site-packages/pydantic_settings* usr/lib64/python3*/site-packages/pydantic_settings* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pydantic_settings* usr/lib64/python3*/site-packages/pydantic_settings* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pydantic-settings -f %{oreon_filedir}/python3-pydantic-settings.list

%changelog

%autochangelog
