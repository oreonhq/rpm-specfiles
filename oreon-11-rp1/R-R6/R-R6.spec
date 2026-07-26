%global source0_hash 59c6eba8b1b912eb7e104f65053235604be853425ee67c152ac4e86a1f2073b4

Name:           R-R6
Version:        %R_rpm_version 2.6.1
Release:        %autorelease
Summary:        Classes with Reference Semantics

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
The R6 package allows the creation of classes with reference semantics,
similar to R's built-in reference classes. Compared to reference classes,
R6 classes are simpler and lighter-weight, and they are not built on S4
classes so they do not require the methods package. These classes allow
public and private members, and they support inheritance, even when the
classes are defined in different packages.

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
