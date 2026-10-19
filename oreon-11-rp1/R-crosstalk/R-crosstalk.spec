%global source0_hash 804def71ea7508cada0eec7aa6d35b487db17a8f9e38dca34fffc236691e36fc
Name:           R-crosstalk
Version:        %R_rpm_version 1.2.2
Release:        1%{?dist}
Summary:        Inter-Widget Interactivity for HTML Widgets
License:        MIT AND Apache-2.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=crosstalk&version=%{version}#/crosstalk_%{version}.tar.gz
BuildArch:      noarch
Provides:       bundled(js-bootstrap-grid) = 3.4.1
Provides:       bundled(js-IonDen-ionrangeslider) = 2.3.1
Provides:       bundled(js-jquery) = 3.5.1
Provides:       bundled(js-brianreavis-selectize) = 0.12.4
Provides:       bundled(js-samsonjs-strftime) = 0.9.2
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides building blocks for allowing HTML widgets to communicate with each
other, with Shiny or without (i.e. static .html files). Currently supports
linked brushing and filtering.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
