%global source0_hash 2efa5a58c676ab3d159219a6efda7d904c6b638a659a308ca8061d4d733f65f3
Name:           R-qvalue
Version:        %R_rpm_version 2.42.0
Release:        1%{?dist}
Summary:        Q-value estimation for false discovery rate control
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/qvalue_2.42.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
It takes a list of p-values resulting from the simultaneous
testing of many hypotheses and estimates their q-values.
The q-value of a test measures the proportion of false positives
incurred (called the false discovery rate) when that particular
test is called significant. Various plots are automatically
generated, allowing one to make sensible significance cut-offs.
Several mathematical results have recently been shown on the
conservative accuracy of the estimated q-values from this software.
The software can be applied to problems in genomics, brain imaging,
astrophysics, and data mining.

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
