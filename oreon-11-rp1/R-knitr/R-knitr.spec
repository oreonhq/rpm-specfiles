%global source0_hash bcfa3081677ff5c3881c7cef35f3305bbf6714b01320c81a523772663741ca11

Name:           R-knitr
Version:        %R_rpm_version 1.51
Release:        %autorelease
Summary:        A General-Purpose Package for Dynamic Report Generation in R

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Recommends:     tex(framed.sty)
Recommends:     tex(listings.sty)

%description
Provides a general-purpose tool for dynamic report generation in R using
Literate Programming techniques.

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
