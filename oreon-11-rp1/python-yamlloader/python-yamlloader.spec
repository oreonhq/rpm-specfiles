%global source0_hash 918232976c9910d079ef74b3266ff9ef674228609aa56e67718b3992940a823f
Name:           python-yamlloader
Version:        1.6.0
Release:        1%{?dist}
Summary:        Ordered YAML loader and dumper for PyYAML.
License:        MIT
URL:            https://github.com/Phynix/yamlloader
Source0:        https://files.pythonhosted.org/packages/source/y/yamlloader/yamlloader-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-yamlloader = %{version}-%{release}
# /oreon:deps
%package -n       python3-yamlloader+dev
Summary:        Metapackage for python3-yamlloader dev extras
Requires:       python3-yamlloader = %{version}-%{release}
Provides:       python3dist(yamlloader[dev]) = %{version}-%{release}

%description -n python3-yamlloader+dev
Metapackage for python3-yamlloader dev extras.

%package -n       python3-yamlloader+doc
Summary:        Metapackage for python3-yamlloader doc extras
Requires:       python3-yamlloader = %{version}-%{release}
Provides:       python3dist(yamlloader[doc]) = %{version}-%{release}

%description -n python3-yamlloader+doc
Metapackage for python3-yamlloader doc extras.

%package -n       python3-yamlloader+test
Summary:        Metapackage for python3-yamlloader test extras
Requires:       python3-yamlloader = %{version}-%{release}
Provides:       python3dist(yamlloader[test]) = %{version}-%{release}

%description -n python3-yamlloader+test
Metapackage for python3-yamlloader test extras.

%description

%package -n     python3-yamlloader
Summary:        Ordered YAML loader and dumper for PyYAML.
%description -n python3-yamlloader

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir yamlloader-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-yamlloader usr/lib/python3*/site-packages/yamlloader* usr/lib64/python3*/site-packages/yamlloader* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/yamlloader* usr/lib64/python3*/site-packages/yamlloader* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-yamlloader -f %{oreon_filedir}/python3-yamlloader.list

%changelog

%autochangelog
