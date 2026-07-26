%global source0_hash 783692117346074cc8860cc16f7e8b328b05fd040e5c206a869ee351e704e917

Name:           R-docopt
Version:        %R_rpm_version 0.7.2
Release:        %autorelease
Summary:        Command-Line Interface Specification Language

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Define a command-line interface by just giving it a description in the specific
format.

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
