%global source0_hash 766034ab5e9728609bd240c9954d23ca0cdb881a98a31b9d3e1c8767c7b7cbb0

Name:           R-xmlparsedata
Version:        %R_rpm_version 1.0.5
Release:        %autorelease
Summary:        Parse Data of 'R' Code as an 'XML' Tree

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Convert the output of 'utils::getParseData()' to an 'XML' tree, that one
can search via 'XPath', and easier to manipulate in general.

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
