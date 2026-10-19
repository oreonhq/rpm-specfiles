%global source0_hash d9e83fc768a3a22b4f6be4b0c53f60f433cc1d518748d5e7bfcd812ad5c09e53
%global giturl  https://github.com/executablebooks/sphinx-book-theme
Name:           python-sphinx-book-theme
Version:        1.4.0
Release:        1%{?dist}
Summary:        Interactive book theme for Sphinx
License:        BSD-3-Clause
BuildArch:      noarch
URL:            https://jupyterbook.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/sphinx-book-theme-%{version}.tar.gz
Source1:        sphinx-book-theme-%{version}-vendor.tar.xz
Source2:        sphinx-book-theme-%{version}-vendor-licenses.txt
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  /usr/bin/npm
BuildRequires:  nodejs-devel
BuildRequires:  yarnpkg
# /oreon:deps
%description

%package     -n python3-sphinx-book-theme
Summary:        Interactive book theme for Sphinx
%description -n python3-sphinx-book-theme

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sphinx-book-theme-%{version} -a1 -p1
cp -p %{SOURCE2} .
rm src/sphinx_book_theme/theme/sphinx_book_theme/static/.gitignore

# Relax strict version requirements
sed -i 's/==/>=/g' pyproject.toml

# Do not run code coverage tests during an RPM build
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -i '/coverage/d;/pytest-cov/d' pyproject.toml

# Substitute the installed nodejs version for the requested version
%global nodejs_version %(%{_bindir}/node -v | sed s/v//)
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml

%build -p

export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv
%install
%pyproject_install
%oreon_autofiles python3-sphinx-book-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v
%files -f %{oreon_filedir}/main.list
%files -n python3-sphinx-book-theme -f %{oreon_filedir}/python3-sphinx-book-theme.list

%changelog

%autochangelog
