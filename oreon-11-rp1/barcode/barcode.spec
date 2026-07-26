%global source0_hash 4229e19279b9787ac7e98852fa0bfd93986dce93b9cb07d93a017d68d409b635

Summary:        Generates barcodes from text strings
Name:           barcode
Version:        0.98
Release:        54%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.gnu.org/software/barcode/
Source0:        https://ftp.gnu.org/gnu/barcode/%{name}-%{version}.tar.gz
Patch0:         barcode-configure.patch
Patch1:         barcode-install-info.patch
Patch2:         barcode-0.98-format-security.patch
Patch3:         barcode-configure-c99.patch
Patch4:         barcode-c99.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{_bindir}/texindex
BuildRequires:  %{_bindir}/dvips
BuildRequires:  %{_bindir}/makeinfo
BuildRequires:  ghostscript

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

%autosetup -p1

%build
# fix definition of INFOTOHTML
export MAKEINFO=makeinfo
%configure
# rebuild all documentation
make -C doc clean
make # doesn't support %%{?_smp_mflags}

%install
%make_install \
  bindir=%{buildroot}%{_bindir} \
  includedir=%{buildroot}%{_includedir} \
  libdir=%{buildroot}%{_libdir} \
  mandir=%{buildroot}%{_mandir} \
  infodir=%{buildroot}%{_infodir}

%files
%license COPYING
%doc ChangeLog README doc/barcode.html
%{_bindir}/barcode
%{_mandir}/man1/barcode.1*
%{_infodir}/barcode.info.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_mandir}/man3/barcode.3*

%changelog
%autochangelog
