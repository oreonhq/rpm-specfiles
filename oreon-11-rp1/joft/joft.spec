%global source0_hash 1570ac33312dae96109567eb07e6846a99d7628752d3f527f502b1d41045c371

Name:           joft
Version:        0.1.1
Release:        %autorelease
Summary:        CLI tool for automation of user actions on a JIRA instance
License:        MIT
URL:            https://github.com/mcurlej/joft
Source:         %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
JOFT is a CLI tool for automation of user actions on a JIRA instance.
This was created because the build-in automation in JIRA is not
sufficient when you want to do complex actions without having
the admin rights on the instance.}

%description %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n joft-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l joft
mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/joft.config.toml

%check
%pytest

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%{_bindir}/joft
%ghost %{_sysconfdir}/joft.config.toml

%changelog
%autochangelog
