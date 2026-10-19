%global source0_hash f47eecd9468083c2029cc99945502cb7708b082c232f9aca65da147157b251c7
Name:           python-aiosignal
Version:        1.4.0
Release:        1%{?dist}
Summary:        List of registered asynchronous callbacks
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiosignal
Source0:        https://files.pythonhosted.org/packages/source/a/aiosignal/aiosignal-%{version}.tar.gz
Patch:          0001-Downstream-only-patch-out-coverage-options.patch
Patch:          0002-Downstream-only-do-not-fail-on-warnings.patch
BuildArch:      noarch
%global common_description %{expand:
A project to manage callbacks in asyncio projects.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 51.0
Requires:       python3-aiosignal = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-aiosignal
Summary:        List of registered asynchronous callbacks
Obsoletes:      python-aiosignal-doc < 1.3.1-15
%description -n python3-aiosignal %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir aiosignal-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiosignal usr/lib/python3*/site-packages/aiosignal* usr/lib64/python3*/site-packages/aiosignal* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiosignal* usr/lib64/python3*/site-packages/aiosignal* usr/bin/*

%check

%pytest
%files
%files -n python3-aiosignal -f %{oreon_filedir}/python3-aiosignal.list

%changelog

%autochangelog
