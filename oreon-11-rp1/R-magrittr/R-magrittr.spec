%global source0_hash 6aba790c40de70d8fb4d2db4bebb377418971761b0da7df2141b5d4ad95981f3
Name:           R-magrittr
Version:        %R_rpm_version 2.0.4
Release:        1%{?dist}
Summary:        Provides a mechanism for chaining commands with a new forward-pipe operator
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=magrittr&version=%{version}#/magrittr_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides a mechanism for chaining commands with a new forward-pipe operator.
This operator will forward a value, or the result of an expression, into
the next function call/expression. There is flexible support for the type of
right-hand side expressions. For more information, see package vignette. To
quote Rene Magritte, "Ceci n'est pas un pipe."

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
