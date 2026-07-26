%global source0_hash 0d24f645d7ce0daa447af1b0cff1123047f3b73cc41cf403650f469721f95173

# This package is part of the Free Electronic Lab.

Name:           mot-adms
Version:        2.3.7
Release:        15%{?dist}
Summary:        An electrical compact device models converter

# SPDX confirmed
License:        GPL-3.0-or-later
URL:            https://github.com/Qucs/ADMS

Source0:        https://github.com/Qucs/ADMS/archive/release-%{version}/adms-%{version}.tar.gz
# Fix for C23 strict prototype
# FIXME this patch actually matches what current mot-adms is doing even with C17,
# however I don't know if this behavior is what upstream intends (mtasaka)
Patch0:         adms-2.3.7-c23-func-prototype.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  flex bison
BuildRequires:  perl(XML::LibXML)
BuildRequires:  automake autoconf
BuildRequires:  libtool
BuildRequires:  git

%description
ADMS is a code generator that converts electrical compact
device models specified in high-level description language
into ready-to-compile C code for the API of spice simulators.
Based on transformations specified in XML language, ADMS
transforms Verilog-AMS code into other target languages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ADMS-release-%{version}
%patch -P0 -p1 -b .c23

%build
autoreconf -vif
%configure --enable-maintainer-mode --disable-silent-rules

make clean
make -C admsXml \
	admstpathYacc.h \
	preprocessorYacc.h \
	verilogaYacc.y \
	%{nil}
# Disabling parallel make
make -j1

%install
make INSTALL="%{_bindir}/install -p" install DESTDIR=%{buildroot}

# Remove libtool archives and static libs
find %{buildroot} -type f '(' -name '*.la' -or -name '*.a' ')' -delete
# For now, remove these .so files
find %{buildroot} -type l -name '*.so' -delete

%files
%license COPYING
%doc AUTHORS
%doc ChangeLog
%doc README.md
%doc TODO

%{_bindir}/admsCheck
%{_bindir}/admsXml

%{_libdir}/libadms*.so.*
%dir %{_includedir}/adms
%{_includedir}/adms/*.vams

%{_mandir}/man1/admsCheck.1*
%{_mandir}/man1/admsXml.1*

%changelog
%autochangelog
