%global source0_hash fe0f26723d35a5dbd1204a80ca1a9c2f85bf5f062355058059f89d01ee2820b5

Name:           slowloris
Version:        0.2.1
Release:        21%{?dist}
Summary:        Low bandwidth DoS tool

License:        MIT
URL:            https://github.com/gkbrk/slowloris
Source0:        %{pypi_source Slowloris}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Slowloris is basically an HTTP Denial of Service attack that affects threaded
servers.

%package -n     python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Slowloris is basically an HTTP Denial of Service attack that affects threaded
servers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Slowloris-%{version}
# Use setuptools
sed -i -e "s/distutils.core/setuptools/g" setup.py
# Remove shebang
sed -i -e '/^#!\//, 1d' %{name}.py

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/%{name}

%files -n python3-%{name}
%doc README.md
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/Slowloris-%{version}-py*.egg-info

%changelog
%autochangelog
