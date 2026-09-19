%global source0_hash 8a1d622565a01ca553a87f52de97244f33d04c20d9e4d0dac76ddfeccb6850b9

%global upname husl

Name: python-%{upname}
Version: 4.0.3
Release: 38%{?dist}
Summary: A Python implementation of HUSL
License: MIT

URL: http://github.com/boronine/pyhusl
Source0: https://pypi.python.org/packages/source/h/husl/husl-%{version}.tar.gz
# By mistake the license is not packaged (fixed in devel version upstream)
Source1: https://raw.githubusercontent.com/husl-colors/husl-python/master/LICENSE.txt
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%global _description\
HUSL is a human-friendly alternative to HSL (Hue, Saturation and Lightness)\
color space. This package provides Python2 support

%description %_description

%package -n python3-%{upname}
Summary: A Python implementation of HUSL
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description -n python3-%{upname}
HUSL is a human-friendly alternative to HSL (Hue, Saturation and Lightness)
color space. This package provides Python3 support

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upname}-%{version}

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
cp -p %{SOURCE1} .
%py3_build

%install
%py3_install

%files -n python3-%{upname}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/husl*
%{python3_sitelib}/__pycache__/*

%changelog
%autochangelog
