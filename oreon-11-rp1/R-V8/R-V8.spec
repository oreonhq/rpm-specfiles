%global source0_hash d5d7da5f367e6d5dde34df73d927bad6d8b36623416c920f2570fe52b589d7ae

Name:           R-V8
Version:        %R_rpm_version 8.0.1
Release:        %autorelease
Summary:        Embedded JavaScript and WebAssembly Engine for R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

ExclusiveArch:  %{nodejs_arches}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  v8-devel

# This is not packaged and it's only used to make sure example docs build when
# offline anyway.
Provides:       bundled(js-crossfilter) = 1.3.12

%description
An R interface to V8: Google's open source JavaScript and WebAssembly engine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
