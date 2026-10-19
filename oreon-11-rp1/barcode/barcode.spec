%global source0_hash 7c031cf3eb811242f53664379aebbdd9fae0b7b26b5e5d584c31a9f338154b64
Summary:        Generates barcodes from text strings
Name:           barcode
Version:        0.99
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.gnu.org/software/barcode/
Source0:        https://ftp.gnu.org/gnu/barcode/%{name}-%{version}.tar.gz
Patch0:         barcode-configure.patch
Patch1:         barcode-install-info.patch
Patch2:         barcode-0.98-format-security.patch
Patch3:         barcode-configure-c99.patch
Patch4:         barcode-c99.patch
# oreon:deps
BuildRequires:  /usr/bin/dvips
BuildRequires:  /usr/bin/makeinfo
BuildRequires:  /usr/bin/texindex
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  make
# /oreon:deps
%description
Barcode is meant to solve most needs in barcode creation with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Ouput is generated as either Postscript or
Encapsulated Postscript.

%package devel
Summary:        Header files and libraries for %{name} development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
%description devel
The %{name}-devel package contains the header files and libraries needed
to develop programs that use the %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export MAKEINFO=makeinfo
%configure
make -C doc clean
make # doesn't support %%{?_smp_mflags}
%install
%make_install \
  bindir=%{buildroot}%{_bindir} \
  includedir=%{buildroot}%{_includedir} \
  libdir=%{buildroot}%{_libdir} \
  mandir=%{buildroot}%{_mandir} \
  infodir=%{buildroot}%{_infodir}
%oreon_autofiles barcode-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n barcode-devel -f %{oreon_filedir}/barcode-devel.list

%changelog

%autochangelog
