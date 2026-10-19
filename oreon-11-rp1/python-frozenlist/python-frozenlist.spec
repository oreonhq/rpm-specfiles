%global source0_hash 3ede829ed8d842f6cd48fc7081d7a41001a56f1f38603f9d49bf3020d59a31ad
Name:           python-frozenlist
Version:        1.8.0
Release:        1%{?dist}
Summary:        List-like structure which can be made immutable
License:        Apache-2.0
URL:            https://github.com/aio-libs/frozenlist
Source0:        https://files.pythonhosted.org/packages/source/f/frozenlist/frozenlist-%{version}.tar.gz
Patch:          0001-Downstream-only-Build-normal-wheels-in-place.patch
Patch:          %{url}/pull/723.patch
%global common_description %{expand:
FrozenList is a list-like structure which implements
collections.abc.MutableSequence, and which can be made immutable.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 47
Requires:       python3-frozenlist = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-frozenlist
Summary:        List-like structure which can be made immutable
%description -n python3-frozenlist %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n frozenlist-%{version} -p1
find . -type f -name '*.c' -print -delete
sed -r -i 's/^([[:blank:]]*)(.*[-_]cov)/\1# \2/' pytest.ini

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-frozenlist usr/lib/python3*/site-packages/frozenlist* usr/lib64/python3*/site-packages/frozenlist* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/frozenlist* usr/lib64/python3*/site-packages/frozenlist* usr/bin/*

%check

%pytest -v
%files
%files -n python3-frozenlist -f %{oreon_filedir}/python3-frozenlist.list

%changelog

%autochangelog
