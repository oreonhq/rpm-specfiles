%global source0_hash af42e649c06e4bbdba94d5a1870a7e8347903571c90cd5e5ca40f52307a3bfd6

Name:           R-rex
Version:        %R_rpm_version 1.2.1
Release:        %autorelease
Summary:        Friendly Regular Expressions

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A friendly interface for the construction of regular expressions.

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
