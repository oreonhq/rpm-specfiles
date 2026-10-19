%global source0_hash 2a0a297d7295a9eebe2d94c4daa3639328ea51dc984525d35e2404ef98a2e439
Name:           R-rpm-macros
Version:        1.3.7
Release:        1%{?dist}
Summary:        Macros to help produce R packages
License:        MIT
URL:            https://github.com/rpm-software-management/R-rpm-macros
Source0:        https://github.com/rpm-software-management/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       R-srpm-macros = %{version}-%{release}
Requires:       R-core
Requires:       rpm
# oreon:deps
BuildRequires:  R-core
BuildRequires:  make
# /oreon:deps
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
%oreon_prep
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles R-srpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n R-srpm-macros -f %{oreon_filedir}/R-srpm-macros.list

%changelog

%autochangelog

