%global source0_hash 4788a510607addfba56fa33c17ffca78e93359e6210ccc34b914fae902f986db
Name:           python-patch-manager
Version:        0.2.0
Release:        1%{?dist}
Summary:        Create, check and email patch series, with Patchwork integration
License:        GPL-2.0-or-later
URL:            https://github.com/nxtboot/patman
Source0:        https://files.pythonhosted.org/packages/source/p/patch_manager/patch_manager-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 78.1.1
Requires:       python3-patch-manager = %{version}-%{release}
# /oreon:deps
%package -n       python3-patch-manager+gmail
Summary:        Metapackage for python3-patch-manager gmail extras
Requires:       python3-patch-manager = %{version}-%{release}
Provides:       python3dist(patch-manager[gmail]) = %{version}-%{release}

%description -n python3-patch-manager+gmail
Metapackage for python3-patch-manager gmail extras.

%package -n       python3-patch-manager+review
Summary:        Metapackage for python3-patch-manager review extras
Requires:       python3-patch-manager = %{version}-%{release}
Provides:       python3dist(patch-manager[review]) = %{version}-%{release}

%description -n python3-patch-manager+review
Metapackage for python3-patch-manager review extras.

%package -n       python3-patch-manager+test
Summary:        Metapackage for python3-patch-manager test extras
Requires:       python3-patch-manager = %{version}-%{release}
Provides:       python3dist(patch-manager[test]) = %{version}-%{release}

%description -n python3-patch-manager+test
Metapackage for python3-patch-manager test extras.

%package -n       python3-patch-manager+all
Summary:        Metapackage for python3-patch-manager all extras
Requires:       python3-patch-manager = %{version}-%{release}
Provides:       python3dist(patch-manager[all]) = %{version}-%{release}

%description -n python3-patch-manager+all
Metapackage for python3-patch-manager all extras.

%description

%package -n     python3-patch-manager
Summary:        Create, check and email patch series, with Patchwork integration
# oreon:reqs
Requires:       python3dist(aiohttp) >= 3.9
Requires:       python3dist(patatt) >= 0.6
Requires:       python3dist(pygit2) >= 1.14
# /oreon:reqs
%description -n python3-patch-manager

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir patch_manager-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-patch-manager usr/lib/python3*/site-packages/patch_manager* usr/lib64/python3*/site-packages/patch_manager* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/patch_manager* usr/lib64/python3*/site-packages/patch_manager* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-patch-manager -f %{oreon_filedir}/python3-patch-manager.list

%changelog

%autochangelog
