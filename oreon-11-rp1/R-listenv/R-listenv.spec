%global source0_hash 6eddc1a201b67b61754a4f18c5d5b641f116b7a0981d8cce506d3989bcb4d6e4

Name:           R-listenv
Version:        %R_rpm_version 0.10.0
Release:        %autorelease
Summary:        Environments Behaving (Almost) as Lists

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
List environments are environments that have list-like properties.  For
instance, the elements of a list environment are ordered and can be
accessed and iterated over using index subsetting, e.g. 'x <- listenv(a =
1, b = 2); for (i in seq_along(x)) x[[i]] <- x[[i]] ^ 2; y <- as.list(x)'.

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
