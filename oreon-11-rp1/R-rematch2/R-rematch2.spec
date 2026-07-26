%global source0_hash fe9cbfe99dd7731a0a2a310900d999f80e7486775b67f3f8f388c30737faf7bb

Name:           R-rematch2
Version:        %R_rpm_version 2.1.2
Release:        %autorelease
Summary:        Tidy Output from Regular Expression Matching

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Wrappers on 'regexpr' and 'gregexpr' to return the match results in tidy
data frames.

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
