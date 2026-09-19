%global source0_hash 474d3530b16b76a1bf1a1114d24092678ea7215fa57c6fdcee6333f1e768b865

Name:           R-ica
Version:        %R_rpm_version 1.0-3
Release:        %autorelease
Summary:        Independent Component Analysis

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Independent Component Analysis (ICA) using various algorithms:
FastICA, Information-Maximization (Infomax), and Joint
Approximate Diagonalization of Eigenmatrices (JADE).

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
