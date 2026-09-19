%global source0_hash bf5151494508032f68ac41e211bda80da9087c65c7068ffdd12f16669bf1f2bc

Name:           R-whisker
Version:        %R_rpm_version 0.4.1
Release:        %autorelease
Summary:        {{mustache}} for R, Logicless Templating

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Implements 'Mustache' logicless templating.

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
