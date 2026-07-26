%global source0_hash c5e83a13af5864027af13f5d10ef29b9b7e9f5bc6d8e13d7791855667fd19c33

%global with_docs 1
%global with_check 1
%global with_django 1

%global srcname whitenoise
%global owner evansd

%if 0%{?rhel} == 9
%undefine with_check
%undefine with_django
%endif

Name:           python-%{srcname}
Version:        6.4.0
Release:        12%{?dist}
Summary:        Static file serving for Python web apps

License:        MIT
URL:            http://whitenoise.evans.io/
# pypi source does not contain tests
Source0:        https://github.com/evansd/whitenoise/archive/refs/tags/%{version}.tar.gz
Patch:          whitenoise-6.4.0-default-docs-theme.patch

BuildArch:      noarch

%description
Radically simplified static file serving for python web apps. with a couple of
lines of config whitenoise allows your web app to serve its own static files,
making it a self-contained unit that can be deployed anywhere without relying
on nginx, amazon s3 or any other external service. (Especially useful on
Heroku, OpenShift and other PaaS providers.)

%package -n python3-%{srcname}
Summary:        Static file serving for Python web apps
License:        MIT

BuildRequires:  python3-devel
BuildRequires:  python3-brotli
%if 0%{?with_django}
BuildRequires:  python3-django
%endif

#for tests
BuildRequires:  python3-pytest

%description -n python3-%{srcname}
Radically simplified static file serving for python web apps. with a couple of
lines of config whitenoise allows your web app to serve its own static files,
making it a self-contained unit that can be deployed anywhere without relying
on nginx, amazon s3 or any other external service. (especially useful on
heroku, openshift and other paas providers.)

%if 0%{?with_docs}
%package -n python3-%{srcname}-doc
Summary:        Documentation for the Python Whitenoise module
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python3-%{srcname}-doc
Documentation for the Python Whitenoise module
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
# remove dangling doc symlink
rm docs/changelog.rst
# copy common doc files to top dir
cp -pr docs/ README.rst LICENSE ../

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Build documentation
%if 0%{?with_docs}
pushd docs
sphinx-build-3 -b html -d build/doctrees . html
# remove unneeded files which create rpmlint warnings
rm -f html/.buildinfo
popd
%endif

%install
%pyproject_install

%pyproject_save_files whitenoise

%if 0%{?with_check}
%check
export DJANGO_SETTINGS_MODULE=tests.django_settings
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%if 0%{?with_docs}
%files -n python3-%{srcname}-doc
%doc docs/html
%license LICENSE
%endif

%changelog
%autochangelog
