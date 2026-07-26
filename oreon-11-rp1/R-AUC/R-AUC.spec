%global source0_hash 836b25b654a82f6ab69b86be95acc22a214da0ad06d71eab787ae1ebe721ae1f

Name:           R-AUC
Version:        %R_rpm_version 0.3.2
Release:        %autorelease
Summary:        Threshold independent performance measures for probabilistic classifiers

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
This package includes functions to compute the area under the curve of
selected measures: The area under the sensitivity curve (AUSEC), the area
under the specificity curve (AUSPC), the area under the accuracy curve
(AUACC), and the area under the receiver operating characteristic curve
(AUROC). The curves can also be visualized. Support for partial areas is

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

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
