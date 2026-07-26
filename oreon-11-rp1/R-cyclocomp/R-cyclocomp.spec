%global source0_hash 9aff06d58bb060e23ac64337a95aebb2c69371b9de5f2549626e3e66acb5b14d

Name:           R-cyclocomp
Version:        %R_rpm_version 1.1.1
Release:        %autorelease
Summary:        Cyclomatic Complexity of R Code

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Cyclomatic complexity is a software metric (measurement), used to indicate
the complexity of a program. It is a quantitative measure of the number of
linearly independent paths through a program's source code. It was
developed by Thomas J. McCabe, Sr. in 1976.

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
