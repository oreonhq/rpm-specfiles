%global source0_hash 8314cbd9ab2256a104194f33a2925415447f91ac165891f0c5f0580cf1958c1e

%global pypi_name expecttest
%global pypi_version 0.2.1
# Upstream does not tag, this is the commit for 0.2.1
%global commit0 683b09a352cc426851adc2e3a9f46e0ab25e4dee
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global desc %{expand: \
This library implements expect tests (also known as "golden" tests).
Expect tests are a method of writing tests where instead of hard-coding
the expected output of a test, you run the test to get the output, and
the test framework automatically populates the expected output. If the
output of the test changes, you can rerun the test with the environment
variable EXPECTTEST_ACCEPT=1 to automatically update the expected output.}

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        A python test utility

License:        MIT
URL:            https://github.com/ezyang/expecttest
Source0:        %{url}/archive/%{commit0}/%{pypi_name}-%{shortcommit0}.tar.gz
BuildArch:      noarch

BuildRequires: python3dist(hypothesis)
BuildRequires: python3dist(pytest)

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        A python test utility

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{commit0}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
%pyproject_check_import
%pytest

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
