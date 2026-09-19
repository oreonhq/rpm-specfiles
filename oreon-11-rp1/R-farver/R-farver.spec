%global source0_hash 528823b95daab4566137711f1c842027a952bea1b2ae6ff098e2ca512b17fe25

Name:           R-farver
Version:        %R_rpm_version 2.1.2
Release:        %autorelease
Summary:        High Performance Colour Space Manipulation

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
The encoding of colour can be handled in many different ways, using different
colour spaces. As different colour spaces have different uses, efficient
conversion between these representations are important. The 'farver' package
provides a set of functions that gives access to very fast colour space
conversion and comparisons implemented in C++, and offers speed improvements
over the 'convertColor' function in the 'grDevices' package.

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
