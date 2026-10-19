%global source0_hash e1c6d8bddc23e5039dd9c537feb371f937d60028fb753b90345698c58ae424a6
Name:           R-IRkernel
Version:        %R_rpm_version 1.3.2
Release:        1%{?dist}
Summary:        Native R Kernel for the 'Jupyter Notebook'
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=IRkernel&version=%{version}#/IRkernel_%{version}.tar.gz
ExcludeArch: %{ix86}
BuildArch:      noarch
Requires:       python-jupyter-filesystem
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  python3dist(jupyter-kernel-test)
BuildRequires:  python3dist(ndjson-testrunner)
# /oreon:deps
%description
The R kernel for the 'Jupyter' environment executes R code which the front-end
('Jupyter Notebook' or other front-ends) submits to the kernel via the network.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Remove bundled Python code
rm -r IRkernel/tests/testthat/{jkt,njr}

%build

%install
%R_install
%R_save_files
R_LIBS_USER=%{buildroot}%{_R_libdir} \
    Rscript -e 'IRkernel::installspec(prefix = "%{buildroot}%{_prefix}")'
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
