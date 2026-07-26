%global source0_hash cbedc98c27a9b94db1a48627a74acce53a337408ff626875d109d51ca9824a79

Name:           R-cliapp
Version:        %R_rpm_version 0.1.2
Release:        %autorelease
Summary:        Create Rich Command Line Applications

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Create rich command line applications, with colors, headings, lists, alerts,
progress bars, etc. It uses CSS for custom themes.

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
