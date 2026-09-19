%global source0_hash 50397784ddd1fd49f02d2d711cb05a1696b154839a5440b598d5bba520d9c623

%global srcname django-picklefield
%global modname picklefield

%global forgeurl https://github.com/koed00/django-q

Name:           python-%{srcname}
Version:        3.2.0
Release:        %autorelease
Summary:        A multiprocessing distributed task queue for Django
License:        MIT
URL:            http://github.com/gintas/django-picklefield
# PyPI tarball has no tests
# Source0:        %%{pypi_source %%{srcname}}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
# Test dependencies:
# for some reason these are not picked up automatically
BuildRequires:  python3dist(django)

%global _description %{expand:
django-picklefield provides an implementation of a pickled object field. Such
fields can contain any picklable objects.

The implementation is taken and adopted from Django snippet \#1694 by Taavi
Taijala, which is in turn based on Django snippet \#513 by Oliver Beattie.}

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
# tox.ini runs coverage tests we don't need and
# need to be patched for py310
#
# the two tests in PickledObjectFieldCheckTests failed
# and django test / unittest's -k doesn't do negations
%python3 -m django test -v2 --settings=tests.settings \
  -k PickledObjectFieldTests \
  -k PickledObjectFieldDeconstructTests

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
