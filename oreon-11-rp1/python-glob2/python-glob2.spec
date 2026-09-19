%global source0_hash 85c3dbd07c8aa26d63d7aacee34fa86e9a91a3873bc30bf62ec46e531f92ab8c

%global desc Version of the glob module that can capture patterns and supports recursive\
wildcards.
%global pkg_name glob2
%global pypi_version 0.7

Name:           python-%{pkg_name}
Version:        0.7
Release:        30%{?dist}
Summary:        Glob module recursive wildcards support

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pkg_name}
Source0:        https://files.pythonhosted.org/packages/d7/a5/bbbc3b74a94fbdbd7915e7ad030f16539bfdc1362f7e9003b594f0537950/glob2-0.7.tar.gz

BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pkg_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
Requires:       python3-setuptools

%description -n python3-%{pkg_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkg_name}-%{pypi_version}
# Compatibility with pytest 8
sed -i "s/setup(/setup_method(/" test.py
sed -i "s/teardown(/teardown_method(/" test.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pkg_name}

%check
%pyproject_check_import

%pytest test.py

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst CHANGES
%license LICENSE

%changelog
%autochangelog
