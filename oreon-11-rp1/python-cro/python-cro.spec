%global source0_hash 71ea445208a1a4d02a7fc945fa0c60d3b10adebc03e327c734583f5777f43736

%global pypi_name cro

%global _description %{expand:
Coral Reefs Optimization (CRO) algorithm artificially simulates a coral reef, 
where different corals (which are the solutions for the considered 
optimization problem) grow and reproduce in a coral-reef, fighting with 
other corals for space and find depredation.}

Name:           python-%{pypi_name}
Version:        0.0.5.2
Release:        12%{?dist}
Summary:        An implementation of CRO metaheuristic algorithm
License:        MIT
URL:            https://github.com/VictorPelaez/coral-reef-optimization-algorithm
Source0:        %{pypi_source %{pypi_name}}

# add LICENSE from upstream -- pypi version does not contain license text
#
# License file is not distributed in sdist
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/issues/71
#
# Add the license file to MANIFEST.i
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/pull/72
Source1:        %{url}/raw/cb11d529acd929c488bb433f8bb87f5d1988d923/LICENSE.txt

# Add missing dependency on “multiprocess”
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/pull/74
Patch:          %{url}/pull/74.patch

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  dos2unix

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n %{pypi_name}-%{version}
# Fix CRNL line endings
find . -type f \( -name '*.py' -o -name '*.csv' -o -name '*.txt'  \) -print0 |
  xargs -r -t -0 dos2unix --keepdate
%autopatch -p1

# Remove shebangs from modules in site-packages. These are not executable
# in the source tarball, and lack “script-like” content.  The
# find-then-modify pattern keeps us from discarding mtimes on sources that
# do not need modification.
find cro -type f -exec \
   gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'

chmod -v a+x examples/example_*.py
%py3_shebang_fix examples
          
%generate_buildrequires
%pyproject_buildrequires

# Add LICENSE.txt to metadata
# https://github.com/VictorPelaez/coral-reef-optimization-algorithm/pull/60
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

%check
# Upstream provides no tests
%pyproject_check_import
# Also use the examples as “smoke tests”
for example in examples/example_*.py
do
  %{py3_test_envvars} %{python3} "${example}"
done
    
%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt examples/

%changelog
%autochangelog
