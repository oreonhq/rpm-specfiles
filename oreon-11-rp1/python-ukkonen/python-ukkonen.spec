%global source0_hash d238ac2751c967594a5ffd4d3e76a01ddcc63d01088a5c54e5fdd9e3cc7e1211
Name:           python-ukkonen
Version:        1.1.0
Release:        1%{?dist}
Summary:        Implementation of bounded Levenshtein distance (Ukkonen)
License:        MIT
URL:            https://www.github.com/asottile/ukkonen
Source0:        https://www.github.com/asottile/ukkonen/archive/v%{version}/ukkonen-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ukkonen = %{version}-%{release}
# /oreon:deps
%description
Implementation of bounded Levenshtein distance (Ukkonen) port

%package -n     python3-ukkonen
Summary:        Implementation of bounded Levenshtein distance (Ukkonen)
%description -n python3-ukkonen
Implementation of bounded Levenshtein distance (Ukkonen) port

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ukkonen-%{version}
cp -p licenses/LICENSE LICENSE-upstream

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ukkonen usr/lib/python3*/site-packages/ukkonen* usr/lib64/python3*/site-packages/ukkonen* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ukkonen* usr/lib64/python3*/site-packages/ukkonen* usr/bin/*

%check

%pytest
%files
%files -n python3-ukkonen -f %{oreon_filedir}/python3-ukkonen.list

%changelog

%autochangelog
