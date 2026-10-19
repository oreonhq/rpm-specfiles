%global source0_hash 0faeba6d5d5276d5b59ce71809b2f16d18a3d66b07791007714e09d60e8ad8ad
Name:           python-bidict
Version:        0.24.1
Release:        1%{?dist}
Summary:        Bidirectional mapping library for Python
License:        MPL-2.0
URL:            https://bidict.readthedocs.io
Source0:        https://github.com/jab/bidict/archive/v%{version}/bidict-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
The bidirectional mapping library for Python.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.12
BuildRequires:  python3dist(uv-build) >= 0.8.13
Requires:       python3-bidict = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n     python3-bidict
Summary:        Bidirectional mapping library for Python
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.0
# /oreon:reqs
%description -n python3-bidict %{common_description}

%prep

%autosetup -p1
# Since we have patched out pytest-benchmark, this would not be recognized.
sed -r -i '/--benchmark/d' pytest.ini

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bidict usr/lib/python3*/site-packages/bidict* usr/lib64/python3*/site-packages/bidict* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bidict* usr/lib64/python3*/site-packages/bidict* usr/bin/*

%check

ignore="${ignore-} --ignore=docs/extending.rst"
%pytest ${ignore-}
%files
%files -n python3-bidict -f %{oreon_filedir}/python3-bidict.list

%changelog

%autochangelog
