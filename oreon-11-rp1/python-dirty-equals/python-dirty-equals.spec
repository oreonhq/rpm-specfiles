%global source0_hash f4ac74ee88f2d11e2fa0f65eb30ee4f07105c5f86f4dc92b09eb1138775027c3
%bcond bootstrap 0
Name:           python-dirty-equals
Version:        0.11
Release:        1%{?dist}
Summary:        Doing dirty (but extremely useful) things with equals
License:        MIT
URL:            https://github.com/samuelcolvin/dirty-equals
Source0:        https://files.pythonhosted.org/packages/source/d/dirty_equals/dirty_equals-%{version}.tar.gz
%if %{without bootstrap}
%endif
BuildArch:      noarch
%global common_description %{expand:
The dirty-equals Python library (mis)uses the __eq__ method to make python code
(generally unit tests) more declarative and therefore easier to read and write.
You can use dirty-equals in whatever context you like, but it comes into its
own when writing unit tests for applications where you’re commonly checking the
response to API calls and the contents of a database.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dirty-equals = %{version}-%{release}
# /oreon:deps
%package -n       python3-dirty-equals+pydantic
Summary:        Metapackage for python3-dirty-equals pydantic extras
Requires:       python3-dirty-equals = %{version}-%{release}
Requires:       python3dist(pydantic) >= 2.4.2
Provides:       python3dist(dirty-equals[pydantic]) = %{version}-%{release}

%description -n python3-dirty-equals+pydantic
Metapackage for python3-dirty-equals pydantic extras.

%description %{common_description}

%package -n python3-dirty-equals
Summary:        Doing dirty (but extremely useful) things with equals
%description -n python3-dirty-equals %{common_description}

%if %{without bootstrap}
%endif

%prep

%autosetup -p1
# Erroring on DeprecationWarnings makes sense upstream, but is probably too
# strict for distribution packaging.
#
# This specifically works around:
#
# DeprecationWarning for datetime.utcfromtimestamp() in Python 3.12
# https://github.com/samuelcolvin/dirty-equals/issues/71
sed -r -i 's/^filterwarnings = "error"$/# &/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dirty-equals usr/lib/python3*/site-packages/dirty_equals* usr/lib64/python3*/site-packages/dirty_equals* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dirty_equals* usr/lib64/python3*/site-packages/dirty_equals* usr/bin/*

%check

ignore="${ignore-} --ignore=tests/test_docs.py"
%if %{with bootstrap}
ignore="${ignore-} --ignore=tests/test_other.py"
%endif
%if v"0%{?python3_version}" >= v"3.14"
k="${k-}${k+ and }not test_is_ip_true[other1-dirty1]"
k="${k-}${k+ and }not test_is_ip_true[other3-dirty3]"
%endif
TZ=UTC %pytest ${ignore-} -k "${k-}" -v
%files
%files -n python3-dirty-equals -f %{oreon_filedir}/python3-dirty-equals.list

%changelog

%autochangelog
