%global source0_hash 17795ff63ca767a48df95d2f4c774400c6098102dce9ffcb5db2596a6d9b68e0

Name:           R-BiocGenerics
Version:        %R_rpm_version 0.56.0
Release:        %autorelease
Summary:        Generic functions for Bioconductor

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
S4 generic functions needed by many other Bioconductor packages.

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
