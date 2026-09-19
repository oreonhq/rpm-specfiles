%global source0_hash f6fc13887d096ba444fb722ef34cc88e079fc18be9668ffead1ba586a30b1c74

Name:           R-tinytest
Version:        %R_rpm_version 1.4.1
Release:        %autorelease
Summary:        Lightweight and Feature Complete Unit Testing Framework

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a lightweight (zero-dependency) and easy to use unit testing
framework. Main features: install tests with the package. Test results are
treated as data that can be stored and manipulated. Test files are R scripts
interspersed with test commands, that can be programmed over. Fully automated
build-install-test sequence for packages. Skip tests when not run locally (e.g.
on CRAN). Flexible and configurable output printing. Compare computed output
with output stored with the package. Run tests in parallel.  Extensible by
other packages. Report side effects.

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
