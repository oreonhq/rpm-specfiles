%global source0_hash 540c8d1ac5d6194116abd96f12fad5d3079f82e9fbceca2704e5ecadb3e04299

# Charliecloud fedora package spec file
#
# Contributors:
#    Dave Love           @loveshack
#    Michael Jennings    @mej
#    Jordan Ogas         @jogas
#    Reid Priedhorksy    @reidpr

# Don't try to compile python3 files with /usr/bin/python.
%{?el7:%global __python %__python3}

Name:          charliecloud
Version:       0.43
Release:       1%{?dist}
Summary:       Lightweight user-defined software stacks for high-performance computing
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
URL:           https://%{name}.io/v%{version}
Source0:       https://gitlab.com/charliecloud/charliecloud/-/package_files/232789969/download#/charliecloud-%{version}.tar.gz
BuildRequires: gcc rsync bash findutils
%if 0%{?fedora} > 36
Requires:      fuse3 squashfuse cjson
BuildRequires: fuse3-libs fuse3-devel squashfuse-devel cjson-devel
%endif

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
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
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
# Suppress discarded-qualifiers warnings treated as errors, emitted by gcc on
# f44 with json.c.
export CFLAGS="$CFLAGS -Wno-error=discarded-qualifiers"
export CXXFLAGS="$CXXFLAGS -Wno-error=discarded-qualifiers"

%configure --docdir=%{_pkgdocdir} \
           --libdir=%{_prefix}/lib \
           --with-python=/usr/bin/python3 \
%if 0%{?fedora} < 37
    --with-squashfuse=no \
%else
%endif
           --with-sphinx-build=%{_bindir}/sphinx-build

%install
%set_build_flags
export CFLAGS="$CFLAGS -Wno-error=discarded-qualifiers"
export CXXFLAGS="$CXXFLAGS -Wno-error=discarded-qualifiers"
%make_install

# Remove bundled license and readme (prefer license and doc macros).
%{__rm} -f %{buildroot}%{_pkgdocdir}/LICENSE
%{__rm} -f %{buildroot}%{_pkgdocdir}/README.rst

%files
%license LICENSE
%doc README.rst
%{_bindir}/ch-checkns
%{_bindir}/ch-convert
%{_bindir}/ch-fromhost
%{_bindir}/ch-run-oci
%{_bindir}/ch-run
%{_mandir}/man1/ch-checkns.1*
%{_mandir}/man1/ch-convert.1*
%{_mandir}/man1/ch-fromhost.1*
%{_mandir}/man1/ch-run-oci.1*
%{_mandir}/man1/ch-run.1*
%{_mandir}/man7/ch-completion.bash.7*
%{_mandir}/man7/charliecloud.7*
%{_prefix}/lib/%{name}/base.sh
%{_prefix}/lib/%{name}/contributors.bash
%{_prefix}/lib/%{name}/version.sh
%{_prefix}/lib/%{name}/version.txt

%files image
%{_bindir}/ch-image
%{_mandir}/man1/ch-image.1*
%{_prefix}/lib/%{name}/build.py
%{_prefix}/lib/%{name}/build_cache.py
%{_prefix}/lib/%{name}/charliecloud.py
%{_prefix}/lib/%{name}/filesystem.py
%{_prefix}/lib/%{name}/force.py
%{_prefix}/lib/%{name}/image.py
%{_prefix}/lib/%{name}/irtree.py
%{_prefix}/lib/%{name}/misc.py
%{_prefix}/lib/%{name}/modify.py
%{_prefix}/lib/%{name}/lark
%{_prefix}/lib/%{name}/lark-1.1.9.dist-info
%{_prefix}/lib/%{name}/pull.py
%{_prefix}/lib/%{name}/push.py
%{_prefix}/lib/%{name}/registry.py
%{_prefix}/lib/%{name}/version.py

%files docs
%license LICENSE
%{_pkgdocdir}/examples
%{_pkgdocdir}/html

%files test
%{_bindir}/ch-test
%{_libexecdir}/%{name}
%{_mandir}/man1/ch-test.1*

%changelog
%autochangelog
