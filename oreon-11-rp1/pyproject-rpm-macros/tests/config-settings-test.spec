%global source0_hash none

Name:           config-settings-test
Version:        1.0.0
Release:        1%{?dist}
Summary:        Test config_settings support

License:        MIT
URL:            ...
Source0:        config_settings_test_backend.py


%description
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -cT

cp -p %{sources} .

cat <<'EOF' >config_settings.py
"""
This is a test package
"""
EOF

cat <<'EOF' >pyproject.toml
[build-system]
build-backend = "config_settings_test_backend"
backend-path = ["."]
requires = ["flit-core", "packaging", "pip"]

[project]
name = "config_settings"
version = "%{version}"
dynamic = ["description"]
EOF


%generate_buildrequires
%pyproject_buildrequires -C abc=123 -C xyz=456 -C--option-with-dashes=1 -C--option-with-dashes=2
%{!?el9:%pyproject_buildrequires -C abc=123 -C xyz=456 -C--option-with-dashes=1 -C--option-with-dashes=2 -w}


%build
%{!?el9:%pyproject_wheel -C abc=123 -C xyz=456 -C--option-with-dashes=1 -C--option-with-dashes=2}


%changelog
* Fri May 19 2023 Maxwell G <maxwell@gtmx.me>
- Initial package
