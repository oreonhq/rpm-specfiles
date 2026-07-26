%global source0_hash e9b4dc74406f6eb8af447f22f5dbaabed6a94301e91e50142501c22c89871770

Name:           R-parsedate
Version:        %R_rpm_version 1.3.2
Release:        %autorelease
Summary:        Recognize and Parse Dates in Various Formats

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Parse dates automatically, without the need of specifying a format.  Currently
it includes the git date parser. It can also recognize and parse all ISO 8601
formats.

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
