%global source0_hash 6aba790c40de70d8fb4d2db4bebb377418971761b0da7df2141b5d4ad95981f3

Name:           R-magrittr
Version:        %R_rpm_version 2.0.4
Release:        %autorelease
Summary:        Provides a mechanism for chaining commands with a new forward-pipe operator

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Provides a mechanism for chaining commands with a new forward-pipe operator.
This operator will forward a value, or the result of an expression, into
the next function call/expression. There is flexible support for the type of
right-hand side expressions. For more information, see package vignette. To
quote Rene Magritte, "Ceci n'est pas un pipe."

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
