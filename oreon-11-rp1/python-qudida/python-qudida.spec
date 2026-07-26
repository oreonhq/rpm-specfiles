%global source0_hash 3f6a7838c3578deec662e63a8cae4ef8d836f6b0d970714be347f868cdcbf232

%global pypi_name qudida

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        11%{?dist}
Summary:        QuDiDA (QUick and DIrty Domain Adaptation)

License:        MIT
URL:            https://github.com/arsenyinfo/qudida
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

Patch0:         001_setup_py.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# Tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(opencv)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(typing-extensions)

%global _description \
QuDiDA is a micro library for very naive though quick pixel level image domain \
adaptation via scikit-learn transformers. \
Is assumed to be used as image augmentation technique, \
while was not tested in public benchmarks.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}/

%changelog
%autochangelog
