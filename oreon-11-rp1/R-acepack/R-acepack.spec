%global source0_hash 653093e308f0dea5ec2719985a01aff700d5795074b3f5239b34632bf45ebadf

Name:           R-acepack
Version:        %R_rpm_version 1.6.3
Release:        %autorelease
Summary:        ACE and AVAS methods for choosing regression transformations

# Automatically converted from old format: Public Domain and MIT - review is highly recommended.
License:        LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-MIT
URL:            %{cran_url}
Source:         %{cran_source}
Source:         ace-copyright.txt

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
ACE and AVAS (additivity and variance stabilization) are used to estimate 
transformations for regression.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
mkdir -p acepack/inst
cp %{SOURCE1} acepack/inst/NOTICE.txt

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
