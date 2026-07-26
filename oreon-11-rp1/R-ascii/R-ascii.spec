%global source0_hash 13459e7a6ab25014c72dc3e435c1b8685b85622aaf51cee430aeecab1918e3f2

Name:           R-ascii
Version:        %R_rpm_version 2.6
Release:        %autorelease
Summary:        Export R Objects to Several Markup Languages

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Coerce R object to asciidoc, txt2tags, restructuredText, org, textile or pandoc
syntax. Package comes with a set of drivers for Sweave.

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
