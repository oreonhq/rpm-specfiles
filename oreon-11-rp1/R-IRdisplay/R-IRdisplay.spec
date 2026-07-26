%global source0_hash 83eb030ff91f546cb647899f8aa3f5dc9fe163a89a981696447ea49cc98e8d2b

Name:           R-IRdisplay
Version:        %R_rpm_version 1.1
Release:        %autorelease
Summary:        'Jupyter' Display Machinery

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
 An interface to the rich display capabilities of 'Jupyter' front-ends
(e.g. 'Jupyter Notebook') <https://jupyter.org>. Designed to be used from a
running 'IRkernel' session <https://irkernel.github.io>.

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
