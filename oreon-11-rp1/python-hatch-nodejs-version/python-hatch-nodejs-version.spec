%global source0_hash 2428ea398dd053f019d2b7ac949dd6b690ca8e826b6d433ad13c5b6c475ae91b
%global srcname hatch-nodejs-version
Name:           python-%{srcname}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Hatch plugin for versioning from a package.json file
License:        MIT
URL:            https://github.com/agoose77/hatch-nodejs-version
Source0:        https://files.pythonhosted.org/packages/source/h/hatch_nodejs_version/hatch_nodejs_version-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-hatch-nodejs-version = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-%{srcname}
Summary:        Hatch plugin for versioning from a package.json file
%description -n python3-%{srcname}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir hatch_nodejs_version-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/hatch_nodejs_version* usr/lib64/python3*/site-packages/hatch_nodejs_version* usr/bin/*

%check

%pytest
%files
%files -n python3-hatch-nodejs-version -f %{oreon_filedir}/python3-hatch-nodejs-version.list

%changelog

%autochangelog
