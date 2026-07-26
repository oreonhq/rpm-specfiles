%global source0_hash c8a4b2bbbe751fdb3547331f4ab3b22f6d50702c9e67bb91c5356405a88ea94f

Name:           R-tinytex
Version:        %R_rpm_version 0.58
Release:        %autorelease
Summary:        Helper Functions to Install and Maintain TeX Live, and Compile LaTeX Documents

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Helper functions to install and maintain the 'LaTeX' distribution named
'TinyTeX' (<https://yihui.org/tinytex/>), a lightweight, cross-platform,
portable, and easy-to-maintain version of 'TeX Live'. This package also
contains helper functions to compile 'LaTeX' documents, and install missing
'LaTeX' packages automatically.

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
