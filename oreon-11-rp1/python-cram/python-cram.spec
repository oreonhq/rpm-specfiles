%global source0_hash 7da7445af2ce15b90aad5ec4792f857cef5786d71f14377e9eb994d8b8337f2f
Name:           python-cram
Version:        0.7
Release:        27%{?dist}
Summary:        Simple testing framework for command line applications
License:        GPL-2.0-or-later
URL:            https://bitheap.org/cram/
Source0:        https://files.pythonhosted.org/packages/source/c/cram/cram-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cram = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-cram
Summary:        Simple testing framework for command line applications
%description -n python3-cram

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cram-%{version}

# Fix shebang in script for tests
%py3_shebang_fix scripts/cram

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cram usr/lib/python3*/site-packages/cram* usr/lib64/python3*/site-packages/cram* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cram* usr/lib64/python3*/site-packages/cram* usr/bin/*

%check

PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHON=%python3 scripts/cram -v tests
%files
%files -n python3-cram -f %{oreon_filedir}/python3-cram.list

%changelog

%autochangelog
