%global source0_hash 292052fe80923aae2260c073f822ceba21f3872ced9a68bb7953b348e561179a

Name:           python-pytokens
Version:        0.4.1
Release:        %autorelease
Summary:        A fast, spec compliant Python 3.14+ tokenizer
License:        MIT
URL:            https://github.com/tusharsadhwani/pytokens
Source:         %{pypi_source pytokens}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons.}

%description %_description

%package -n python3-pytokens
Summary:        %{summary}

%description -n python3-pytokens %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n pytokens-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
export PYTOKENS_USE_MYPYC=0
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytokens

%check
%pytest --override-ini addopts=

%files -n python3-pytokens -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
