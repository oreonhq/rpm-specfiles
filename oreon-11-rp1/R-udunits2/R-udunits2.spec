%global source0_hash 3e6dc4a12c155fa3e77f982084adbd6cb75d7a106d0b1a49ddc50a17fa4d045b

Name:           R-udunits2
Version:        %R_rpm_version 0.13.2.2
Release:        %autorelease
Summary:        Udunits-2 Bindings for R

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  udunits2-devel

%description
Provides simple bindings to Unidata's udunits library.

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
