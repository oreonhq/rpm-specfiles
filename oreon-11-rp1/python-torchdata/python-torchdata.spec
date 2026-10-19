%global source0_hash 945c53a8587567624aaad2d66204fbae9acb9535696554c53ffeb83320c308b9
%global pypi_name torchdata
%bcond_with gitcommit
%if %{with gitcommit}
%global pypi_version 0.7.1
%global commit0 66f0b984d4c3b2f7d715d8eb4e4cac5101bf7f08
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240327
%else
%global pypi_version 0.11.0
%endif
%bcond_with test
Name:           python-%{pypi_name}
%if %{with gitcommit}
Version:        %{pypi_version}^git%{date0}.%{shortcommit0}
%else
Version:        %{pypi_version}
%endif
Release:        1%{?dist}
Summary:        A PyTorch module for data loading
License:        BSD-3-Clause
URL:            https://github.com/pytorch/data
%if %{with gitcommit}
Source0:        https://github.com/pytorch/data/archive/refs/tags/v%{version}.tar.gz#/data-%{version}.tar.gz
%else
%endif
ExclusiveArch:  x86_64 aarch64
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(urllib3)
# /oreon:deps
%description
torchdata is a library of common modular data loading primitives for
easily constructing data pipelines.

%package -n     python3-%{pypi_name}
Summary:        A PyTorch module for data loading
%description -n python3-%{pypi_name}
torchdata is a library of common modular data loading primitives for
easily constructing data pipelines.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%autosetup -p1 -n data-%{commit0}
%else
%autosetup -p1 -n data-%{version}
%endif

rm -rf third_party/*

%build

%py3_build
%check

%if %{with test}
%pytest
%endif
%install
%py3_build
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-torchdata -f %{oreon_filedir}/python3-torchdata.list

%changelog

%autochangelog
