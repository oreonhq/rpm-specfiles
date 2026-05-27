%global source0_hash none

Name:           pythondist
Version:        4.3.0
Release:        0
Summary:        ...
License:        ZPLv2.1
Source0:        https://files.pythonhosted.org/packages/source/z/zope.component/zope.component-4.3.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Turn off Python bytecode compilation because the build would fail without Python 3.7/3.10
%define __brp_python_bytecompile %{nil}

%description
...

%package -n python3-zope-component
Summary:        ...
%description -n python3-zope-component
...

%package -n python3.7-zope-component
Summary:        ...
%description -n python3.7-zope-component
...

%if v"%{python3_version}" != v"3.9"
%package -n python3.9-zope-component
Summary:        ...
%description -n python3.9-zope-component
...
%endif

%if v"%{python3_version}" != v"3.10"
%package -n python3.10-zope-component
Summary:        ...
%description -n python3.10-zope-component
...
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n zope.component-%{version}

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}/usr/lib/python3.7/site-packages
cp -a %{buildroot}%{python3_sitelib}/zope.component-%{version}-py%{python3_version}.egg-info \
      %{buildroot}/usr/lib/python3.7/site-packages/zope.component-%{version}-py3.7.egg-info

%if v"%{python3_version}" != v"3.9"
mkdir -p %{buildroot}/usr/lib/python3.9/site-packages
cp -a %{buildroot}%{python3_sitelib}/zope.component-%{version}-py%{python3_version}.egg-info \
      %{buildroot}/usr/lib/python3.9/site-packages/zope.component-%{version}-py3.9.egg-info
%endif

%if v"%{python3_version}" != v"3.10"
mkdir -p %{buildroot}/usr/lib/python3.10/site-packages
cp -a %{buildroot}%{python3_sitelib}/zope.component-%{version}-py%{python3_version}.egg-info \
      %{buildroot}/usr/lib/python3.10/site-packages/zope.component-%{version}-py3.10.egg-info
%endif

%files -n python3-zope-component
%license LICENSE.txt
%{python3_sitelib}/*

%files -n python3.7-zope-component
%license LICENSE.txt
/usr/lib/python3.7/site-packages/zope.component-%{version}-py3.7.egg-info/

%if v"%{python3_version}" != v"3.9"
%files -n python3.9-zope-component
%license LICENSE.txt
/usr/lib/python3.9/site-packages/zope.component-%{version}-py3.9.egg-info/
%endif

%if v"%{python3_version}" != v"3.10"
%files -n python3.10-zope-component
%license LICENSE.txt
/usr/lib/python3.10/site-packages/zope.component-%{version}-py3.10.egg-info/
%endif
