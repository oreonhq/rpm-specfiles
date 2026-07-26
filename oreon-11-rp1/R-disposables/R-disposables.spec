%global source0_hash 3af23d2c1ebe6f819b13b04cc6cbb1a1507a0c15ef867fa013f66aca2453bc60

Name:           R-disposables
Version:        %R_rpm_version 1.0.3
Release:        %autorelease
Summary:        Create Disposable R Packages for Testing

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Create disposable R packages for testing. You can create, install and load
multiple R packages with a single function call, and then unload,
uninstall and destroy them with another function call. This is handy when
testing how some R code or an R package behaves with respect to other

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
