%global source0_hash e90d14284001963325a84a9dbeef029609d52515da8d65c87ae61be21b7fe0a7

Name:           R-highr
Version:        %R_rpm_version 0.11
Release:        %autorelease
Summary:        Syntax Highlighting for R Source Code

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides syntax highlighting for R source code. Currently it supports LaTeX and
HTML output. Source code of other languages is supported via Andre Simon's
highlight package (<http://www.andre-simon.de>).

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
