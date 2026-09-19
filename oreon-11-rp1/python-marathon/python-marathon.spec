%global source0_hash c0ac040a4b67cb649e52e897b47ba43e984c9ecff17727c9627f9dc4fb06ee0b

%global srcname marathon

Name:           python-marathon
Version:        0.13.0
Release:        15%{?dist}
Summary:        Python client library/interface to the Mesos Marathon REST API

License:        MIT
URL:            https://github.com/thefactory/marathon-python
Source0:	%url/archive/%{version}/marathon-python-%{version}.tar.gz

Patch0:		marathon-dont-use-2to3.patch
Patch1:		iterable-import-from-collections.abc.patch

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-requests-mock
BuildRequires:	pyproject-rpm-macros
%py_provides python3-%{srcname}

%description
%{summary}.

%package -n python3-%{srcname}
Summary:	%{summary}

%description -n python3-%{srcname}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n marathon-python-%{version}

# DeprecationWarning: Please use assertEqual instead
for f in tests/test_model_app.py tests/test_model_deployment.py
do
  sed -i 's/assertEquals/assertEqual/' $f
done 

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
