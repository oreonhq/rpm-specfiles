%global source0_hash 1555e6c2fb67bd38ff11b479f74aa287b2d93f4add487aec53b836ff07de3a3a

Name:           R-httr
Version:        %R_rpm_version 1.4.7
Release:        %autorelease
Summary:        Tools for Working with URLs and HTTP

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Useful tools for working with HTTP organised by HTTP verbs (GET(), POST(),
etc). Configuration functions make it easy to control additional request
components (authenticate(), add_headers() and so on).

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
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
