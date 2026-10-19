%global source0_hash c7b45011e052458ae79015d5eea3046c37d099023d4b253dde26ee1c29ea2f36
Name:           PyYAML
Version:        6.0.3
Release:        1%{?dist}
Summary:        YAML parser and emitter for Python
License:        MIT
URL:            https://github.com/yaml/pyyaml
Source0:        https://github.com/yaml/pyyaml/archive/refs/tags/%{version}.tar.gz#/PyYAML-6.0.3.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(Cython) >= 3.0
Requires:       python3-PyYAML = %{version}-%{release}
# /oreon:deps
%description
YAML parser and emitter for Python

%package -n python3-pyyaml
Summary:        %summary
%py_provides    python3-yaml
%py_provides    python3-PyYAML
%description -n python3-pyyaml
YAML parser and emitter for Python

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n pyyaml-%{version}
chmod a-x examples/yaml-highlight/yaml_hl.py

# remove pre-generated file
rm -rf ext/_yaml.c

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyyaml usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files
%files -n python3-pyyaml -f %{oreon_filedir}/python3-pyyaml.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0.3-1
- Prepare for Oreon 11 (RP1)
