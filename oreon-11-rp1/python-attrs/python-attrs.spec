# Avoid unwanted/unavailable dependencies in RHEL builds.
# Turn the tests off when bootstrapping Python, because pytest requires attrs
%bcond tests %{undefined rhel}

Name:           python-attrs
Version:        25.4.0
Release:        %autorelease
Summary:        Python attributes without boilerplate

# SPDX
License:        MIT
URL:            http://www.attrs.org/
BuildArch:      noarch
Source:         https://github.com/python-attrs/attrs/archive/%{version}/attrs-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 2bff06c2afd09911e10e8ab8126ae0eeb3d13b7fed5db66bf7e021682cc2d9f0
%global source0_file attrs-25.4.0.tar.gz
# oreon url source checksums end

BuildRequires:  python3-devel

%global _description %{expand:
attrs is an MIT-licensed Python package with class decorators that
ease the chores of implementing the most common attribute-related
object protocols.}

%description %{_description}

%package -n python3-attrs
Summary:        %{summary}

%description -n python3-attrs %{_description}

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/attrs-25.4.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2bff06c2afd09911e10e8ab8126ae0eeb3d13b7fed5db66bf7e021682cc2d9f0" || { echo "oreon: Source0 SHA256 mismatch for attrs-25.4.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n attrs-%{version}
# Remove undesired/optional test dependency on pympler
sed -i '/"pympler",/d' pyproject.toml

# Remove tests-mypy extra from tests-no-zope extra
sed -i "/attrs\[tests-mypy\]/d" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-g tests}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l attr attrs

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-attrs -f %{pyproject_files}
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.4.0-1
- Prepare for Oreon 11 (RP1)
