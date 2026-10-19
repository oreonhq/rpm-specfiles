%global source0_hash 17abe02d043a253b68b47e3af69c9fc755b895db68fdc8811786125df564c6e0
Name:           icoutils
Version:        0.32.3
Release:        1%{?dist}
Summary:        Utility for extracting and converting Microsoft icon and cursor files
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            http://www.nongnu.org/icoutils/
Source0:        https://nongnu.uib.no/%{name}/%{name}-%{version}.tar.bz2
Patch1:        0001-wrestool-Fix-get_resource_id_quoted-to-return-heap-a.patch
Patch2:        0002-gcc15.patch
Supplements: (kio-extras and wine-core)
Provides:       bundled(gnulib)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
The icoutils are a set of programs for extracting and converting images in
Microsoft Windows icon and cursor files. These files usually have the
extension .ico or .cur, but they can also be embedded in executables or
libraries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%patch 1 -p1
%patch 2 -p1

autoreconf -fiv

for f in AUTHORS NEWS; do
  iconv -f ISO88592 -t UTF8 < $f > $f.utf8 && \
  touch -r $f $f.utf8 && \
  mv $f.utf8 $f 
done

%build

%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.32.3-20
- Import
