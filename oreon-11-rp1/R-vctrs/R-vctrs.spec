%global source0_hash bc10f39c766379376f7d51071be1dfb018458946c9b34014700099c0cbf24820

Name:           R-vctrs
Version:        %R_rpm_version 0.7.0
Release:        %autorelease
Summary:        Vector Helpers

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.6.5

%description
Defines new notions of prototype and size that are used to provide tools for
consistent and well-founded type-coercion and size-recycling, and are in turn
connected to ideas of type- and size-stability useful for analysing function
interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
