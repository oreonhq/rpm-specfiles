%global source0_hash f543eb18bd7de8893a3c0bac0e4fa5fea46a4e10f5d8182cebc40c97b8593863
Name:    freeze
Version: 2.5.0
Release:        1%{?dist}
Summary:        freeze/melt/fcat compression utilities
License:   GPL-1.0-or-later
Source0:        http://www.ibiblio.org/pub/Linux/utils/compress/freeze-%{version}.tar.gz
Source1:   Freeze_license_email.txt
Patch0:    freeze-2.5.patch
Patch1:    freeze-2.5.0-printf.patch
Patch2:    freeze-2.5.0-deffile.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Freeze is an old file compressor and decompressor that is not in
common use anymore, but can be useful if the need ever arises to
dearchive files compressed with it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp -a %{SOURCE1} .
%patch -P0 -p1 -b .Makefile
%patch -P1 -p1 -b .printf
%patch -P2 -p1 -b .deffile

%build

%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
chmod u+x configure
%configure
%make_build CFLAGS="$RPM_OPT_FLAGS -Dputc=putc"
%install
%make_install \
  DEST="%{buildroot}%{_bindir}" MANDEST="%{buildroot}%{_mandir}/man1/" \
  INSTALL_PROGRAM='install -D -p -m 0755' INSTALL_DATA='install -D -p -m 0644'
for bin in fcat melt unfreeze; do
        ln -fs freeze %{buildroot}%{_bindir}/$bin
        rm -f %{buildroot}%{_mandir}/man1/$bin.1
        ln -fs freeze.1.gz %{buildroot}%{_mandir}/man1/$bin.1.gz
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
