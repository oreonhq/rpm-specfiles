%global source0_hash 244e55ca485805ae2fcae8621dec7bb35e9fcd0da707271eb5ef984b88605042

Name:           R-IRanges
Version:        %R_rpm_version 2.44.0
Release:        %autorelease
Summary:        Low-level containers for storing sets of integer ranges

# See https://www.redhat.com/archives/fedora-r-devel-list/2009-April/msg00001.html
# Automatically converted from old format: Artistic 2.0 and Copyright only - review is highly recommended.
License:        Artistic-2.0 AND LicenseRef-Callaway-Copyright-only
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 2.44.0

%description
The IRanges class and its extensions are low-level containers
for storing sets of integer ranges. A typical use of these containers
in biology is for representing a set of chromosome regions.
More specific extensions of the IRanges class will typically
allow the storage of additional information attached to each
chromosome region as well as a hierarchical relationship between
these regions.

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
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
