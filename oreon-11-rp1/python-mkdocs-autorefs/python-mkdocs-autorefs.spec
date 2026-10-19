%global source0_hash d54a284f27a7346b9c38f1f852177940c222da508e66edc816a0fa55fc6da197
Name:           python-mkdocs-autorefs
Version:        1.4.4
Release:        1%{?dist}
Summary:        Automatically link across pages in MkDocs.
License:        ISC
URL:            https://mkdocstrings.github.io/autorefs
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_autorefs/mkdocs_autorefs-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/mkdocstrings/autorefs/pull/60.patch
Patch100:       mkdocs_autorefs-revert-license-fields.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-autorefs = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-autorefs
Summary:        Automatically link across pages in MkDocs.
# oreon:reqs
Requires:       python3dist(markdown) >= 3.3
Requires:       python3dist(markupsafe) >= 2.0.1
Requires:       python3dist(mkdocs) >= 1.1
# /oreon:reqs
%description -n python3-mkdocs-autorefs

%prep
%global oreon_srcdir mkdocs_autorefs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-autorefs usr/lib/python3*/site-packages/mkdocs_autorefs* usr/lib64/python3*/site-packages/mkdocs_autorefs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_autorefs* usr/lib64/python3*/site-packages/mkdocs_autorefs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-autorefs -f %{oreon_filedir}/python3-mkdocs-autorefs.list

%changelog

%autochangelog
