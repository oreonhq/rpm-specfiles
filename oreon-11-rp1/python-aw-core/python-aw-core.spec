%global source0_hash ba5f6d36cd5a87e6fc8fe95c43bc5ddf8309ca00df5f1e43032a62304a5a758e

%global srcname aw-core

Name:           python-%{srcname}
Version:        0.5.17
Release:        %autorelease
Summary:        Core library for ActivityWatch

License:        MPL-2.0
URL:            https://github.com/ActivityWatch/aw-core
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

Patch:          https://github.com/ActivityWatch/aw-core/pull/127.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  help2man
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Core library for ActivityWatch.}

%description %{_description}

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{srcname}-%{version}

# works also with 3.9 on f39 and 3.11 on f40, so unpinning
sed -ri 's/platformdirs = "3.10"/platformdirs = ">=3.9"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L {aw_cli,aw_core,aw_datastore,aw_transform,aw_query}
mkdir -p %{buildroot}%{_mandir}/man1
export PYTHONPATH="$PYTHONPATH:%{buildroot}%{python3_sitelib}"
help2man --no-discard-stderr %{buildroot}%{_bindir}/aw-cli -o %{buildroot}%{_mandir}/man1/aw-cli.1

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_mandir}/man1/aw-cli.1*
%{_bindir}/aw-cli

%changelog
%autochangelog
