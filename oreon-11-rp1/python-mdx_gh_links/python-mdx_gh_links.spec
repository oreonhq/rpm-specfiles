%global source0_hash f879a581083cd0a38100bf08ed3e7c60a7daebb931fe660c70f07067ca0675ad
Name:           python-mdx_gh_links
Version:        0.4
Release:        1%{?dist}
Summary:        Python-Markdown Github-Links Extension
License:        BSD-3-Clause
URL:            https://github.com/Python-Markdown/github-links
Source0:        https://github.com/Python-Markdown/github-links/archive/%{version}/mdx_gh_links-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-mdx_gh_links = %{version}-%{release}
# /oreon:deps
%description
This package provides an extension to Python-Markdown which adds support for
shorthand links to GitHub users, repositories, issues and commits.

%package -n python3-mdx_gh_links
Summary:        Python-Markdown Github-Links Extension
# oreon:reqs
Requires:       python3dist(markdown) >= 3.0.0
# /oreon:reqs
%description -n python3-mdx_gh_links
This package provides an extension to Python-Markdown which adds support for
shorthand links to GitHub users, repositories, issues and commits.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir github-links-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mdx_gh_links usr/lib/python3*/site-packages/mdx_gh_links* usr/lib64/python3*/site-packages/mdx_gh_links* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mdx_gh_links* usr/lib64/python3*/site-packages/mdx_gh_links* usr/bin/*

%check

%pytest
%files
%files -n python3-mdx_gh_links -f %{oreon_filedir}/python3-mdx_gh_links.list

%changelog

%autochangelog
