%global source0_hash f879a581083cd0a38100bf08ed3e7c60a7daebb931fe660c70f07067ca0675ad

Name:           python-mdx_gh_links
Version:        0.4
Release:        11%{?dist}
Summary:        Python-Markdown Github-Links Extension

License:        BSD-3-Clause
URL:            https://github.com/Python-Markdown/github-links
Source0:        https://github.com/Python-Markdown/github-links/archive/%{version}/mdx_gh_links-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
This package provides an extension to Python-Markdown which adds support for
shorthand links to GitHub users, repositories, issues and commits.

%package -n python3-mdx_gh_links
Summary:        %{summary}

%description -n python3-mdx_gh_links
This package provides an extension to Python-Markdown which adds support for
shorthand links to GitHub users, repositories, issues and commits.

%generate_buildrequires
%pyproject_buildrequires -r

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n github-links-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mdx_gh_links

%check
%pytest

%files -n python3-mdx_gh_links -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
