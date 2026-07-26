%global source0_hash 96812bdb7a0dd99690d84e4b0a3def91389e4290f53f01919ef28a50554e31d1

Name:           R-sourcetools
Version:        %R_rpm_version 0.1.7-1
Release:        %autorelease
Summary:        Tools for Reading, Tokenizing and Parsing R Code

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.1.7

%description
Tools for the reading and tokenization of R code. The 'sourcetools' package
provides both an R and C++ interface for the tokenization of R code, and
helpers for interacting with the tokenized representation of R code.

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
