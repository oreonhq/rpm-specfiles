%global source0_hash 342a666de780235da91c7186781c03ab3a5992fd9d572119b49d4149549a1ed2
%bcond tests 0
Name:           python-mkdocs-minify-plugin
Version:        0.8.0
Release:        1%{?dist}
Summary:        MkDocs plugin to minify HTML, JS or CSS files
License:        MIT
URL:            https://github.com/byrnereese/mkdocs-minify-plugin
Source0:        https://github.com/byrnereese/mkdocs-minify-plugin/archive/%{version}/mkdocs-minify-plugin-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-minify-plugin = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-minify-plugin
Summary:        MkDocs plugin to minify HTML, JS or CSS files
%description -n python3-mkdocs-minify-plugin

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mkdocs-minify-plugin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-minify-plugin usr/lib/python3*/site-packages/mkdocs_minify_plugin* usr/lib64/python3*/site-packages/mkdocs_minify_plugin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_minify_plugin* usr/lib64/python3*/site-packages/mkdocs_minify_plugin* usr/bin/*

%check

%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif
%files
%files -n python3-mkdocs-minify-plugin -f %{oreon_filedir}/python3-mkdocs-minify-plugin.list

%changelog

%autochangelog
