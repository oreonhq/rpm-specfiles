%global source0_hash 9bb97e987d486d7abd85d04cb98a53f666f02785c108647b795c4a111c5eb09f
Name:           lwtools
Version:        4.25
Release:        1%{?dist}
Summary:        Cross-development tool chain for Motorola 6809 and Hitachi 6309
License:        GPL-3.0-only
URL:            http://www.lwtools.ca/
Source0:        http://www.lwtools.ca/releases/lwtools/lwtools-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lwtools-doc -f %{oreon_filedir}/lwtools-doc.list

%changelog

%autochangelog
