%global source0_hash 3f6a7838c3578deec662e63a8cae4ef8d836f6b0d970714be347f868cdcbf232
%global pypi_name qudida
Name:           python-%{pypi_name}
Version:        0.0.4
Release:        11%{?dist}
Summary:        QuDiDA (QUick and DIrty Domain Adaptation)
License:        MIT
URL:            https://github.com/arsenyinfo/qudida
Source0:        https://github.com/arsenyinfo/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
Patch0:         001_setup_py.patch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(opencv)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-extensions)
# /oreon:deps
%description

%package -n     python3-%{pypi_name}
Summary:        QuDiDA (QUick and DIrty Domain Adaptation)
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-qudida -f %{oreon_filedir}/python3-qudida.list

%changelog

%autochangelog
