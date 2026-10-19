%global source0_hash 6db69ca6ecc4fc310cd5ec2559169cbddeb5c26946663c689e84f459347b17e6
Name:           R-broom
Version:        %R_rpm_version 1.0.11
Release:        1%{?dist}
Summary:        Convert Statistical Objects into Tidy Tibbles
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=broom&version=%{version}#/broom_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Summarizes key information about statistical objects in tidy tibbles. This
makes it easy to report results, create plots and consistently work with
large numbers of models at once. Broom provides three verbs that each
provide different types of information about a model. tidy() summarizes
information about model components such as coefficients of a regression.
glance() reports information about an entire model, such as goodness of fit
measures like AIC and BIC. augment() adds information about individual
observations to a dataset, such as fitted values or influence measures.

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
