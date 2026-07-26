%global source0_hash 15daf7bf2907aef8503635bc8631fce9fd75248a1fc2496825588c4bdf785c26

Name:           R-rematch
Version:        %R_rpm_version 2.0.0
Release:        %autorelease
Summary:        Match Regular Expressions with a Nicer 'API'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A small wrapper on 'regexpr' to extract the matches and captured groups
from the match of a regular expression to a character vector.

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
