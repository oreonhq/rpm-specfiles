%global source0_hash 1626d96d2672a6cf021d9b66a5013b6e594865403b4a06d75034e0a9ff1cbdc6

%{!?_licensedir: %global license %%doc}

%global modname blowfish
%global sum     Fast, efficient Blowfish cipher implementation in pure Python (3.4+)

Name:               python-blowfish
Version:            0.6.1
Release:            35%{?dist}
Summary:            %{sum}

License:            GPL-3.0-or-later
URL:                http://pypi.python.org/pypi/blowfish
Source0:            https://files.pythonhosted.org/packages/source/b/%{modname}/%{modname}-%{version}.tar.bz2

BuildArch:          noarch
BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

%description
%{sum}.

%package -n python3-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
%{sum}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

#%%check
#%%{__python3} -m unittest setup.py

%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{modname}*
%{python3_sitelib}/__pycache__/*

%changelog
%autochangelog
