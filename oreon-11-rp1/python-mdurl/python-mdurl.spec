%global source0_hash 99d4fabddab7ee4a05fa458deb1a6f0d009966e4631c50d1b875767a1cd3896d
Name:           python-mdurl
Version:        0.1.2
Release:        1%{?dist}
Summary:        Markdown URL utilities
License:        MIT
URL:            https://github.com/executablebooks/mdurl
Source0:        https://github.com/executablebooks/mdurl/archive/%{version}/mdurl-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2.0
Requires:       python3-mdurl = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mdurl
Summary:        Markdown URL utilities
%description -n python3-mdurl

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n mdurl-%{version}
sed -i "s/pytest-cov//" tests/requirements.txt

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mdurl usr/lib/python3*/site-packages/mdurl* usr/lib64/python3*/site-packages/mdurl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mdurl* usr/lib64/python3*/site-packages/mdurl* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-mdurl -f %{oreon_filedir}/python3-mdurl.list

%changelog

%autochangelog
