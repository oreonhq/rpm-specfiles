%global source0_hash c13e86e49696d6655411fe09473c34997e49ff45e8cdf7576297b0ca71ceac3d

Name:           python-falcon
Epoch:          1
Version:        4.2.0
Release:        %autorelease
Summary:        ASGI+WSGI framework for building data plane APIs
License:        Apache-2.0
URL:            https://falconframework.org
Source:         %{pypi_source falcon}

# downstream-only patch to remove coverage build requirement
Patch:          0001-Remove-coverage-test-requirement.patch

BuildRequires:  gcc

%global common_description %{expand:
Falcon is a minimalist ASGI/WSGI framework for building mission-critical REST
APIs and microservices, with a focus on reliability, correctness, and
performance at scale.  When it comes to building HTTP APIs, other frameworks
weigh you down with tons of dependencies and unnecessary abstractions.  Falcon
cuts to the chase with a clean design that embraces HTTP and the REST
architectural style.}

%description %{common_description}

%package -n python3-falcon
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-falcon %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n falcon-%{version}

%generate_buildrequires
%pyproject_buildrequires -e mintest

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l falcon

%check
%tox -e mintest

%files -n python3-falcon -f %{pyproject_files}
%doc README.rst
%{_bindir}/falcon-bench
%{_bindir}/falcon-inspect-app
%{_bindir}/falcon-print-routes

%changelog
%autochangelog
