%global source0_hash 73bd696b4d4211096e0d1e382d5ce6591527d2ff400cc7ae8230f0235eed021b

Name:           R-repr
Version:        %R_rpm_version 1.1.7
Release:        %autorelease
Summary:        Serializable Representations

License:        GPL-3.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
String and binary representations of objects for several formats / mime
types.

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
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
