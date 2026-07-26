%global source0_hash 893f111d31deccd2cc959bc9db7ba2ce9020a2dd1b9c1c009587e449c4cce1a1

Name:           R-viridisLite
Version:        %R_rpm_version 0.4.2
Release:        %autorelease
Summary:        Colorblind-Friendly Color Maps (Lite Version)

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Color maps designed to improve graph readability for readers with common
forms of color blindness and/or color vision deficiency. The color maps are
also perceptually-uniform, both in regular form and also when converted to
black-and-white for printing. This is the 'lite' version of the 'viridis'
package that also contains 'ggplot2' bindings for discrete and continuous
color and fill scales and can be found at
<https://cran.r-project.org/package=viridis>.

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
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
