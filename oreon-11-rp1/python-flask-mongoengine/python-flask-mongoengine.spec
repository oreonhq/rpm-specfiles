%global source0_hash ce68726d2be8d88006e88f17e4be3b7ad07c79ca8dedb60653d3dab5d9485840

%global srcname flask-mongoengine

Name:           python-flask-mongoengine
Version:        1.0.0
Release:        14%{?dist}
Summary:        Flask extension that provides integration with MongoEngine

License:        BSD-3-Clause
URL:            https://flask-mongoengine.readthedocs.org/
Source0:        %{pypi_source}

# Flask >= 2.3 Support
# https://github.com/MongoEngine/flask-mongoengine/pull/507
# Parts are removed (tests aren't part of the tarball used here)
# And modified to apply cleanly
Patch01:        d283967f012463833c683746f86df1a2212a0eed.patch

BuildArch:      noarch

%description
A Flask extension that provides integration with MongoEngine. It handles
connection management for your app. You can also use WTForms as model forms
for your models.

%package -n python3-flask-mongoengine
Summary:        Flask extension that provides integration with MongoEngine
BuildRequires:  python3-devel

%description -n python3-flask-mongoengine
A Flask extension that provides integration with MongoEngine. It handles
connection management for your app. You can also use WTForms as model forms
for your models.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_mongoengine

%check
# No real tests except coverage tests
%py3_check_import flask_mongoengine

%files -n python3-flask-mongoengine -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
