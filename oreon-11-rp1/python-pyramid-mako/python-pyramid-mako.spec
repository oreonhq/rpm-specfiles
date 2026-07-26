%global source0_hash 876ae86ccde08b40d27a57a29ad78cb0b2a890a933b9c886b89a944baf7336a3

%global modname pyramid_mako
%global srcname pyramid-mako
%global commit 50a2322554a8c058789556e3ebe3af91d0f857a6
%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
%global date 20230112

Name:               python-%{srcname}
Version:            1.1.0^%{date}%{shortcommit}
Release:            14%{?dist}
Summary:            Mako template bindings for the Pyramid web framework

License:            BSD-4-Clause
URL:                http://pypi.python.org/pypi/%{srcname}
#Source0:            %%pypi_source %%{modname}
Source0:            https://github.com/Pylons/%{modname}/archive/%{commit}/%{modname}-%{commit}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

%description
These are bindings for the Mako templating system for the Pyramid web
framework.

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname}
These are bindings for the Mako templating system for the Pyramid web
framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{commit}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

# Remove lingering .gitignore file and hidden static folder
rm docs/.gitignore
rm -rf docs/.static

# Fix BuildRequire on pytest-cover
sed -i 's|pytest-cover|pytest-cov|g' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pyproject_check_import
%pytest tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst COPYRIGHT.txt CONTRIBUTORS.txt CHANGES.txt docs/
%license LICENSE.txt

%changelog
%autochangelog
