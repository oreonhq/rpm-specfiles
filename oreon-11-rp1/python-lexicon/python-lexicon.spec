%global source0_hash d815dd65da6f7d2cee75aa06ae011c16d5aee43ee2e21ca5baa87391b1cb3f22
%bcond_without tests
Name:		python-lexicon
Version:	3.0.0
Release:        4%{?dist}
Summary:        Powerful dict subclass(es) with aliasing and attribute access
License:	BSD-2-Clause
URL:		https://github.com/bitprophet/lexicon
Source0:        https://github.com/bitprophet/lexicon/archive/%{version}/lexicon-%{version}.tar.gz
BuildArch:	noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-lexicon = %{version}-%{release}
# /oreon:deps
%description
Lexicon is a simple collection of dict sub-classes providing extra power.

%package -n python3-lexicon
Summary:	Powerful dict subclass(es) with aliasing and attribute access
%description -n python3-lexicon
Lexicon is a simple collection of dict sub-classes providing extra power.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lexicon-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lexicon usr/lib/python3*/site-packages/lexicon* usr/lib64/python3*/site-packages/lexicon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lexicon* usr/lib64/python3*/site-packages/lexicon* usr/bin/*
%if %{with tests}
%check

%pytest
%endif
%files
%files -n python3-lexicon -f %{oreon_filedir}/python3-lexicon.list

%changelog

%autochangelog
