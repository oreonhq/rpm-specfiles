%global source0_hash 80ccf3dde851133ef3e333b818a817c296c6ccdacfc4709cd466995289cd556c

Name:           R-yaml
Version:        %R_rpm_version 2.3.12
Release:        %autorelease
Summary:        Methods to Convert R Data to YAML and Back

# See `COPYING` for license breakdown.
License:        BSD-3-Clause AND MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

# Slightly patched, so can't unbundle yet.
Provides:       bundled(libyaml) = 0.2.5

%description
Implements the 'libyaml' 'YAML' 1.1 parser and emitter
(<https://pyyaml.org/wiki/LibYAML>) for R.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
