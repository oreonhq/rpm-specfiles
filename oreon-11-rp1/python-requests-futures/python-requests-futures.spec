%global source0_hash 6b7eb57940336e800faebc3dab506360edec9478f7b22dc570858ad3aa7458da

Name:           python-requests-futures
Version:        1.0.2
Release:        7%{?dist}
Summary:        Asynchronous Python HTTP Requests

License:        Apache-2.0
URL:            https://github.com/ross/requests-futures
Source:         %{pypi_source requests_futures}
BuildArch:      noarch

%global _description %{expand:
Small add-on for the Python requests http library. Makes use of Python 3.2’s
concurrent.futures or the back-port for prior versions of Python.}

%description %_description

%package -n python3-requests-futures
Summary:        %{summary}
Obsoletes:      python-requests-futures < 1.0.0-14

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-httpbin

%description -n python3-requests-futures %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n requests_futures-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files requests_futures

%check
%pytest -v -m 'not network'

%files -n python3-requests-futures -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
