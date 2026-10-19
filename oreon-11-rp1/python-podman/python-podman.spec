%global source0_hash bc39b77f4a6a0598bbe860d199e0d54ef2ec551131ae7eab66f0557c43331fb3
Name:           python-podman
Version:        5.8.0
Release:        1%{?dist}
Summary:        Bindings for Podman RESTful API
License:        ...
URL:            https://github.com/containers/podman-py
Source0:        https://files.pythonhosted.org/packages/source/p/podman/podman-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 46.4
Requires:       python3-podman = %{version}-%{release}
# /oreon:deps
%package -n       python3-podman+progress_bar
Summary:        Metapackage for python3-podman progress_bar extras
Requires:       python3-podman = %{version}-%{release}
Requires:       python3dist(rich) >= 12.5.1
Provides:       python3dist(podman[progress_bar]) = %{version}-%{release}

%description -n python3-podman+progress_bar
Metapackage for python3-podman progress_bar extras.

%package -n       python3-podman+docs
Summary:        Metapackage for python3-podman docs extras
Requires:       python3-podman = %{version}-%{release}
Provides:       python3dist(podman[docs]) = %{version}-%{release}

%description -n python3-podman+docs
Metapackage for python3-podman docs extras.

%package -n       python3-podman+test
Summary:        Metapackage for python3-podman test extras
Requires:       python3-podman = %{version}-%{release}
Provides:       python3dist(podman[test]) = %{version}-%{release}

%description -n python3-podman+test
Metapackage for python3-podman test extras.

%description

%package -n     python3-podman
Summary:        Bindings for Podman RESTful API
# oreon:reqs
Requires:       python3dist(requests) >= 2.24
Requires:       python3dist(tomli) >= 1.2.3
# /oreon:reqs
%description -n python3-podman

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir podman-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-podman usr/lib/python3*/site-packages/podman* usr/lib64/python3*/site-packages/podman* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/podman* usr/lib64/python3*/site-packages/podman* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-podman -f %{oreon_filedir}/python3-podman.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.6.0-1
- Prepare for Oreon 11 (RP1)
