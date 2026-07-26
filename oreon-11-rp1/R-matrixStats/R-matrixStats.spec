%global source0_hash 12996c5f3e6fc202a43e1087f16a71b7fa93d7e908f512542c7ee89cf95dcc15

Name:           R-matrixStats
Version:        %R_rpm_version 1.5.0
Release:        %autorelease
Summary:        Functions that Apply to Rows and Columns of Matrices (and to Vectors)

License:        Artistic-2.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
High-performing functions operating on rows and columns of matrices, e.g. 
col / rowMedians(), col / rowRanks(), and col / rowSds(). Functions optimized 
per data type and for subsetted calculations such that both memory usage and 
processing time is minimized. There are also optimized vector-based methods, 
e.g. binMeans(), madDiff() and weightedMedian().

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
