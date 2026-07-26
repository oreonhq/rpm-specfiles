%global source0_hash 560a04f85006fccd74feaa4b6213a446392ff7b5ec0194a5464b6c30f182fa33

%global srcname moreorless

%bcond_without tests

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        Python diff wrapper
License:        MIT
URL:            https://github.com/thatch/moreorless/
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist setuptools_scm}
%if %{with tests}
BuildRequires:  %{py3_dist coverage}
BuildRequires:  %{py3_dist parameterized}
%endif

%global _description %{expand:
This is a thin wrapper around difflib.unified_diff that Does The Right Thing for
"No newline at eof". The args are also simplified compared to difflib.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l moreorless

%check
%if %{with tests}
%{python3} -m coverage run -m moreorless.tests -v
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%exclude %{python3_sitelib}/%{srcname}/py.typed

%changelog
%autochangelog
