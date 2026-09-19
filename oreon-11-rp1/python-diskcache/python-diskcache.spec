%global source0_hash ecd01a006c60c68171571da77d905878bacc2103a8e0ade55dcda26271ea2bb3

%global         srcname         diskcache
%global         forgeurl        https://github.com/grantjenks/python-diskcache
Version:        5.6.3
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        12%{?dist}
Summary:        Python disk-backed cache

License:        Apache-2.0
URL:            https://grantjenks.com/docs/diskcache/
# Pypi version does not have tests
Source0:        %{forgesource}

# Mitigate the risk of unsafe pickel deserialization.
# This is a modified version of the upstream patch that changes the default
# to a safe alternative.
# https://github.com/grantjenks/python-diskcache/pull/359.patch
Patch:          0001-CVE-2025-69872-unsafe-pickle.patch

BuildRequires:  python3-devel
BuildRequires:  python3-tox

BuildArch: noarch

%global _description %{expand:
DiskCache is an Apache2 licensed disk and file backed cache library,
written in pure-Python, and compatible with Django.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
# Relax test version requirement
sed -i 's/==4.2.*//g' requirements-dev.txt
sed -i 's/==4.2.*//g' tox.ini

%generate_buildrequires
%pyproject_buildrequires -e %{toxenv}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%tox -e py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
