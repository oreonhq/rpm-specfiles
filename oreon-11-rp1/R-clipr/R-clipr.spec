%global source0_hash 32c2931992fbec9c31b71de3e27059f1cbb45b4b1f45fd42e0e8dbcec6de3be9

Name:           R-clipr
Version:        %R_rpm_version 0.8.0
Release:        %autorelease
Summary:        Read and Write from the System Clipboard

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Requires:       xsel

%description
Simple utility functions to read from and write to the Windows, OS X, and
X11 clipboards.

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
