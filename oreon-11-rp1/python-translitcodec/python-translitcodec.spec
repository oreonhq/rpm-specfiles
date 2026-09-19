%global source0_hash 3be7975c630ec0f1dd5b3712160c991a9776132985aed2588cba083ba00fa3c8

%global pypi_name translitcodec

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        17%{?dist}
Summary:        Unicode to 8-bit charset transliteration codec

License:        MIT
URL:            http://pypi.python.org/pypi/translitcodec/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description
Best-effort representations using smaller coded character sets
(ASCII, ISO 8859, etc.).

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Best-effort representations using smaller coded character sets
(ASCII, ISO 8859, etc.).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
%autochangelog
