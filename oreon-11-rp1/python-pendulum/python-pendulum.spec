%global source0_hash 9d9abeca83fffad7c79954de93aa7eb4af1decbd32308d35fb10b3f1dcb2aeac

%bcond tests 1

# Package an unreleased snapshot to fix Python 3.14 issues,
# https://github.com/python-pendulum/pendulum/issues/900.
%global commit 628fd8510a8956647beedc685c0f0b6bfdc1eeec
%global snapdate 20251024

Name:           python-pendulum
Version:        3.2.0~dev0^%{snapdate}git%{sub %{commit} 1 7}
Release:        2%{?dist}
Summary:        Python datetimes made easy

License:        MIT
URL:            https://pendulum.eustace.io
%global forgeurl https://github.com/sdispater/pendulum
# Source:         %%{forgeurl}/archive/%%{version}/pendulum-%%{version}.tar.gz
Source:         %{forgeurl}/archive/%{commit}/pendulum-%{commit}.tar.gz

Patch:          0001-Allow-PyO3-0.26-until-we-have-0.27-RHBZ-2404994.patch

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros
BuildRequires:  tomcli
BuildRequires:  tzdata

%if %{with tests}
# Even though there is now a [test] extra, some test dependencies are still
# only listed in [tool.poetry.group.test.dependencies].
BuildRequires:  %{py3_dist pytest}
%endif

%global common_description %{expand:
Unlike other datetime libraries for Python, Pendulum is a drop-in replacement
for the standard datetime class (it inherits from it), so, basically, you can
replace all your datetime instances by DateTime instances in you code.

It also removes the notion of naive datetimes: each Pendulum instance is
timezone-aware and by default in UTC for ease of use.}

%description %{common_description}

%package -n     python3-pendulum
Summary:        %{summary}
# Rust crates compiled into the executable contribute additional license terms.
# To obtain the following list of licenses, build the package and note the
# output of %%{cargo_license_summary}.
#
# MIT
# MIT OR Apache-2.0
License:        %{license} AND (MIT OR Apache-2.0)

Requires:       tzdata

%description -n python3-pendulum %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pendulum-%{commit} -p1
# Remove tzdata dependency. We can rely on a system-wide timezone database.
tomcli-set pyproject.toml lists delitem project.dependencies 'tzdata.*'
# Remove pytest-benchmark dependency. We don't care about it in RPM builds.
sed -i '/@pytest.mark.benchmark/d' $(find tests -type f -name '*.py')
%cargo_prep
cd rust
rm Cargo.lock
# Remove unpackaged feature. This is only needed for Windows.
tomcli-set Cargo.toml lists delitem dependencies.pyo3.features \
    'generate-import-lib'

%generate_buildrequires
# For unclear reasons, maturin checks for all crate dependencies when it is
# invoked as part of %%pyproject_buildrequires – including those corresponding
# to optional features.
#
# Since maturin always checks for dev-dependencies, we need -t so that they are
# generated even when the “check” bcond is disabled.
pushd rust >/dev/null
%cargo_generate_buildrequires -t
popd >/dev/null
%pyproject_buildrequires %{?with_tests:-x test}

%build
export RUSTFLAGS=%{shescape:%build_rustflags}

pushd rust
%cargo_license_summary
%{cargo_license} > ../LICENSES.dependencies
popd

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pendulum

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-pendulum -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
