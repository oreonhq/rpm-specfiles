%global source0_hash 7c35c5421a39bb82e58018febd90e3b6e5db34c5443aaaf742b3f33d4655f1c0
%global upname pathtools
Name:		python-%{upname}
Version:	0.1.2
Release:        1%{?dist}
Summary:        Pattern matching and various utilities for file systems paths
License:	MIT
URL:		https://github.com/gorakhargosh/%{upname}
Source0:        https://files.pythonhosted.org/packages/source/%/%{upname/%{upname-%{version}.tar.gz
Patch:		pathtools-0.1.2-version_imp.patch
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# /oreon:deps
%description

%package -n python3-%{upname}
Summary: %summary
%{?python_provide:%python_provide python3-%{upname}}
%description -n python3-%{upname}

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pathtools -f %{oreon_filedir}/python3-pathtools.list

%changelog

%autochangelog
