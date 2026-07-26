%global source0_hash f3ce4851e1c1e388cafd5b195c8bb833cfcab13e691984066b23fe1c33887d4a

Name:           R-discretization
Version:        %R_rpm_version 1.0-1.1
Release:        %autorelease
Summary:        Data Preprocessing, Discretization for Classification

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A collection of supervised discretization algorithms. It can also
be grouped in terms of top-down or bottom-up, implementing
the discretization algorithms.

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
