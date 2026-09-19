%global source0_hash f5fbb829a763c81b35571227cbeba346dee9713ff9c6c0c1a73f73256d51707c

Name:           R-XML
Version:        %R_rpm_version 3.99-0.20
Release:        %autorelease
Summary:        Tools for Parsing and Generating XML Within R and S-Plus

License:        BSD-3-Clause
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  libxml2-devel

%description
Many approaches for both reading and creating XML (and HTML) documents
(including DTDs), both local and accessible via HTTP or FTP.  Also offers
access to an XPath "interpreter".

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
