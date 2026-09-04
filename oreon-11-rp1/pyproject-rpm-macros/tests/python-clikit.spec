%global source0_hash 979a7442ca1be1eaa9fae3e0ab7d63828b85fd42ded2d6954340a8b926500b39

%global pypi_name clikit
Name:           python-%{pypi_name}
Version:        0.6.2
Release:        1%{?dist}
Summary:        Builds beautiful and testable command line interfaces

License:        MIT
URL:            https://github.com/sdispater/clikit
Source0:        https://files.pythonhosted.org/packages/source/c/clikit/clikit-0.3.1.tar.gz

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%description
Tests building with the poetry(-core) build backend.


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{pypi_name}-%{version}
%if 0%{?rhel}
# force the poetry-core build backend, as that is available rather than full poetry
sed -i 's/"poetry>=0.12"/"poetry-core"/' pyproject.toml
sed -i 's/"poetry.masonry.api"/"poetry.core.masonry.api"/' pyproject.toml
%endif


%generate_buildrequires
# this runtime-requires pastel<0.2 which is no longer available in Fedora
%pyproject_buildrequires -R


%build
%pyproject_wheel


%install
# Internal check that $TMPDIR is not changed
TPMDIR_original="$TMPDIR"

%pyproject_install

# Internal check that $TMPDIR is not changed
test "$TMPDIR" == "$TPMDIR_original"


%check
# Internal check that the RECORD and REQUESTED files are
# always removed in %%pyproject_wheel
test ! $(find %{buildroot}%{python3_sitelib}/ | grep -E "\.dist-info/RECORD$")
test ! $(find %{buildroot}%{python3_sitelib}/ | grep -E "\.dist-info/REQUESTED$")


%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
