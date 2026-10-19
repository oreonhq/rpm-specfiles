%global source0_hash df23ff24adde68d8c095fefe890434ba69e088e14986739cab74e62cbf62a0da
Name:           R-lobstr
Version:        %R_rpm_version 1.1.3
Release:        1%{?dist}
Summary:        Visualize R Data Structures with Trees
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=lobstr&version=%{version}#/lobstr_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A set of tools for inspecting and understanding R data structures inspired by
str(). Includes ast() for visualizing abstract syntax trees, ref() for showing
shared references, cst() for showing call stack trees, and obj_size() for
computing object sizes.

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
