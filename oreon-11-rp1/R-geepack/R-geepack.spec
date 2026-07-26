%global source0_hash 6ef0ee6876fbbed01ecf5c6150ad2d38709fcb83560b7acd5860e381371ae1d6

Name:           R-geepack
Version:        %R_rpm_version 1.3.13
Release:        %autorelease
Summary:        Generalized Estimating Equation Package

License:        GPL-3.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.3.13

%description
Generalized estimating equations solver for parameters in mean, scale, and
correlation structures, through mean link, scale link, and correlation
link. Can also handle clustered categorical responses.

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
