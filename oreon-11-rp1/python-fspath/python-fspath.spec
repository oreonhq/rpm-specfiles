%global source0_hash 3620ef6cd6d9657bb844dcee594270210a4ad61bce8ac5007e728809d8caac6e
Name:           python-fspath
Version:        20230629
Release:        1%{?dist}
Summary:        Handling path names and executables more comfortable
License:        AGPL-3.0-or-later
URL:            http://return42.github.io/fspath
Source0:        https://files.pythonhosted.org/packages/source/f/fspath/fspath-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fspath = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-fspath
Summary:        Handling path names and executables more comfortable
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-fspath

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fspath-%{version}

# remove shebangs
for f in fspath/{cli,debug,os_env}.py
do
    sed -i '1d' "$f"
done

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fspath usr/lib/python3*/site-packages/fspath* usr/lib64/python3*/site-packages/fspath* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fspath* usr/lib64/python3*/site-packages/fspath* usr/bin/*

%check

export TEST_TEMPDIR=$RPM_BUILD_ROOT/%{_tmppath}
%pytest tests -k "not test_download and not test_ZIP"
%files
%files -n python3-fspath -f %{oreon_filedir}/python3-fspath.list

%changelog

%autochangelog
