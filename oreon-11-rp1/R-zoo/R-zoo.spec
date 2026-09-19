%global source0_hash c0d139b7d3dee4f28202bc8d82fd76109af26530c43e39a051b1eb145d1861ea

Name:           R-zoo
Version:        %R_rpm_version 1.8-15
Release:        %autorelease
Summary:        Z's ordered observations for irregular time series

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.8.15

%description
An S3 class with methods for totally ordered indexed observations. It is
particularly aimed at irregular time series of numeric vectors/matrices and
factors. zoo's key design goals are independence of a particular index/date/
time class and consistency with with ts and base R by providing methods to
extend standard generics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
#Fix line endings
sed -i -e 's/\r//' zoo/inst/doc/zoo*.Rnw

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
