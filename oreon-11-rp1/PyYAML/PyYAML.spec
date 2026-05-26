# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 c7b45011e052458ae79015d5eea3046c37d099023d4b253dde26ee1c29ea2f36
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           PyYAML
Version:        6.0.3
Release:        %autorelease
Summary:        YAML parser and emitter for Python

# SPDX
License:        MIT
URL:            https://github.com/yaml/pyyaml
Source:         https://github.com/yaml/pyyaml/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libyaml-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%global _description\
YAML is a data serialization format designed for human readability and\
interaction with scripting languages.  PyYAML is a YAML parser and\
emitter for Python.\
\
PyYAML features a complete YAML 1.1 parser, Unicode support, pickle\
support, capable extension API, and sensible error messages.  PyYAML\
supports standard YAML tags and provides Python-specific tags that\
allow to represent an arbitrary Python object.\
\
PyYAML is applicable for a broad range of tasks from complex\
configuration files to object serialization and persistence.

%description %_description


%package -n python3-pyyaml
Summary:        %summary
%py_provides    python3-yaml
%py_provides    python3-PyYAML

%description -n python3-pyyaml %_description


%prep
%oreon_verify_sources
%autosetup -p1 -n pyyaml-%{version}
chmod a-x examples/yaml-highlight/yaml_hl.py

# remove pre-generated file
rm -rf ext/_yaml.c


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files yaml _yaml


%check
%pytest


%files -n python3-pyyaml -f %{pyproject_files}
%doc CHANGES README.md examples


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0.3-1
- Prepare for Oreon 11 (RP1)
