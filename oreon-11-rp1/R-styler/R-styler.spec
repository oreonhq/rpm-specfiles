%global source0_hash f08760782b2ead047dd8f166a7cd5e01ace8d713087712bf61d193f610fbfe18

Name:           R-styler
Version:        %R_rpm_version 1.11.0
Release:        %autorelease
Summary:        Non-Invasive Pretty Printing of R Code

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Pretty-prints R code without changing the user's formatting intent.

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
