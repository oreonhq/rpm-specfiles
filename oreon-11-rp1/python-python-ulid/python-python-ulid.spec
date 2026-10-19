%global source0_hash bbeec02556190bb9dc3401faa7268696acbfbe7b6db9908c155dc3548629f20c
Name:           python-ulid
Version:        4.0.1
Release:        1%{?dist}
Summary:        Universally unique lexicographically sortable identifier
License:        MIT
URL:            https://github.com/mdomke/python-ulid
Source0:        https://files.pythonhosted.org/packages/source/p/python_ulid/python_ulid-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Depend-on-typing-extensions-for-Python-3.11-avoid-it.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ulid = %{version}-%{release}
# /oreon:deps
%package -n       python3-ulid+pydantic
Summary:        Metapackage for python3-ulid pydantic extras
Requires:       python3-ulid = %{version}-%{release}
Requires:       python3dist(pydantic) >= 2.0
Provides:       python3dist(ulid[pydantic]) = %{version}-%{release}

%description -n python3-ulid+pydantic
Metapackage for python3-ulid pydantic extras.

%description

%package -n     python3-python-ulid
Summary:        Universally unique lexicographically sortable identifier
%description -n python3-python-ulid

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir python_ulid-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-python-ulid usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-python-ulid -f %{oreon_filedir}/python3-python-ulid.list

%changelog

%autochangelog
