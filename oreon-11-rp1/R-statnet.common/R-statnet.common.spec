%global source0_hash 66787cbada206c85d884af5ffa234aedec9aa96634230380322a30c7951dd33f

Name:           R-statnet.common
Version:        %R_rpm_version 4.13.0
Release:        %autorelease
Summary:        Common R Scripts and Utilities Used by the Statnet Project Software

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Non-statistical utilities used by the software developed by the Statnet
Project. They may also be of use to others.

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
