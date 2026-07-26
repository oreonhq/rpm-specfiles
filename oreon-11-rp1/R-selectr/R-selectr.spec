%global source0_hash e8a6f1f4cc8b91efdf8a69dd5344b112149b5c21973c7987db63be931267f165

Name:           R-selectr
Version:        %R_rpm_version 0.5-1
Release:        %autorelease
Summary:        Translate CSS Selectors to XPath Expressions

License:        BSD-3-Clause
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Translates a CSS3 selector into an equivalent XPath expression. This allows us
to use CSS selectors when working with the XML package as it can only evaluate
XPath expressions. Also provided are convenience functions useful for using CSS
selectors on XML nodes. This package is a port of the Python package
'cssselect' (<https://cssselect.readthedocs.io/>).

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
