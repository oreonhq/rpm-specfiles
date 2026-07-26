%global source0_hash 32cbe426ba8fa7b62ce5b211f80f0718a0c749cc7ff09e3f4b43a57f7ccdf5e5

%global modname zope.component

Summary: Zope Component Architecture
Name: python-zope-component
Version: 5.0.1
Release: 17%{?dist}
Source0: https://pypi.io/packages/source/z/%{modname}/%{modname}-%{version}.tar.gz
License: ZPL-2.1
BuildArch: noarch
URL: https://pypi.io/project/zope.component

%description
This package represents the core of the Zope Component Architecture.
Together with the 'zope.interface' package, it provides facilities for
defining, registering and looking up components.

%package -n python3-zope-component
Summary: Zope Component Architecture
%{?python_provide:%python_provide python3-zope-component}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

Requires: python3-zope-interface
Requires: python3-zope-event

%description -n python3-zope-component
This package represents the core of the Zope Component Architecture.
Together with the 'zope.interface' package, it provides facilities for
defining, registering and looking up components.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}

rm -rf %{modname}.egg-info

%build
%py3_build

# build Sphinx documents
COPYRIGHT=`grep Author: PKG-INFO |sed -e 's/Author: //'`
cat >docs/conf.py <<END
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = '%{modname}'
copyright = '$COPYRIGHT'
version = '%{version}'
release = '%{version}'
pygments_style = 'sphinx'
html_static_path = ['_static']
extensions = []
END

sphinx-build -b html docs/ html

rm -fr html/{.buildinfo,.doctrees}

%install
%py3_install

%files -n python3-zope-component
%doc CHANGES.rst COPYRIGHT.txt README.rst
%doc html/
%license LICENSE.txt
%{python3_sitelib}/zope/component/
%exclude %{python3_sitelib}/zope/component/*.txt
%{python3_sitelib}/%{modname}-*.egg-info
%{python3_sitelib}/%{modname}-*-nspkg.pth

%changelog
%autochangelog
