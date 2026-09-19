%global source0_hash cc6c997a1f4102fed2ce75d4c6dd057c4017c2ae1c930c8b37ca51a9a22ccbe1

Name:           R-tkrplot
Version:        %R_rpm_version 0.0-30
Release:        %autorelease
Summary:        TK Rplot

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  tcl-devel < 1:9
BuildRequires:  tk-devel < 1:9

%description
Simple mechanism for placing R graphics in a Tk widget.

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
