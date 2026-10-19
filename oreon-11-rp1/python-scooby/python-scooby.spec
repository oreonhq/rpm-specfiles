%global source0_hash 407c45068cd9aa7ccc31e7371c942b27bf24c4e08771f980efc42d7bc362022a
%bcond tests 1
Name:           python-scooby
Version:        0.12.0
Release:        1%{?dist}
Summary:        A Great Dane turned Python environment detective
License:        MIT
URL:            https://github.com/banesullivan/scooby
Source0:        https://github.com/banesullivan/scooby/archive/v%{version}/scooby-%{version}.tar.gz
Source1:        scooby.1
%if %{with tests}
%endif
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
This is a lightweight tool for easily reporting your Python environment’s
package versions and hardware resources.}
# oreon:deps
BuildRequires:  /usr/bin/time
BuildRequires:  python3-devel
BuildRequires:  python3dist(psutil)
# /oreon:deps
%description %{common_description}

%package -n python3-scooby
Summary:        A Great Dane turned Python environment detective
BuildRequires:  %{py3_dist psutil}
Recommends:     %{py3_dist psutil}
%description -n python3-scooby %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n scooby-%{version} -p1

# - Omit mkl from the test dependencies because it is proprietary
# - Omit pyvips, which is not packaged (upstream CI lacks it too)
# - Omit no_version, which is not packaged; it is just a demonstration of a
#   package without a __version__. Without this, we must skip two tests; that
#   seems a reasonable price to pay in order to avoid packaging something which
#   is merely “for demonstration purposes.”
# - https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^(mkl|pyvips|no_version|pytest-cov)\b/# &/' requirements_test.txt

%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'
%oreon_autofiles python3-scooby usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
k="${k-}${k+ and }not test_get_version"
k="${k-}${k+ and }not test_tracking"
k="${k-}${k+ and }not test_import_os_error"
k="${k-}${k+ and }not test_import_time"
%pytest -k "${k-}" -v
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-scooby -f %{oreon_filedir}/python3-scooby.list

%changelog

%autochangelog
