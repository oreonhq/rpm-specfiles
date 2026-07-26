%global source0_hash 896e38a0a5321ae716f775dc7751efd8ae29c72c6dc0679325d3353663905f78

Name:           R-tkWidgets
Version:        %R_rpm_version 1.88.0
Release:        %autorelease
Summary:        Widgets to provide user interfaces from bioconductor

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Widgets to provide user interfaces. tcltk should have been installed for
the widgets to run.

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
