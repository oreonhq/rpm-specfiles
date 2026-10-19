%global source0_hash a9beab8fe58993dc1e86056dc2ff4809cbc8f3b74df458e29102d57e2635b460
%global desc %{expand: \
wxnatpy is a wxPython widget which allows users to browse the contents of a
XNAT repository.  It is built on top of wxPython and xnatpy.}
Name:           python-wxnatpy
Version:        0.4.0
Release:        1%{?dist}
Summary:        wxnatpy is a wxPython widget which allows users to browse the contents of a XNAT repository
License:        Apache-2.0
URL:            https://github.com/pauldmccarthy/wxnatpy
Source0:        https://github.com/pauldmccarthy/wxnatpy/archive/%{version}/wxnatpy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wxnatpy = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n python3-wxnatpy
Summary:        wxnatpy is a wxPython widget which allows users to browse the contents of a XNAT repository
BuildRequires:  python3-devel
%description -n python3-wxnatpy
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n wxnatpy-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wxnatpy usr/lib/python3*/site-packages/wxnatpy* usr/lib64/python3*/site-packages/wxnatpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wxnatpy* usr/lib64/python3*/site-packages/wxnatpy* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-wxnatpy -f %{oreon_filedir}/python3-wxnatpy.list

%changelog

%autochangelog
