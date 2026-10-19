%global source0_hash 7d44051cce4de6a870bc08642e561e9d2b0c09b261e9fb709a5489f44699f551
Name:           python-mergedeep
Version:        1.3.4
Release:        1%{?dist}
Summary:        A deep merge function for python
BuildArch:      noarch
License:        MIT
URL:            https://github.com/clarketm/mergedeep
Source0:        https://github.com/clarketm/mergedeep/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mergedeep = %{version}-%{release}
# /oreon:deps
%description
A deep merge function for python.

%package -n python3-mergedeep
Summary:        A deep merge function for python
%description -n python3-mergedeep
A deep merge function for python.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mergedeep-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mergedeep usr/lib/python3*/site-packages/mergedeep* usr/lib64/python3*/site-packages/mergedeep* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mergedeep* usr/lib64/python3*/site-packages/mergedeep* usr/bin/*

%check

%tox
%files
%files -n python3-mergedeep -f %{oreon_filedir}/python3-mergedeep.list

%changelog

%autochangelog
