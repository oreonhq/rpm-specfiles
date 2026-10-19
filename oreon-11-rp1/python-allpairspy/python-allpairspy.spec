%global source0_hash f69d31a3b56eee119d1ec6063e9c732dd44fbba352ef738cb22d9699fc4009fe
Name:          python-allpairspy
Version:       2.5.1
Release:        1%{?dist}
Summary:        Pairwise test combinations generator
License:       MIT
URL:           https://github.com/thombashi/allpairspy
Source0:        https://files.pythonhosted.org/packages/source/a/allpairspy/allpairspy-%{version}.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-allpairspy = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%package -n python3-allpairspy
Summary:        Pairwise test combinations generator
%description -n python3-allpairspy
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n allpairspy-%{version}
rm -rf allpairspy.egg-info

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-allpairspy usr/lib/python3*/site-packages/allpairspy* usr/lib64/python3*/site-packages/allpairspy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/allpairspy* usr/lib64/python3*/site-packages/allpairspy* usr/bin/*

%check

%{pytest}
%files
%files -n python3-allpairspy -f %{oreon_filedir}/python3-allpairspy.list

%changelog

%autochangelog
