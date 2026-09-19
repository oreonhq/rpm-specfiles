%global source0_hash 4589f8b72291329e70b7f3a8c20f2feb4e7764eebad2e6976bc9a3eee7686ce9

Name:           R-utf8
Version:        %R_rpm_version 1.2.6
Release:        %autorelease
Summary:        Unicode Text Processing

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Process and print 'UTF-8' encoded international text (Unicode). Input,
validate, normalize, encode, format, and display.

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
