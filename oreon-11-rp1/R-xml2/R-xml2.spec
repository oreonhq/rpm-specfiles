%global source0_hash ed87cfa478f9e4c398288963cf7b0e1a66ba08f54d909b261a4a6c35944f50ab

Name:           R-xml2
Version:        %R_rpm_version 1.5.2
Release:        %autorelease
Summary:        Parse XML

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  libxml2-devel
Obsoletes:      %{name}-devel <= 1.5.1

%description
Work with XML files using a simple, consistent interface. Built on top of
the 'libxml2' C library.

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
