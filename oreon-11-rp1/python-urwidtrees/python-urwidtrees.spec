%global source0_hash db7344de2c03257698c9fc12f140d46cee505241b0df378e6f76925d22c32eaa

Name:           python-urwidtrees
Version:        1.0.4
Release:        2%{?dist}
Summary:        Tree Widget Container API for the urwid toolkit

License:        GPL-3.0-or-later
                # PyPI release is not maintained by pazz, so let's stick with github
URL:            https://github.com/pazz/urwidtrees
Source:         https://github.com/pazz/urwidtrees/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel

%global _description %{expand:
It uses an MVC approach and allows to build trees of widgets. Its design
goals are

 * clear separation classes that define, decorate and display trees of widgets
 * representation of trees by local operations on node positions
 * easy to use default implementation for simple trees
 * Collapses are considered decoration}

%description %_description

%package -n     python3-urwidtrees
Summary:        %{summary}

%description -n python3-urwidtrees %_description

%package -n python3-urwidtrees-doc
BuildRequires:  python3-sphinx
Summary:        Documentation for urwidtrees

%description -n python3-urwidtrees-doc
Development documentation for urwidtrees

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n urwidtrees-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs/
make -e SPHINXBUILD=/usr/bin/sphinx-build-3 html
popd

%install
%pyproject_install
%pyproject_save_files -l urwidtrees

%check
%pyproject_check_import

%files -n python3-urwidtrees -f %{pyproject_files}
%license LICENSE.md

%files -n python3-urwidtrees-doc
%license LICENSE.md
%doc docs/build/html

%changelog
%autochangelog
