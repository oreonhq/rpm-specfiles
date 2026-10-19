%global source0_hash 6fd5e0eaa40ff349959d1cee2872eee90ae32065cc5df9714b1066981535acde
Name:           python-pyclip
Version:        0.7.0
Release:        15%{?dist}
Summary:        Cross-platform Clipboard module for Python with binary support
License:        Apache-2.0
URL:            https://github.com/spyoungtech/pyclip
Source0:        https://github.com/spyoungtech/pyclip/archive/v%{version}/pyclip-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyclip = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyclip
Summary:        Cross-platform Clipboard module for Python with binary support
%description -n python3-pyclip

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyclip-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyclip usr/lib/python3*/site-packages/pyclip* usr/lib64/python3*/site-packages/pyclip* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyclip* usr/lib64/python3*/site-packages/pyclip* usr/bin/*

%files
%files -n python3-pyclip -f %{oreon_filedir}/python3-pyclip.list

%changelog

%autochangelog
