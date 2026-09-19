%global source0_hash 47aac79f889a828a5f8b4756cb972d7c2966bb984cbae17a4bd2389a73270794

Name:           R-evaluate
Version:        %R_rpm_version 1.0.5
Release:        %autorelease
Summary:        Parsing and Evaluation Tools that Provide More Details than the Default

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Parsing and evaluation tools that make it easy to recreate the command line
behaviour of R.

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
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
