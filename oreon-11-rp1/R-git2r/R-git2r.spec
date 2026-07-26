%global source0_hash 8cd4f00555c4058836275b31f3be82034c27cad05f4b0296dfc32ca5b666ccac

Name:           R-git2r
Version:        %R_rpm_version 0.36.2
Release:        %autorelease
Summary:        Provides Access to Git Repositories

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libgit2) >= 0.26.0

%description
Interface to the 'libgit2' library, which is a pure C implementation of the
'Git' core methods. Provides access to 'Git' repositories to extract data
and running some basic 'Git' commands.

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
