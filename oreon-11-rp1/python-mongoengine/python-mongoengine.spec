%global source0_hash 3b43abaf2d5f0b7d39efc2b7d9e78f4d4a5dc7ce92b9889ba81a5a9b8dee3cf3

%global pkgname mongoengine
%global sum A Python Document-Object Mapper for working with MongoDB
%global desc MongoEngine is a Document-Object Mapper (think ORM, \
but for document databases) for working with MongoDB \
from Python. It uses a simple declarative API, similar \
to the Django ORM.
 
 
Name:          python-mongoengine
Version:       0.29.1
Release:       8%{?dist}
BuildArch:     noarch
 
License:       MIT
Summary:       %{sum}
URL:           http://mongoengine.org/
Source0:       %{pypi_source %pkgname}

BuildRequires: python3-devel

%description
%{desc}
 
 
%package -n python3-%{pkgname}
Summary:       %{sum}
Recommends:    python3-blinker
Recommends:    python3-pillow
Requires:      python3-pymongo
Requires:      python3-pymongo-gridfs
 
 
%description -n python3-%{pkgname}
%{desc}
 
 
%package doc
Summary:       Documentation for %{name}
BuildArch:     noarch
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-pymongo-gridfs
BuildRequires: make
 
 
%description doc
Documentation for %{name}.
 
 
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}
find . -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'
# Avoid build dependency on readthedocs-sphinx-ext
sed -Ei 's/(, )?"readthedocs_ext\.readthedocs"//' docs/conf.py
 

%generate_buildrequires
%pyproject_buildrequires

 
%build
%pyproject_wheel
PYTHONPATH=$(pwd) make -C docs SPHINXBUILD=sphinx-build-3 html
rm -f docs/_build/html/.buildinfo
# Don't ship fonts
rm -rf docs/_build/html/_static/font
 
 
%install
%pyproject_install
%pyproject_save_files -l %{pkgname}
 

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.rst
 
 
%files doc
%license LICENSE
%doc docs/_build/html
 
 
%changelog
%autochangelog
