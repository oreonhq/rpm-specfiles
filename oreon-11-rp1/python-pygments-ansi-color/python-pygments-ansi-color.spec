%global source0_hash 77ca4d7e436863f198a7754385493e2c2506168c4685d16bf86dd91948a4841c
Name:           python-pygments-ansi-color
Version:        0.3.0
Release:        1%{?dist}
Summary:        ANSI color-code highlighting
License:        Apache-2.0
URL:            https://github.com/chriskuehl/pygments-ansi-color
Source0:        https://github.com/chriskuehl/pygments-ansi-color/archive/v%{version}/pygments-ansi-color-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pygments-ansi-color = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pygments-ansi-color
Summary:        ANSI color-code highlighting
%description -n python3-pygments-ansi-color

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pygments-ansi-color-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygments-ansi-color usr/lib/python3*/site-packages/pygments_ansi_color* usr/lib64/python3*/site-packages/pygments_ansi_color* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygments_ansi_color* usr/lib64/python3*/site-packages/pygments_ansi_color* usr/bin/*

%check

%pytest -v
%files
%files -n python3-pygments-ansi-color -f %{oreon_filedir}/python3-pygments-ansi-color.list

%changelog

%autochangelog
