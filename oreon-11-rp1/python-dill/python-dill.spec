%global source0_hash 423092df4182177d4d8ba8290c8a5b640c66ab35ec7da59ccfa00f6fa3eea5fa
%bcond_without check
Name: python-dill
Version: 0.4.1
Release:        1%{?dist}
Summary:        Serialize all of Python
License: BSD-3-Clause
URL: https://github.com/uqfoundation/dill
Source0:        https://files.pythonhosted.org/packages/source/d/dill/dill-%{version}.tar.gz
Patch:  https://github.com/uqfoundation/dill/pull/755.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-dill = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-dill
Summary:        Serialize all of Python
%description -n python3-dill

# The graph extra needs objgraph>=1.7.2; python-objgraph is not packaged
# The profile extra needs gprof2dot>=2022.7.29; python-gprof2dot is not packaged

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir dill-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm %{buildroot}%{_bindir}/get_objgraph %{buildroot}%{_bindir}/get_gprof
find '%{buildroot}%{python3_sitelib}/dill' -type f -name '*.py' ! -perm /0111 \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'
%oreon_autofiles python3-dill usr/lib/python3*/site-packages/dill* usr/lib64/python3*/site-packages/dill* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dill* usr/lib64/python3*/site-packages/dill* usr/bin/*

%check

%if %{with check}
%{py3_test_envvars} %{python3} dill/tests/__main__.py
%endif
%pyproject_check_import -t
%files
%files -n python3-dill -f %{oreon_filedir}/python3-dill.list

%changelog

%autochangelog
