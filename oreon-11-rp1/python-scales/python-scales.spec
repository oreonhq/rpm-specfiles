%global source0_hash 4561b8042818de0c02af8366a8c6f350040fb0ee822963aa305586433e3fe26f
Name:           python-scales
Version:        1.0.9
Release:        28%{?dist}
Summary:        Stats for Python processes
License:        Apache-2.0
URL:            https://github.com/Cue/scales
Source0:        https://github.com/Cue/scales/archive/%{version}.tar.gz
Patch0:         fix_py38_compatibility.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-scales = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-scales
Summary:        Stats for Python 3 processes
Requires:       python3-six
Requires:       python3-simplejson
%description -n python3-scales

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n scales-%{version}
%patch -P0 -p1
# Python 3.11 compatibility
sed -i "s/self.assertEquals/self.assertEqual/g" \
    src/greplin/scales/scales_test.py \
    src/greplin/scales/aggregation_test.py \
    src/greplin/scales/formats_test.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-scales usr/lib/python3*/site-packages/scales* usr/lib64/python3*/site-packages/scales* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/scales* usr/lib64/python3*/site-packages/scales* usr/bin/*

%check

%pytest
%files
%files -n python3-scales -f %{oreon_filedir}/python3-scales.list

%changelog

%autochangelog
