%global source0_hash a6125ea7db6cc1a900d76a967f262535af09831160a93c56d7f0d522a79b5faf
Name:           python-mkdocs-static-i18n
Version:        1.3.1
Release:        1%{?dist}
Summary:        MkDocs i18n plugin using static translation markdown files
License:        MIT
URL:            https://github.com/ultrabug/mkdocs-static-i18n
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_static_i18n/mkdocs_static_i18n-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-static-i18n = %{version}-%{release}
# /oreon:deps
%package -n       python3-mkdocs-static-i18n+material
Summary:        Metapackage for python3-mkdocs-static-i18n material extras
Requires:       python3-mkdocs-static-i18n = %{version}-%{release}
Requires:       python3dist(mkdocs-material) < 9.7.2
Provides:       python3dist(mkdocs-static-i18n[material]) = %{version}-%{release}

%description -n python3-mkdocs-static-i18n+material
Metapackage for python3-mkdocs-static-i18n material extras.

%description

%package -n     python3-mkdocs-static-i18n
Summary:        MkDocs i18n plugin using static translation markdown files
# oreon:reqs
Requires:       python3dist(mkdocs) >= 1.5.2
# /oreon:reqs
%description -n python3-mkdocs-static-i18n

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mkdocs_static_i18n-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-static-i18n usr/lib/python3*/site-packages/mkdocs_static_i18n* usr/lib64/python3*/site-packages/mkdocs_static_i18n* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_static_i18n* usr/lib64/python3*/site-packages/mkdocs_static_i18n* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-static-i18n -f %{oreon_filedir}/python3-mkdocs-static-i18n.list

%changelog

%autochangelog
