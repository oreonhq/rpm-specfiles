%global source0_hash cf730414d5d4ab387b4e9890a4b1df9d17a3903488e8da8df1cf2e11e44558cb

Name:           R-dplyr
Version:        %R_rpm_version 1.1.4
Release:        %autorelease
Summary:        A Grammar of Data Manipulation

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel < 0.8.5-4

%description
A fast, consistent tool for working with data frame like objects, both in
memory and out of memory.

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
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
