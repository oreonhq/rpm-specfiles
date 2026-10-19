%global source0_hash 10c9511cea88f568257f960358a467d12b970e1f7b2c0e5fb2bb48cab1928443
Name:           python-mkdocs-material-extensions
Version:        1.3.1
Release:        1%{?dist}
Summary:        Extension pack for Python Markdown and MkDocs Material
License:        MIT
URL:            https://github.com/facelessuser/mkdocs-material-extensions
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_material_extensions/mkdocs_material_extensions-%{version}.tar.gz
BuildArch:      noarch
%bcond tests 1
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 0.21.1
Requires:       python3-mkdocs-material-extensions = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-material-extensions
Summary:        Extension pack for Python Markdown and MkDocs Material
%description -n python3-mkdocs-material-extensions

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mkdocs_material_extensions-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-material-extensions usr/lib/python3*/site-packages/mkdocs_material_extensions* usr/lib64/python3*/site-packages/mkdocs_material_extensions* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_material_extensions* usr/lib64/python3*/site-packages/mkdocs_material_extensions* usr/bin/*

%check

%pyproject_check_import %{!?with_tests:-e materialx.emoji}
%if %{with tests}
%tox
%endif
%files
%files -n python3-mkdocs-material-extensions -f %{oreon_filedir}/python3-mkdocs-material-extensions.list

%changelog

%autochangelog
