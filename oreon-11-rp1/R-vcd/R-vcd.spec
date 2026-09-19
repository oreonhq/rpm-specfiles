%global source0_hash 9dac62ace393ef6e56a1f5fa8909081350d2f9f46e47ea6f78759d41a81df8cc

Name:           R-vcd
Version:        %R_rpm_version 1.4-13
Release:        %autorelease
Summary:        Visualizing categorical data

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Visualization techniques, data sets, summary and inference procedures aimed
particularly at categorical data. Special emphasis is given to highly
extensible grid graphics. The package was package was originally inspired
by the book "Visualizing Categorical Data" by Michael Friendly and is now
the main support package for a new book, "Discrete Data Analysis with R"
by Michael Friendly and David Meyer (2015).

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
