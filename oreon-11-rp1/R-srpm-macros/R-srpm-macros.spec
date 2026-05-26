Name:           R-srpm-macros
Version:        1.3.7
Release:        %autorelease
Summary:        Source-stage rpm automation for R packages

License:        MIT
URL:            https://github.com/rpm-software-management/R-rpm-macros
Source0:        https://github.com/rpm-software-management/R-rpm-macros/archive/v%{version}/R-rpm-macros-%{version}.tar.gz
Patch0:         0001-tests-expect-R-4.6-ABI.patch
# oreon url source checksums begin
%global source0_sha256 2a0a297d7295a9eebe2d94c4daa3639328ea51dc984525d35e2404ef98a2e439
%global source0_file R-rpm-macros-1.3.7.tar.gz
# oreon url source checksums end

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  R-core
Requires:       redhat-rpm-config

%description
This package provides SRPM-stage rpm automation to simplify the creation
of R packages.

It limits itself to the automation subset required to create R SRPM packages
and needs to be included in the default build root.

The rest of the automation is provided by the R-rpm-macros package, that
R-srpm-macros will pull in for R packages only.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/R-rpm-macros-1.3.7.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2a0a297d7295a9eebe2d94c4daa3639328ea51dc984525d35e2404ef98a2e439" || { echo "oreon: Source0 SHA256 mismatch for R-rpm-macros-1.3.7.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n R-rpm-macros-%{version}

%install
%make_install PREFIX=%{_prefix}

%check
%make_build test OFFLINE=1

%files
%doc README.md
%license LICENSE
%{_rpmconfigdir}/macros.d/macros.R-rpm
%{_rpmconfigdir}/macros.d/macros.R-srpm
%{_rpmconfigdir}/fileattrs/R.attr
%{_rpmconfigdir}/R-deps.R
%{_rpmconfigdir}/R-files.R

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.7-1
- Import
