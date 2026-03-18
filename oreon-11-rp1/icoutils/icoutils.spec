Name:           icoutils
Version:        0.32.3
Release:        20%{?dist}
Summary:        Utility for extracting and converting Microsoft icon and cursor files

License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            http://www.nongnu.org/icoutils/
Source0:        http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2

# Possible security fix, at minimum it's a DoS.
# Upstream commit d72956a6de228c91d1fc48fd15448fadea9ab6cf
Patch1:         0001-wrestool-Fix-get_resource_id_quoted-to-return-heap-a.patch
# Fix build for GCC 15
Patch2:         0002-gcc15.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext 
BuildRequires:  libpng-devel
BuildRequires:  perl-generators
BuildRequires:  make

Supplements: (kio-extras and wine-core)

Provides:       bundled(gnulib)

%description
The icoutils are a set of programs for extracting and converting images in
Microsoft Windows icon and cursor files. These files usually have the
extension .ico or .cur, but they can also be embedded in executables or
libraries.

%prep
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


%files -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS TODO ChangeLog
%{_bindir}/extresso
%{_bindir}/genresscript
%{_bindir}/icotool
%{_bindir}/wrestool
%{_mandir}/man1/*.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.32.3-20
- Prepare for Oreon 11 (RP1)
