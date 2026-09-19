%global source0_hash 63d27fac1684f052e4ce909cffd2abb6be952a4dc53eb4abe0d3bba61db85b8e

Name:           python-unique-log-filter
Version:        0.1.0
Release:        %autorelease
Summary:        A log filter that removes duplicate log messages

License:        BSD-2-Clause
URL:            https://github.com/twizmwazin/unique_log_filter
Source:         https://github.com/twizmwazin/unique_log_filter/archive/v%{version}/unique_log_filter-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A log filter that removes duplicate log messages.}

%description %_description

%package -n     python3-unique-log-filter
Summary:        %{summary}

%description -n python3-unique-log-filter %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n unique_log_filter-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L unique_log_filter

%check
%{py3_test_envvars} %{python3} test_unique_log_filter.py

%files -n python3-unique-log-filter -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
