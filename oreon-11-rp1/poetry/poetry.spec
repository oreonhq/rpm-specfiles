%global source0_hash 62fa2c26d716729befd8ddb95c6341835f73397642449aa0dccea1e40d9f97c4
%bcond bootstrap 0
%global common_description %{expand:
Poetry helps you declare, manage and install dependencies of Python
projects, ensuring you have the right stack everywhere.}
Name:           poetry
Summary:        Python dependency management and packaging made easy
Version:        2.4.3
Release:        1%{?dist}
License:        MIT
URL:            https://python-poetry.org/
Source0:        https://github.com/python-poetry/poetry/archive/%{version}/poetry-%{version}.tar.gz
Patch:          Patch-get_embedded_wheel-to-return-system-wheels-fro.patch
Patch:          dulwich-1.0.0.patch
BuildArch:      noarch
%if %{without bootstrap}
%endif
Requires:       python3-poetry = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 2.0
Requires:       python3-poetry = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n     python3-poetry
Summary:        Python dependency management and packaging made easy
Conflicts:      python3-virtualenv < 20.19.0-2
# oreon:reqs
Requires:       python3dist(build) (>=1.2.1
Requires:       python3dist(build) < 2.0.0)
Requires:       python3dist(cachecontrol[filecache]) (>=0.14.0
Requires:       python3dist(cachecontrol[filecache]) < 0.15.0)
Requires:       python3dist(cleo) (>=2.1.0
Requires:       python3dist(cleo) < 3.0.0)
Requires:       python3dist(dulwich) (>=0.25.0
Requires:       python3dist(dulwich) < 2)
Requires:       python3dist(fastjsonschema) (>=2.18.0
Requires:       python3dist(fastjsonschema) < 3.0.0)
Requires:       python3dist(findpython) (>=0.6.2
Requires:       python3dist(findpython) < 0.9.0)
Requires:       python3dist(installer) (>=0.7.0
Requires:       python3dist(installer) < 2.0.0)
Requires:       python3dist(keyring) (>=25.1.0
Requires:       python3dist(keyring) < 26.0.0)
Requires:       python3dist(packaging) (>=24.2)
Requires:       python3dist(pbs-installer[download,install]) (>=2025.6.10)
Requires:       python3dist(pkginfo) (>=1.12
Requires:       python3dist(pkginfo) < 2.0)
Requires:       python3dist(platformdirs) (>=3.0.0
Requires:       python3dist(platformdirs) < 5)
Requires:       python3dist(poetry-core) (==2.4.0)
Requires:       python3dist(pyproject-hooks) (>=1.0.0
Requires:       python3dist(pyproject-hooks) < 2.0.0)
Requires:       python3dist(requests) (>=2.26
Requires:       python3dist(requests) < 3.0)
Requires:       python3dist(requests-toolbelt) (>=1.0.0
Requires:       python3dist(requests-toolbelt) < 2.0.0)
Requires:       python3dist(shellingham) (>=1.5
Requires:       python3dist(shellingham) < 2.0)
Requires:       python3dist(tomli) (>=2.0.1
Requires:       python3dist(tomli) < 3.0.0)
Requires:       python3dist(tomlkit) (>=0.11.4
Requires:       python3dist(tomlkit) < 1.0.0)
Requires:       python3dist(trove-classifiers) (>=2022.5.19)
Requires:       python3dist(virtualenv) (>=20.26.6)
Requires:       python3dist(xattr) (>=1.0.0
Requires:       python3dist(xattr) < 2.0.0)
# /oreon:reqs
%description -n python3-poetry %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Drop upper bounds of some dependencies that release more frequently.
# poetry pins bery agressibly with upper bounds for not yet released versions.
sed -i -r 's/(keyring|virtualenv|fastjsonschema) \(>=([^,]+),<.*\)/\1 >= \2/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
export PYTHONPATH=%{buildroot}%{python3_sitelib}
for i in bash,bash-completion/completions,poetry fish,fish/vendor_completions.d,poetry.fish zsh,zsh/site-functions,_poetry; do IFS=","
    set -- $i
    mkdir -p %{buildroot}%{_datadir}/$2
    %{buildroot}%{_bindir}/poetry completions $1 | sed 's|%{buildroot}||g' > %{buildroot}%{_datadir}/$2/$3
done
%oreon_autofiles python3-poetry usr/lib/python3*/site-packages/poetry* usr/lib64/python3*/site-packages/poetry* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/poetry* usr/lib64/python3*/site-packages/poetry* usr/bin/*
%if %{without bootstrap}
%check

%pytest -m "not network"
%endif
%files
%files -n python3-poetry -f %{oreon_filedir}/python3-poetry.list

%changelog

%autochangelog
