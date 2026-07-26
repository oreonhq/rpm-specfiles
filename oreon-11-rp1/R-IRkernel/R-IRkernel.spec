%global source0_hash e1c6d8bddc23e5039dd9c537feb371f937d60028fb753b90345698c58ae424a6

Name:           R-IRkernel
Version:        %R_rpm_version 1.3.2
Release:        %autorelease
Summary:        Native R Kernel for the 'Jupyter Notebook'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildArch:      noarch
BuildRequires:  R-devel
BuildRequires:  python3dist(jupyter-kernel-test)
BuildRequires:  python3dist(ndjson-testrunner)
Requires:       python-jupyter-filesystem

%description
The R kernel for the 'Jupyter' environment executes R code which the front-end
('Jupyter Notebook' or other front-ends) submits to the kernel via the network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Remove bundled Python code
rm -r IRkernel/tests/testthat/{jkt,njr}

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files
# Install the kernel spec, too.
R_LIBS_USER=%{buildroot}%{_R_libdir} \
    Rscript -e 'IRkernel::installspec(prefix = "%{buildroot}%{_prefix}")'

%check
%R_check

%files -f %{R_files}
%{_datadir}/jupyter/kernels/ir

%changelog
%autochangelog
