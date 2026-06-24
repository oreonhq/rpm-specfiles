%global source0_hash none

Name:           R-rpm-macros
Version:        1.3.7
Release:        %autorelease
Summary:        Macros to help produce R packages

License:        MIT
URL:            https://github.com/rpm-software-management/R-rpm-macros
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  R-core
Requires:       R-srpm-macros = %{version}-%{release}
Requires:       R-core
Requires:       rpm

%description
This package contains the R RPM macros, that most implementations should rely
on.

You should not need to install this package manually as the R-devel package
requires it. So install the R-devel package instead.

%package -n R-srpm-macros
Summary:   Source-stage rpm automation for R packages
BuildArch: noarch
Requires:  redhat-rpm-config

%description -n R-srpm-macros
This package provides SRPM-stage rpm automation to simplify the creation
of R packages.

It limits itself to the automation subset required to create R SRPM packages
and needs to be included in the default build root.

The rest of the automation is provided by the R-rpm-macros package, that
R-srpm-macros will pull in for R packages only.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1


%install
%make_install PREFIX=%{_prefix}


%check
# not robust enough
# %%make_build test OFFLINE=1


%files
%doc README.md
%license LICENSE
%{_rpmconfigdir}/fileattrs/R.attr
%{_rpmconfigdir}/macros.d/macros.R-rpm
%{_rpmconfigdir}/R-*.R


%files -n R-srpm-macros
%doc README.md
%license LICENSE
%{_rpmconfigdir}/macros.d/macros.R-srpm


%changelog
%autochangelog

