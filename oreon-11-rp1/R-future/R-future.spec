%global source0_hash 2577bf3d0676dc4c7467e21a3925b5b907157be9d72fafa7a77f501965932fbf

Name:           R-future
Version:        %R_rpm_version 1.69.0
Release:        %autorelease
Summary:        Unified Parallel and Distributed Processing in R for Everyone

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
BuildRequires:  hostname

%description
The purpose of this package is to provide a lightweight and unified Future
API for sequential and parallel processing of R expression via futures.
The simplest way to evaluate an expression in parallel is to use `x %<-% {
expression }` with `plan(multisession)`. This package implements
sequential, multicore, multisession, and cluster futures.  With these, R
expressions can be evaluated on the local machine, in parallel a set of
local machines, or distributed on a mix of local and remote machines.
Extensions to this package implement additional backends for processing
futures via compute cluster schedulers, etc. Because of its unified API,
there is no need to modify any code in order switch from sequential on the
local machine to, say, distributed processing on a remote compute cluster.
Another strength of this package is that global variables and functions are
automatically identified and exported as needed, making it straightforward
to tweak existing code to make use of futures.

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
