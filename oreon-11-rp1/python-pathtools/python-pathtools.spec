%global source0_hash 7c35c5421a39bb82e58018febd90e3b6e5db34c5443aaaf742b3f33d4655f1c0

%global upname pathtools

Name:		python-%{upname}
Version:	0.1.2
Release:	43%{?dist}
Summary:	Pattern matching and various utilities for file systems paths

License:	MIT
URL:		https://github.com/gorakhargosh/%{upname}
Source0:	%{pypi_source %{upname}}
# This is hacky, but I don't feel like writing a real fix for this
# silly upstream approach. imp is retired in python 3.12, so we need
# to not use it. This replaces the use of it with a marker string
# we'll sub out with the real version in %prep
# not upstreamable, upstream would need to do the mess recommended at
# https://docs.python.org/3.12/whatsnew/3.12.html#removed , or just
# use a less silly way of getting version numbers into setup.py...
# reported as https://github.com/gorakhargosh/pathtools/issues/13
Patch:		pathtools-0.1.2-version_imp.patch

BuildArch:	noarch
BuildRequires: make
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx

%global _description\
%{name} is a Python API library for common path\
and pattern functionality.\

%description %_description

%package -n python3-%{upname}
Summary: %summary
%{?python_provide:%python_provide python3-%{upname}}

%description -n python3-%{upname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upname}-%{version} -p1

# remove hashbang from lib's files
sed -i -e '/#!\//d' pathtools/*.py

# Use the default sphinx theme
# python-flask-sphinx-themes is orphaned
sed -i "s/html_theme = 'flask'/html_theme = 'default'/" ./docs/source/conf.py

# replace the marker from the imp-removal patch with the real version
sed -i -e "s,||VERSION||,'%{version}',g" setup.py

%build
%py3_build

pushd docs
make SPHINXBUILD=sphinx-build-3 html
rm -rf build/html/.build*
popd

%install
%py3_install

%files -n python3-%{upname}
%license LICENSE
%doc AUTHORS LICENSE README
%doc docs/build/html
%{python3_sitelib}/pathtools*/

%changelog
%autochangelog
