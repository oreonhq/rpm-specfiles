%global source0_hash 9efba7106b6192be290b6ea1e92f6b2fb04d8059ff364cabf9c08fba1e4dae71

Name:           python-shellingham
Version:        1.5.4
Release:        %autorelease
Summary:        Tool to detect surrounding Shell
License:        ISC
URL:            https://github.com/sarugaku/shellingham
Source0:        %{url}/archive/%{version}/shellingham-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock

%description
Shellingham detects what shell the current Python executable is running in.

%package -n     python3-shellingham
Summary:        %{summary}

%description -n python3-shellingham
Shellingham detects what shell the current Python executable is running in.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n shellingham-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l shellingham

%check
%pytest -v

%files -n python3-shellingham -f %{pyproject_files}
%doc README.rst CHANGELOG.rst

%changelog
%autochangelog
