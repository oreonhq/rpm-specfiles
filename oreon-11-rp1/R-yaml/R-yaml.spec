%global source0_hash 80ccf3dde851133ef3e333b818a817c296c6ccdacfc4709cd466995289cd556c
Name:           R-yaml
Version:        %R_rpm_version 2.3.12
Release:        1%{?dist}
Summary:        Methods to Convert R Data to YAML and Back
License:        BSD-3-Clause AND MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=yaml&version=%{version}#/yaml_%{version}.tar.gz
ExcludeArch:    %{ix86}
Provides:       bundled(libyaml) = 0.2.5
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Implements the 'libyaml' 'YAML' 1.1 parser and emitter
(<https://pyyaml.org/wiki/LibYAML>) for R.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
