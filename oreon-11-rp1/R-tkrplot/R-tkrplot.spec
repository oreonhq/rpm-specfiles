%global source0_hash cc6c997a1f4102fed2ce75d4c6dd057c4017c2ae1c930c8b37ca51a9a22ccbe1
Name:           R-tkrplot
Version:        %R_rpm_version 0.0-30
Release:        1%{?dist}
Summary:        TK Rplot
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=tkrplot&version=0.0-30#/tkrplot_0.0-30.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
# /oreon:deps
%description
Simple mechanism for placing R graphics in a Tk widget.

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
