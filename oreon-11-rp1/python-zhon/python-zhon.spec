%global source0_hash a072349ed90717f657aa37cf2c62e4878d9cdbd19db5f5c1852b8963e6ea7022
Name:           python-zhon
Version:        2.1.1
Release:        1%{?dist}
Summary:        Zhon provides constants used in Chinese text processing
License:        MIT
URL:            https://github.com/tsroten/zhon
Source0:        https://github.com/tsroten/zhon/archive/v%{version}/zhon-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-zhon = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-zhon
Summary:        Zhon provides constants used in Chinese text processing
%description -n python3-zhon

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir zhon-%{version}
%oreon_prep
%build

%pyproject_wheel
pushd docs
sphinx-build -b text .  text
popd
%install
%pyproject_install
%oreon_autofiles python3-zhon usr/lib/python3*/site-packages/zhon* usr/lib64/python3*/site-packages/zhon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zhon* usr/lib64/python3*/site-packages/zhon* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-zhon -f %{oreon_filedir}/python3-zhon.list

%changelog

%autochangelog
