%global source0_hash b316d9c37177b19ce7f39ba32872d09ab600909709fd313c1e39398a4ae51287

Name:           R-diffobj
Version:        %R_rpm_version 0.3.6
Release:        %autorelease
Summary:        Diffs for R Objects

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Generate a colorized diff of two R objects for an intuitive visualization
of their differences.

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
