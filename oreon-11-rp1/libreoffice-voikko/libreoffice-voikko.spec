%global source0_hash 8322b58d83eb6e1398d6914885d88a2ee08c8dd2fc2b72d75fba8fe83eefbe38
%global libo %{_libdir}/libreoffice
%global voikkoext %{libo}/share/extensions/voikko.uno.pkg
%global debug_package %{nil}
%global _python_bytecompile_extra 0
Name:           libreoffice-voikko
Version:        5.0
Release:        1%{?dist}
Summary:        Finnish spellchecker and hyphenator extension for LibreOffice
License:        GPL-3.0-or-later
URL:            http://voikko.puimula.org/
Source0:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
Patch0:         0001-make-install-unpacked-flattens-the-python-hierarchy-.patch
Requires:         python3-libvoikko
Requires:         libreoffice-core%{?_isa}
Requires:         libreoffice-pyuno%{?_isa}
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
This package contains a Finnish spell-checking and hyphenation component for
LibreOffice. The actual spell-checking and hyphenation functionality is
provided by the Voikko library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .fix.install-unpacked

%build

make extension-files %{?_smp_mflags}
%install
make install-unpacked DESTDIR=$RPM_BUILD_ROOT%{voikkoext}
%py_byte_compile %{__python3} %{buildroot}%{voikkoext}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0-23
- Prepare for Oreon 11 (RP1)
