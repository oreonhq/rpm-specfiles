%global source0_hash 59c6eba8b1b912eb7e104f65053235604be853425ee67c152ac4e86a1f2073b4
Name:           R-R6
Version:        %R_rpm_version 2.6.1
Release:        1%{?dist}
Summary:        Classes with Reference Semantics
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=R6&version=%{version}#/R6_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
The R6 package allows the creation of classes with reference semantics,
similar to R's built-in reference classes. Compared to reference classes,
R6 classes are simpler and lighter-weight, and they are not built on S4
classes so they do not require the methods package. These classes allow
public and private members, and they support inheritance, even when the
classes are defined in different packages.

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
