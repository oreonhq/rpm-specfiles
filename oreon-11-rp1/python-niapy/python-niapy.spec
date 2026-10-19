%global source0_hash f26c813266548ec2a21fdd3436ad8a19dbefacd9f8deb886a7156f020aae5e21
Name:           python-niapy
Version:        2.7.1
Release:        1%{?dist}
Summary:        Micro framework for building nature-inspired algorithms
License:        MIT
URL:            https://github.com/NiaOrg/NiaPy
Source0:        https://github.com/NiaOrg/NiaPy/archive/v%{version}/NiaPy-%{version}.tar.gz
Patch:          %{url}/pull/742.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.10.0
BuildRequires:  python3dist(uv-build) >= 0.9.17
Requires:       python3-niapy = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-niapy
Summary:        Micro framework for building nature-inspired algorithms
Provides:       python-niapy-doc = %{version}-%{release}
Obsoletes:      python-niapy-doc < 2.5.2-10
# oreon:reqs
Requires:       python3dist(matplotlib) >= 3.10.8
Requires:       python3dist(numpy) >= 2.3.5
Requires:       python3dist(openpyxl) >= 3.1.5
Requires:       python3dist(pandas) >= 2.3.3
# /oreon:reqs
%description -n python3-niapy

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n NiaPy-%{version} -p1

# - Don’t bound the version of Python. We must use the system interpreter.
# - Convert SemVer pins to minimum versions, since we can’t generally respect
#   the upper bounds in Fedora.
sed -r -i -e 's/^python ?=/# &/' -e 's/([^#]+ ?= ?")\^/\1>=/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-niapy usr/lib/python3*/site-packages/niapy* usr/lib64/python3*/site-packages/niapy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/niapy* usr/lib64/python3*/site-packages/niapy* usr/bin/*

%check

%pytest -ra -k "${k-}"
%files
%files -n python3-niapy -f %{oreon_filedir}/python3-niapy.list

%changelog

%autochangelog
