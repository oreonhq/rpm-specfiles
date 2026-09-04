%global source0_hash 823df091e2d694bb4fba83ff921e590be3c106494eaac9c8a8c150b617e8b827

%global modname crank

Name:               python-crank
Version:            0.9.0
Release:            1%{?dist}
Summary:            Generalization of dispatch mechanism for use across frameworks

License:            MIT
URL:                https://pypi.io/project/crank
Source0:            https://pypi.io/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-webob

%global _description\
Generalization of dispatch mechanism for use across frameworks.

%description %_description

%package -n python3-%{modname}
Summary:            Generalization of dispatch mechanism for use across python3 web frameworks

%description -n python3-%{modname}
Generalization of dispatch mechanism for use across web frameworks.

This package provides the python3 version of this module

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

# The current upstream tarball doesn't contain the tests
#%check
#%{__python3} setup.py test

%check
%pyproject_check_import

%files -n python3-%{modname} -f %{pyproject_files}

%changelog
%autochangelog
