%global source0_hash fc673560595ebe4687d314934be2810b7ac5167742a80659246149791abb59ba

Name:           R-units
Version:        %R_rpm_version 1.0-0
Release:        %autorelease
Summary:        Measurement Units for R Vectors

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  udunits2-devel
Obsoletes:      %{name}-devel < 0.6.3
Recommends:     R-xml2

%description
Support for measurement units in R vectors, matrices and arrays: automatic
propagation, conversion, derivation and simplification of units; raising
errors in case of unit incompatibility. Compatible with the POSIXct, Date
and difftime classes. Uses the UNIDATA udunits library and unit database
for unit compatibility checking and conversion.
Documentation about 'units' is provided in the paper by Pebesma, Mailund
& Hiebert (2016, <doi:10.32614/RJ-2016-061>), included in this package as
a vignette; see 'citation("units")' for details.

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
