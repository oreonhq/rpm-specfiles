%global source0_hash dd36db4cc608682500f950ee7926ab91243d2a304131f73bf4edb337bb898467

%global __pytest %{expand:expect <(echo '
    spawn /usr/bin/pytest {*}$argv
    expect default
    catch wait result
    exit [lindex $result 3]
') --}

Name:           python-invoke
Version:        3.0.3
Release:        1%{?dist}
Summary:        A Python task execution tool and library

License:        BSD-2-Clause
URL:            https://www.pyinvoke.org/
Source:         https://github.com/pyinvoke/invoke/archive/%{version}/invoke-%{version}.tar.gz

Patch1:         0001-Fix-requirements.patch
# https://github.com/pyinvoke/invoke/issues/1038
Patch2:         %{name}-SystemError.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  expect

%global _description %{expand:
Invoke is a Python task execution tool and library, drawing inspiration from
various sources to arrive at a powerful and clean feature set.}

%description %_description

%package -n python3-invoke
Summary:        %{summary}

%description -n python3-invoke %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n invoke-%{version}
# Remove bundled libs, import will fallback to system provided libs
rm -rfv invoke/vendor

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files invoke
# Backwards compatible links
ln -s inv %{buildroot}%{_bindir}/inv3
ln -s invoke %{buildroot}%{_bindir}/invoke3

%check
%pyproject_check_import
%pytest -s

%files -n python3-invoke -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/inv
%{_bindir}/inv3
%{_bindir}/invoke
%{_bindir}/invoke3

%changelog
%autochangelog
