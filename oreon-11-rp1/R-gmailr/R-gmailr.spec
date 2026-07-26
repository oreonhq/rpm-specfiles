%global source0_hash a9f4000ca72cf37f52d13ec4e726eb3b7f8c33094ad95667e03047590b30c42e

Name:           R-gmailr
Version:        %R_rpm_version 2.0.0
Release:        %autorelease
Summary:        Access the Gmail RESTful API

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
An interface to the Gmail RESTful API.  Allows access to your Gmail
messages, threads, drafts and labels.

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
