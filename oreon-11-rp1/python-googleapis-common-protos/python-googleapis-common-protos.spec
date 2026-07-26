%global source0_hash fb4a14e3b4f44f67fa7478a597937f36f21038ab178f538be4879956738a5f80

%bcond tests 1

# When bootstrapping, we do not include the “grpc” extra in the BR’s. That adds
# a BR on python3dist(grpcio), but this package is required by
# python3dist(grpcio-status), which creates a circular dependency with grpc.
%bcond_with bootstrap

Name:           python-googleapis-common-protos
Version:        1.63.0
Release:        %autorelease
Summary:        Common protobufs used in Google APIs

License:        Apache-2.0
URL:            https://github.com/googleapis/python-api-common-protos
Source:         %{url}/archive/v%{version}/python-api-common-protos-%{version}.tar.gz

# fix: increase upper limit for protobuf 5.X versions
# https://github.com/googleapis/python-api-common-protos/pull/212
Patch:          %{url}/pull/212.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}

%package -n python3-googleapis-common-protos
Summary:        %{summary}

%description -n python3-googleapis-common-protos %{common_description}

%pyproject_extras_subpkg -n python3-googleapis-common-protos grpc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n python-api-common-protos-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires %{?!with_bootstrap:-x grpc}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l google

%check
%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif

%files -n python3-googleapis-common-protos -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.rst

%changelog
%autochangelog
