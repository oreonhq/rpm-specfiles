%global source0_hash 13ad0bc8f16522084b34bfb718b3a808e2766ee243787c5229cc629c29c1ecab

Name:           python-wurlitzer
Version:        3.1.1
Release:        %autorelease
Summary:        Capture C-level output in context managers

License:        MIT
URL:            https://github.com/minrk/wurlitzer
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/wurlitzer-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -l wurlitzer

BuildRequires:  %{py3_dist pytest}

%description
Capture C-level stdout/stderr pipes in Python via os.dup2.

%package -n     python3-wurlitzer
Summary:        %{summary}

%description -n python3-wurlitzer
Capture C-level stdout/stderr pipes in Python via os.dup2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n wurlitzer-%{version}

%check
%pytest -v test.py

%files -n python3-wurlitzer -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
