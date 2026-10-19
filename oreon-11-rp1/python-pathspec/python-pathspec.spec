%global source0_hash 17db5ecd524104a120e173814c90367a96a98d07c45b2e10c2f3919fff91bf5a
Name:           python-pathspec
Version:        1.1.1
Release:        1%{?dist}
Summary:        Utility library for gitignore style pattern matching of file paths.
License:        MPL-2.0
URL:            https://github.com/cpburnz/python-pathspec
Source0:        https://files.pythonhosted.org/packages/source/p/pathspec/pathspec-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-pathspec = %{version}-%{release}
# /oreon:deps
%package -n       python3-pathspec+hyperscan
Summary:        Metapackage for python3-pathspec hyperscan extras
Requires:       python3-pathspec = %{version}-%{release}
Requires:       python3dist(hyperscan) >= 0.7
Provides:       python3dist(pathspec[hyperscan]) = %{version}-%{release}

%description -n python3-pathspec+hyperscan
Metapackage for python3-pathspec hyperscan extras.

%package -n       python3-pathspec+optional
Summary:        Metapackage for python3-pathspec optional extras
Requires:       python3-pathspec = %{version}-%{release}
Requires:       python3dist(typing-extensions) >= 4
Provides:       python3dist(pathspec[optional]) = %{version}-%{release}

%description -n python3-pathspec+optional
Metapackage for python3-pathspec optional extras.

%package -n       python3-pathspec+re2
Summary:        Metapackage for python3-pathspec re2 extras
Requires:       python3-pathspec = %{version}-%{release}
Requires:       python3dist(google-re2) >= 1.1
Provides:       python3dist(pathspec[re2]) = %{version}-%{release}

%description -n python3-pathspec+re2
Metapackage for python3-pathspec re2 extras.

%description

%package -n     python3-pathspec
Summary:        Utility library for gitignore style pattern matching of file paths.
%description -n python3-pathspec

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pathspec-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pathspec usr/lib/python3*/site-packages/pathspec* usr/lib64/python3*/site-packages/pathspec* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pathspec* usr/lib64/python3*/site-packages/pathspec* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pathspec -f %{oreon_filedir}/python3-pathspec.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.4-1
- Prepare for Oreon 11 (RP1)
