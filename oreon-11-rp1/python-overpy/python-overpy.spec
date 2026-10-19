%global source0_hash 05ba0aa23455cdddb8679e0476bd1d9cbf7380f3136ef2785f836733a68c4468
%global github_name python-overpy
%global pretty_name overpy
Name:           python-%{pretty_name}
Version:        0.7
Release:        12%{?dist}
Summary:        Python Wrapper to access the Overpass API
License:        MIT
URL:            https://github.com/DinoTools/python-overpy
Source0:        https://github.com/DinoTools/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  python3dist(sphinx-rtd-theme)
# /oreon:deps
%description

%package -n python3-%{pretty_name}
Summary:        Python Wrapper to access the Overpass API
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
%description -n python3-%{pretty_name}

%package doc
Summary:        %{summary}
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{github_name}-%{version}
rm -rf %{pretty_name}.egg-info

%build

%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
rm -rf html/.{doctrees,buildinfo}
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-overpy -f %{oreon_filedir}/python3-overpy.list
%files -n python-overpy-doc -f %{oreon_filedir}/python-overpy-doc.list

%changelog

%autochangelog
