%global source0_hash 244e55ca485805ae2fcae8621dec7bb35e9fcd0da707271eb5ef984b88605042
Name:           R-IRanges
Version:        %R_rpm_version 2.44.0
Release:        1%{?dist}
Summary:        Low-level containers for storing sets of integer ranges
License:        Artistic-2.0 AND LicenseRef-Callaway-Copyright-only
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/IRanges_2.44.0.tar.gz
Obsoletes:      %{name}-devel <= 2.44.0
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
The IRanges class and its extensions are low-level containers
for storing sets of integer ranges. A typical use of these containers
in biology is for representing a set of chromosome regions.
More specific extensions of the IRanges class will typically
allow the storage of additional information attached to each
chromosome region as well as a hierarchical relationship between
these regions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
