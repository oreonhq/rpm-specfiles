%global source0_hash 51f370165c124904b907e78f6f0192b88ce2df5a93835cddd11565a328709976

Name:           R-pkgload
Version:        %R_rpm_version 1.4.1
Release:        %autorelease
Summary:        Simulate Package Installation and Attach

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Simulates the process of installing a package and then attaching it. This
is a key part of the 'devtools' package as it allows you to rapidly iterate
while developing a package.

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
