%global source0_hash 8e0825803c488aa2cb118ed277a18d4617984608e75d10d5bffa5e24734eb022

%global pypi_name yapf

%global desc %{expand: \
YAPF Introduction Most of the current formatters for Python e.g., autopep8, and
pep8ify are made to remove lint errors from code. This has some obvious
limitations. For instance, code that conforms to the PEP 8 guidelines may not
be}

%global forgeurl https://github.com/google/yapf

Name:           python-%{pypi_name}
Version:        0.40.2
Release:        %autorelease
Summary:        A formatter for Python code
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0

%global tag v%{version}
%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}
Patch:          fix_installed_modules.patch
Patch:          fix_tox_requirements.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel, git-core
BuildRequires:  python3dist(setuptools)
# Required for running tests
BuildRequires:  python3-importlib-metadata
BuildRequires:  python3-platformdirs

%description %{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(setuptools)
# Upstream has forked lib2to3. From their README:
# A fork of python's lib2to3 with select features backported from black's
# blib2to3.
# Reasons for forking:
# - black's fork of lib2to3 already considers newer features like
#   Structured Pattern matching
# - lib2to3 itself is deprecated and no longer getting support
# Maintenance moving forward:
# - Most changes moving forward should only have to be done to the
#   grammar files in this project.
Provides:       bundled(python3dist(lib2to3))
%description -n python3-%{pypi_name} %{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

cp plugins/README.md README-plugins.md

# Remove shebang
sed -i '/^#!/d' third_party/yapf_third_party/_ylib2to3/pgen2/token.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name} yapf_third_party

%check
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README*
%{_bindir}/yapf
%{_bindir}/yapf-diff

%changelog
%autochangelog
