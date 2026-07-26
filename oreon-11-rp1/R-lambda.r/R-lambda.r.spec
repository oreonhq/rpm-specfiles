%global source0_hash d252fee39065326c6d9f45ad798076522cec05e73b8905c1b30f95a61f7801d6

Name:           R-lambda.r
Version:        %R_rpm_version 1.2.4
Release:        %autorelease
Summary:        Modeling data with functional programming

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A language extension to efficiently write functional programs in R. Syntax
extensions include multi-part function definitions, pattern matching,
guard statements, built-in (optional) type safety.

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
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
