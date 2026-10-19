%global source0_hash 13ad0bc8f16522084b34bfb718b3a808e2766ee243787c5229cc629c29c1ecab
Name:           python-wurlitzer
Version:        3.1.1
Release:        1%{?dist}
Summary:        Capture C-level output in context managers
License:        MIT
URL:            https://github.com/minrk/wurlitzer
VCS:            git:%{url}.git
Source0:        https://github.com/minrk/wurlitzer/archive/%{version}/wurlitzer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wurlitzer = %{version}-%{release}
# /oreon:deps
%description
Capture C-level stdout/stderr pipes in Python via os.dup2.

%package -n     python3-wurlitzer
Summary:        Capture C-level output in context managers
%description -n python3-wurlitzer
Capture C-level stdout/stderr pipes in Python via os.dup2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir wurlitzer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wurlitzer usr/lib/python3*/site-packages/wurlitzer* usr/lib64/python3*/site-packages/wurlitzer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wurlitzer* usr/lib64/python3*/site-packages/wurlitzer* usr/bin/*

%check

%pytest -v test.py
%files
%files -n python3-wurlitzer -f %{oreon_filedir}/python3-wurlitzer.list

%changelog

%autochangelog
