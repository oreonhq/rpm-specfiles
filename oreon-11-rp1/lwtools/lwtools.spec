%global source0_hash e18c01841be3b149b79df38a67b59c51247ec40df0740b972eb724a3a3c72869

Name:           lwtools
Version:        4.24
Release:        3%{?dist}
Summary:        Cross-development tool chain for Motorola 6809 and Hitachi 6309

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://www.lwtools.ca/
Source0:        http://www.lwtools.ca/releases/lwtools/lwtools-%{version}.tar.gz

%description
LWTOOLS is a set of cross-development tools for the Motorola 6809 and
Hitachi 6309 microprocessors. It supports assembling to raw binaries,
CoCo LOADM binaries, and a proprietary object file format for later
linking. It also supports macros and file inclusion among other things.

%package doc
Summary:        Documentation for the LWTOOLS cross-development tool chain
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

BuildRequires: make
BuildRequires:  gcc

%description doc
The complete documentation for the LWTOOLS cross-development tool chain.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export LDFLAGS=${LDFLAGS:-%__global_ldflags}
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make install PREFIX=%{buildroot}/usr LWCC_LIBBIN_FILES=''

mkdir -p %{buildroot}%{_docdir}/%{name}
mv docs/*.txt %{buildroot}%{_docdir}/%{name}
mv docs/manual %{buildroot}%{_docdir}/%{name}
cp -a 00README.txt %{buildroot}%{_docdir}/%{name}

%files
%{_bindir}/*
%dir %{_docdir}/%{name}
%license COPYING GPL3

%files doc
%{_docdir}/%{name}/*.txt
%{_docdir}/%{name}/manual

%changelog
%autochangelog
