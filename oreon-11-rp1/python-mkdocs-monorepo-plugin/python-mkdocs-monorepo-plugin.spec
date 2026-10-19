%global source0_hash 09200bcf837ad35070e6da973aa0cb682e69ed6e16f254a30584550c6d2d8ebb
Name:           python-mkdocs-monorepo-plugin
Version:        1.1.2
Release:        1%{?dist}
Summary:        Plugin for adding monorepository support in Mkdocs
License:        Apache-2.0
URL:            https://github.com/backstage/mkdocs-monorepo-plugin
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs-monorepo-plugin/mkdocs-monorepo-plugin-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-monorepo-plugin = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-monorepo-plugin
Summary:        Plugin for adding monorepository support in Mkdocs
%description -n python3-mkdocs-monorepo-plugin

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mkdocs-monorepo-plugin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-monorepo-plugin usr/lib/python3*/site-packages/mkdocs_monorepo_plugin* usr/lib64/python3*/site-packages/mkdocs_monorepo_plugin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_monorepo_plugin* usr/lib64/python3*/site-packages/mkdocs_monorepo_plugin* usr/bin/*

%check

%pytest -v -k "not test_plugin_on_config_with_nav"
%files
%files -n python3-mkdocs-monorepo-plugin -f %{oreon_filedir}/python3-mkdocs-monorepo-plugin.list

%changelog

%autochangelog
