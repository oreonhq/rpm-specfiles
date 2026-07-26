%global source0_hash 3970f8570ac54491237bcdb3d8ab5e3eef6c057df29f8c3d1151a51a9c23b975

%global srcname click-log
%global pyname click_log
%global sum Logging integration for python-click

Name:           python-%{srcname}
Version:        0.4.0
Release:        17%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/click-contrib/%{srcname}
Source0:        https://files.pythonhosted.org/packages/32/32/228be4f971e4bd556c33d52a22682bfe318ffe57a1ddb7a546f347a90260/click-log-0.4.0.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-click

%generate_buildrequires
%pyproject_buildrequires

%description
Logging support to python click (CLI creation kit)
applications.

%package -n     python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-click

%description -n python3-%{srcname}
Logging support to python 3 click (CLI creation kit)
applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pyname}
%{python3_sitelib}/%{pyname}-%{version}.dist-info

%changelog
%autochangelog
