%global source0_hash a90266e5eb59c7f419774d5c6d6bd5e09701a26c9218c5933c9bce6765aa1558

Name:           R-ellipsis
Version:        %R_rpm_version 0.3.2
Release:        %autorelease
Summary:        Tools for Working with ...

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
The ellipsis is a powerful tool for extending functions. Unfortunately this
power comes at a cost: misspelled arguments will be silently ignored. The
ellipsis package provides a collection of functions to catch problems and alert
the user.

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
