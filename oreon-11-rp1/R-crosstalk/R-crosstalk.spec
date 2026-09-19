%global source0_hash 804def71ea7508cada0eec7aa6d35b487db17a8f9e38dca34fffc236691e36fc

Name:           R-crosstalk
Version:        %R_rpm_version 1.2.2
Release:        %autorelease
Summary:        Inter-Widget Interactivity for HTML Widgets

# See LICENSE.note for bundled licenses
# - jQuery: MIT
# - Bootstrap: MIT
# - selectize.js: Apache-2.0
# - es5-shim: MIT
# - ion.rangeSlider: MIT
# - strftime for Javascript: MIT
License:        MIT AND Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

# Check `R/controls.R` for the bundled versions:
# MIT; inst/lib/bootstrap
Provides:       bundled(js-bootstrap-grid) = 3.4.1
# MIT; inst/lib/ionrangeslider
Provides:       bundled(js-IonDen-ionrangeslider) = 2.3.1
# MIT; inst/lib/jquery
Provides:       bundled(js-jquery) = 3.5.1
# Apache-2.0; inst/lib/selectize
Provides:       bundled(js-brianreavis-selectize) = 0.12.4
# MIT; inst/lib/strftime
Provides:       bundled(js-samsonjs-strftime) = 0.9.2

%description
Provides building blocks for allowing HTML widgets to communicate with each
other, with Shiny or without (i.e. static .html files). Currently supports
linked brushing and filtering.

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
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
