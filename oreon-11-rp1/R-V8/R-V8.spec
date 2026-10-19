%global source0_hash d5d7da5f367e6d5dde34df73d927bad6d8b36623416c920f2570fe52b589d7ae
Name:           R-V8
Version:        %R_rpm_version 8.0.1
Release:        1%{?dist}
Summary:        Embedded JavaScript and WebAssembly Engine for R
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=V8&version=%{version}#/V8_%{version}.tar.gz
ExclusiveArch:  %{nodejs_arches}
ExcludeArch:    %{ix86}
Provides:       bundled(js-crossfilter) = 1.3.12
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  v8-devel
# /oreon:deps
%description
An R interface to V8: Google's open source JavaScript and WebAssembly engine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
