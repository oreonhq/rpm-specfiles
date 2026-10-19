%global source0_hash 3a55207bcfed53ddd5c5bae174524062935efed17792e9de2ad0205ce9ad63f7
Name:           python-monotonic
Version:        1.6
Release:        1%{?dist}
Summary:        An implementation of time.monotonic() for Python 2 & < 3.3
License:        Apache-2.0
URL:            https://github.com/atdt/monotonic
Source0:        https://files.pythonhosted.org/packages/source/m/monotonic/monotonic-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-monotonic = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-monotonic
Summary:        An implementation of time.monotonic() for Python 2 & < 3.3
BuildRequires:  python3-devel
Provides:       deprecated()
%description -n python3-monotonic

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir monotonic-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-monotonic usr/lib/python3*/site-packages/monotonic* usr/lib64/python3*/site-packages/monotonic* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/monotonic* usr/lib64/python3*/site-packages/monotonic* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-monotonic -f %{oreon_filedir}/python3-monotonic.list

%changelog

%autochangelog
