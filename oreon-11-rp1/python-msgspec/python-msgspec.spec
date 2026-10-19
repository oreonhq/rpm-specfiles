%global source0_hash 2313508e394b0d208f8f56892ca9b2799e2561329de9763b19619595a6c0f72c
Name:           python-msgspec
Version:        0.21.1
Release:        1%{?dist}
Summary:        A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML.
License:        BSD-3-Clause
URL:            https://jcristharif.com/msgspec/
Source0:        https://files.pythonhosted.org/packages/source/m/msgspec/msgspec-%{version}.tar.gz
Patch:          https://github.com/jcrist/msgspec/pull/852.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-msgspec = %{version}-%{release}
# /oreon:deps
%package -n       python3-msgspec+toml
Summary:        Metapackage for python3-msgspec toml extras
Requires:       python3-msgspec = %{version}-%{release}
Provides:       python3dist(msgspec[toml]) = %{version}-%{release}

%description -n python3-msgspec+toml
Metapackage for python3-msgspec toml extras.

%package -n       python3-msgspec+yaml
Summary:        Metapackage for python3-msgspec yaml extras
Requires:       python3-msgspec = %{version}-%{release}
Provides:       python3dist(msgspec[yaml]) = %{version}-%{release}

%description -n python3-msgspec+yaml
Metapackage for python3-msgspec yaml extras.

%description

%package -n     python3-msgspec
Summary:        A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML.
%description -n python3-msgspec

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir msgspec-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-msgspec usr/lib/python3*/site-packages/msgspec* usr/lib64/python3*/site-packages/msgspec* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/msgspec* usr/lib64/python3*/site-packages/msgspec* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-msgspec -f %{oreon_filedir}/python3-msgspec.list

%changelog

%autochangelog
