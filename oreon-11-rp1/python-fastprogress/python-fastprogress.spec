%global source0_hash 89e28ac1d2a5412aab18ee3f3dfd1ee8b5c1f2f7a44d0add0d0d4f69f0191bfe

%global srcname fastprogress

Name: python-%{srcname}
Version: 1.0.0
Release: %autorelease
Summary: Progress bar for Jupyter Notebook and console 

License: Apache-2.0
URL: https://github.com/AnswerDotAI/fastprogress
Source0: %{pypi_source}

BuildArch: noarch

%global _description %{expand:
A Python-based, fast and simple progress bar 
for Jupyter Notebook and console.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{srcname}

%check
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
