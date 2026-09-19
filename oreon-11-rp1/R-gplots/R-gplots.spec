%global source0_hash f84c0b38d8fdbb6aa45fa81b9b21ee96f2c5891a5d37c77643977d06a66be302

Name:           R-gplots
Version:        %R_rpm_version 3.3.0
Release:        %autorelease
Summary:        Various R Programming Tools for Plotting Data

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Various R programming tools for plotting data, including:
- calculating and plotting locally smoothed summary function,
- enhanced versions of standard plots,
- manipulating colors,
- calculating and plotting two-dimensional data summaries,
- enhanced regression diagnostic plots,
- formula-enabled interface to 'stats::lowess' function,
- displaying textual data in plots,
- plotting a matrix where each cell contains a dot whose size reflects the
  relative magnitude of the elements,
- plotting "Venn" diagrams,
- displaying Open-Office style plots,
- plotting multiple data on same region, with separate axes,
- plotting means and confidence intervals,
- spacing points in an x-y plot so they don't overlap.

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
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
