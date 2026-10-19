%global source0_hash 896e38a0a5321ae716f775dc7751efd8ae29c72c6dc0679325d3353663905f78
Name:           R-tkWidgets
Version:        %R_rpm_version 1.88.0
Release:        1%{?dist}
Summary:        Widgets to provide user interfaces from bioconductor
License:        Artistic-2.0
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/tkWidgets_1.88.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Widgets to provide user interfaces. tcltk should have been installed for
the widgets to run.

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
