%global source0_hash 9efba7106b6192be290b6ea1e92f6b2fb04d8059ff364cabf9c08fba1e4dae71
Name:           python-shellingham
Version:        1.5.4
Release:        1%{?dist}
Summary:        Tool to detect surrounding Shell
License:        ISC
URL:            https://github.com/sarugaku/shellingham
Source0:        https://github.com/sarugaku/shellingham/archive/%{version}/shellingham-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-shellingham = %{version}-%{release}
# /oreon:deps
%description
Shellingham detects what shell the current Python executable is running in.

%package -n     python3-shellingham
Summary:        Tool to detect surrounding Shell
%description -n python3-shellingham
Shellingham detects what shell the current Python executable is running in.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir shellingham-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-shellingham usr/lib/python3*/site-packages/shellingham* usr/lib64/python3*/site-packages/shellingham* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/shellingham* usr/lib64/python3*/site-packages/shellingham* usr/bin/*

%check

%pytest -v
%files
%files -n python3-shellingham -f %{oreon_filedir}/python3-shellingham.list

%changelog

%autochangelog
