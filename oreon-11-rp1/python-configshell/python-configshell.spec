%global source0_hash ce1ee0a983108078ea09d3deec509b41ea6d01cc1d1ceac991741cd32dd0c710
%global oname configshell-fb
Name:           python-configshell
License:        Apache-2.0
Summary:        A framework to implement simple but nice CLIs
Epoch:          1
Version:        2.0.3
Release:        1%{?dist}
URL:            https://github.com/open-iscsi/configshell-fb
Source0:        https://github.com/open-iscsi/configshell-fb/archive/refs/tags/v%{version}.tar.gz#/configshell-fb-2.0.3.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-configshell = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-configshell
Summary:        A framework to implement simple but nice CLIs
# oreon:reqs
Requires:       python3dist(pyparsing) < 4
Requires:       python3dist(pyparsing) >= 2.4.7
# /oreon:reqs
%description -n python3-configshell

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{oname}-%{version}

%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-configshell usr/lib/python3*/site-packages/configshell* usr/lib64/python3*/site-packages/configshell* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/configshell* usr/lib64/python3*/site-packages/configshell* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-configshell -f %{oreon_filedir}/python3-configshell.list

%changelog

%autochangelog
