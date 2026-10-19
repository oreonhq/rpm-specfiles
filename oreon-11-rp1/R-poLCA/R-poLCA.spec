%global source0_hash ed8c60a42bff0402c9ba2f9ce1422dd171e711c1a64498c4d96010ddb29f6b16
Name:           R-poLCA
Version:        %R_rpm_version 1.6.0.1
Release:        1%{?dist}
Summary:        Polytomous variable Latent Class Analysis
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=poLCA&version=%{version}#/poLCA_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Latent class analysis and latent class regression models for polytomous
outcome variables.  Also known as latent structure analysis.

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
