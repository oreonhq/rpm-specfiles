%global source0_hash c2726ad155cb4dae842b0aeccf3ee2e53306cd4f99a79f6c18450cbb92d7758c

Name:           R-wavethresh
Version:        %R_rpm_version 4.7.3
Release:        %autorelease
Summary:        R module, Software to perform wavelet statistics and transforms

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Software to perform 1-d and 2-d wavelet statistics and transforms

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
