%global source0_hash 6050917628d4740517541422b607404d044117bc31b770c4f9e9e1939a50c908
Name:           python-mkdocs-click
Version:        0.9.0
Release:        1%{?dist}
Summary:        MkDocs extension to generate documentation for Click CLIs
License:        Apache-2.0
URL:            https://pypi.org/project/mkdocs-click/
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_click/mkdocs_click-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 0.22.0
Requires:       python3-mkdocs-click = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-click
Summary:        MkDocs extension to generate documentation for Click CLIs
# oreon:reqs
Requires:       python3dist(click) >= 8.1
Requires:       python3dist(markdown) >= 3.3
# /oreon:reqs
%description -n python3-mkdocs-click

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mkdocs_click-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-click usr/lib/python3*/site-packages/mkdocs_click* usr/lib64/python3*/site-packages/mkdocs_click* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_click* usr/lib64/python3*/site-packages/mkdocs_click* usr/bin/*

%check

%pytest
%files
%files -n python3-mkdocs-click -f %{oreon_filedir}/python3-mkdocs-click.list

%changelog

%autochangelog
