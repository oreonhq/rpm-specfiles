%global source0_hash a8affaae19384aca66f6efef3babd705042a76e546f08e886f5f28691ac62a3b
Name:           python-eyed3
Version:        0.9.9
Release:        1%{?dist}
Summary:        Python audio data toolkit _ID3 and MP3_
License:        ...
URL:            https://eyed3.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/e/eyed3/eyed3-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-eyed3 = %{version}-%{release}
# /oreon:deps
%package -n       python3-eyed3+yaml-plugin
Summary:        Metapackage for python3-eyed3 yaml-plugin extras
Requires:       python3-eyed3 = %{version}-%{release}
Requires:       python3dist(pyyaml) >= 6.0.2
Provides:       python3dist(eyed3[yaml-plugin]) = %{version}-%{release}

%description -n python3-eyed3+yaml-plugin
Metapackage for python3-eyed3 yaml-plugin extras.

%package -n       python3-eyed3+art-plugin
Summary:        Metapackage for python3-eyed3 art-plugin extras
Requires:       python3-eyed3 = %{version}-%{release}
Requires:       python3dist(pillow) >= 11.3.0
Requires:       python3dist(pylast) >= 5.5.0
Requires:       python3dist(requests) >= 2.32.4
Provides:       python3dist(eyed3[art-plugin]) = %{version}-%{release}

%description -n python3-eyed3+art-plugin
Metapackage for python3-eyed3 art-plugin extras.

%package -n       python3-eyed3+test
Summary:        Metapackage for python3-eyed3 test extras
Requires:       python3-eyed3 = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.3.5
Requires:       python3dist(coverage) >= 7.8.0
Requires:       python3dist(tox) >= 4.25.0
Requires:       python3dist(factory-boy) >= 3.3.3
Requires:       python3dist(pytest-cov) >= 6.1.1
Requires:       python3dist(check-manifest) >= 0.50
Requires:       python3dist(flake8) >= 7.2.0
Provides:       python3dist(eyed3[test]) = %{version}-%{release}

%description -n python3-eyed3+test
Metapackage for python3-eyed3 test extras.

%package -n       python3-eyed3+dev
Summary:        Metapackage for python3-eyed3 dev extras
Requires:       python3-eyed3 = %{version}-%{release}
Requires:       python3dist(twine) >= 6.1.0
Requires:       python3dist(sphinx) >= 7.4.7
Requires:       python3dist(sphinx-rtd-theme) >= 3.0.2
Requires:       python3dist(sphinx-issues) >= 5.0.1
Requires:       python3dist(cogapp) >= 3.5
Requires:       python3dist(paver) >= 1.3.4
Requires:       python3dist(nicfit-py[cookiecutter]) >= 0.8.7
Requires:       python3dist(regarding) >= 0.2.0
Provides:       python3dist(eyed3[dev]) = %{version}-%{release}

%description -n python3-eyed3+dev
Metapackage for python3-eyed3 dev extras.

%description

%package -n     python3-eyed3
Summary:        Python audio data toolkit _ID3 and MP3_
# oreon:reqs
Requires:       python3dist(deprecation) >= 2.1.0
Requires:       python3dist(filetype) >= 1.2.0
# /oreon:reqs
%description -n python3-eyed3

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir eyed3-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-eyed3 usr/lib/python3*/site-packages/eyed3* usr/lib64/python3*/site-packages/eyed3* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/eyed3* usr/lib64/python3*/site-packages/eyed3* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-eyed3 -f %{oreon_filedir}/python3-eyed3.list

%changelog

%autochangelog
