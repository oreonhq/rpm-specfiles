%global source0_hash a53986042414bb95506e2b486e7ab27e6ea0889160cdff794b5004ee79313907

Name:           python-http-server-mock
Version:        1.7
Release:        %autorelease
Summary:        Python 3 library to mock a http server using Flask

# Please clarify GPL license version(s)
# https://github.com/ezequielramos/http-server-mock/issues/8
License:        GPL-3.0-only
URL:            https://github.com/ezequielramos/http-server-mock
Source:         %{pypi_source http_server_mock}

BuildArch:      noarch

BuildRequires:  python3-devel

# Test requirements are in requirements.txt:
#   - this file is not in the sdist
#   - it is redundant with install_requires
#   - it pins exact versions
#   - it contains unwanted coverage and linting dependencies
# It is simple enough to list manually:
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
http-server-mock is a HTTP Server Mock using Flask. You can use it to test
possible integrations with your application.}

%description %{common_description}

%package -n python3-http-server-mock
Summary:        %{summary}

%description -n python3-http-server-mock %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n http_server_mock-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l http_server_mock

%check
%pytest

%files -n python3-http-server-mock -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
