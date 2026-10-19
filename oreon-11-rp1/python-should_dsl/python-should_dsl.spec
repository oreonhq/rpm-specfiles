%global source0_hash 36f753d90fbdf84ef2b7a9e07813e3efac725376feb7a793549f3fff7a03232a
Summary:        Should assertions in Python in as clear and readable a way as possible
Name:		python-should_dsl
Version:	2.1.2
Release:        1%{?dist}
License:	MIT
URL:		https://github.com/nsi-iff/should-dsl
Source0:        https://files.pythonhosted.org/packages/source/s/should_dsl/should_dsl-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-should_dsl = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-should_dsl
Summary:	Should assertions in Python in as clear and readable a way as possible
%description -n python3-should_dsl

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n should_dsl-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-should_dsl usr/lib/python3*/site-packages/should_dsl* usr/lib64/python3*/site-packages/should_dsl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/should_dsl* usr/lib64/python3*/site-packages/should_dsl* usr/bin/*

%check

%{py3_test_envvars} %{python3} run_examples.py README.rst
%files
%files -n python3-should_dsl -f %{oreon_filedir}/python3-should_dsl.list

%changelog

%autochangelog
