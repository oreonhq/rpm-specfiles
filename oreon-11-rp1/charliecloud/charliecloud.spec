%global source0_hash 540c8d1ac5d6194116abd96f12fad5d3079f82e9fbceca2704e5ecadb3e04299
%{?el7:%global __python %__python3}
Name:          charliecloud
Version:       0.43
Release:        1%{?dist}
Summary:        Lightweight user-defined software stacks for high-performance computing
License:       Apache-2.0
URL:           https://%{name}.io/v%{version}
Source0:        https://gitlab.com/charliecloud/charliecloud/-/package_files/232789969/download#/charliecloud-%{version}.tar.gz
# oreon:deps
BuildRequires:  bash
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-requests
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  rsync
# /oreon:deps
%description
Charliecloud uses Linux user namespaces to run containers with no privileged
operations or daemons and minimal configuration changes on center resources.
This simple approach avoids most security risks while maintaining access to
the performance and functionality already on offer.

Container images can be built using Docker or anything else that can generate
a standard Linux filesystem tree.

For more information: https://charliecloud.io

%package       docs
Summary:       Charliecloud man pages
License:       BSD and ASL 2.0
BuildArch:     noarch
Obsoletes:     %{name}-docs < %{version}-%{release}
BuildRequires: python%{python3_pkgversion}-sphinx
BuildRequires: python%{python3_pkgversion}-sphinx_rtd_theme
%description docs
Html and man page documentation for %{name}.

%package image
Summary:       Charliecloud container image manipulation tools
License:       ASL 2.0 and MIT
BuildRequires: python3-devel
BuildRequires: python%{python3_pkgversion}-requests
Requires:      %{name}
Requires:      python3
Requires:      python%{python3_pkgversion}-requests
Requires:      git >= 2.28.1
Provides:      bundled(python%{python3_pkgversion}-lark-parser) = 1.1.9
%description image
This package provides ch-image, Charliecloud's completely unprivileged container
image manipulation tool.

%package   test
Summary:   Charliecloud test suite
License:   Apache-2.0
Requires:  %{name} %{name}-image
Requires:  bats
Obsoletes: %{name}-test < %{version}-%{release}
%description test
Test fixtures for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%set_build_flags
export CFLAGS="$CFLAGS -Wno-error=discarded-qualifiers"
export CXXFLAGS="$CXXFLAGS -Wno-error=discarded-qualifiers"
%configure --docdir=%{_pkgdocdir} \
           --libdir=%{_prefix}/lib \
           --with-python=/usr/bin/python3 \
           --with-sphinx-build=%{_bindir}/sphinx-build
%install
%set_build_flags
export CFLAGS="$CFLAGS -Wno-error=discarded-qualifiers"
export CXXFLAGS="$CXXFLAGS -Wno-error=discarded-qualifiers"
%make_install
%{__rm} -f %{buildroot}%{_pkgdocdir}/LICENSE
%{__rm} -f %{buildroot}%{_pkgdocdir}/README.rst
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n charliecloud-docs -f %{oreon_filedir}/charliecloud-docs.list
%files -n charliecloud-image -f %{oreon_filedir}/charliecloud-image.list
%files -n charliecloud-test -f %{oreon_filedir}/charliecloud-test.list

%changelog

%autochangelog
