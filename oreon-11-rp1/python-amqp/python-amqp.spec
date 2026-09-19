%global source0_hash cddc00c725449522023bad949f70fff7b48f0b1ade74d170a6f10ab044739432

# Tests can optionally be disabled
%bcond_without tests

# These Sphinx docs do not build without sphinx_celery packaged
%bcond_with sphinx_docs

%global srcname amqp

Name:           python-%{srcname}
Version:        5.3.1
Release:        %autorelease
Summary:        Low-level AMQP client for Python (fork of amqplib)

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pypi.python.org/pypi/amqp
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%if %{with sphinx_docs}
BuildRequires:  python3-sphinx
%endif

%description
Low-level AMQP client for Python

This is a fork of amqplib, maintained by the Celery project.

This library should be API compatible with librabbitmq.

%package -n python3-%{srcname}
Summary:        Client library for AMQP
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-vine >= 5.1.0
%endif
%if %{with sphinx_docs}
BuildRequires:  python3-sphinx >= 0.8
%endif
Requires:    python3-vine >= 5.1.0

%description -n python3-%{srcname}
Low-level AMQP client for Python

This is a fork of amqplib, maintained by the Celery project.

This library should be API compatible with librabbitmq.

%package doc
Summary:        Documentation for python-amqp
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for python-amqp

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%if %{with sphinx_docs}
# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

pushd docs

# Disable extensions to prevent intersphinx from accessing net during build.
# Other extensions listed are not used.
sed -i s/^extensions/disable_extensions/ conf.py

SPHINX_DEBUG=1 sphinx-build -b html . build/html
rm -rf build/html/.doctrees build/html/.buildinfo

popd
%endif

%check
%pyproject_check_import

%if %{with tests}
%pytest t/unit
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc Changelog README.rst

%files doc
%license LICENSE
%if %{with sphinx_docs}
%doc docs/build/html docs/reference
%endif

%changelog
%autochangelog
