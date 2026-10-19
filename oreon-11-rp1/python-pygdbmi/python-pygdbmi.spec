%global source0_hash 5c52a37211d55eeeaf5c06eacc8e8d49e9dacfd36a526d3534b4a5d5f5ee94d9
Name:           python-pygdbmi
Version:        0.11.0.0
Release:        1%{?dist}
Summary:        Get Structured Output from GDB's Machine Interface
License:        MIT
URL:            https://github.com/cs01/pygdbmi
Source0:        https://github.com/cs01/pygdbmi/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pygdbmi = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pygdbmi
Summary:        Get Structured Output from GDB's Machine Interface
%description -n python3-pygdbmi

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pygdbmi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygdbmi usr/lib/python3*/site-packages/pygdbmi* usr/lib64/python3*/site-packages/pygdbmi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygdbmi* usr/lib64/python3*/site-packages/pygdbmi* usr/bin/*

%check

%pytest --ignore tests/test_gdbcontroller.py
%files
%files -n python3-pygdbmi -f %{oreon_filedir}/python3-pygdbmi.list

%changelog

%autochangelog
