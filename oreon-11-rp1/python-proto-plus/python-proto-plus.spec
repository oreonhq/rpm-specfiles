%global source0_hash dec75e8480954fbfd5ca3ceee09ad0d5fbfcb9615cc3ae4f1cd60a36c5148eb3

# tests are enabled by default
%bcond_without  tests

%global         srcname     proto-plus
%global         forgeurl    https://github.com/googleapis/proto-plus-python
Version:        1.22.3
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python wrapper around protocol buffers

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytz)
%endif

%global _description %{expand:
This is a wrapper around protocol buffers. Protocol buffers is a specification
format for APIs, such as those inside Google. This library provides protocol
buffer message classes and objects that largely behave like native Python
types.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files proto

%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTING.rst

%changelog
%autochangelog
