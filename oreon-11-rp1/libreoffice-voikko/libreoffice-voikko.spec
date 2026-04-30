%global libo %{_libdir}/libreoffice
# The location of the installed extension. Apparently the directory name must
# end with .uno.pkg or unopkg will fail.
%global voikkoext %{libo}/share/extensions/voikko.uno.pkg
# The python code in this package is clearly noarch, but LibreOffice is
# arch-specific. Keeping this package arch-specific as well, for now.
%global debug_package %{nil}

# Manually byte-compile the extension files later
%global _python_bytecompile_extra 0

Name:           libreoffice-voikko
Version:        5.0
Release:        23%{?dist}
Summary:        Finnish spellchecker and hyphenator extension for LibreOffice

License:        GPL-3.0-or-later
URL:            http://voikko.puimula.org/
# The usual format of stable release URLs
Source0:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
# The usual format of test release URLs
#Source0:        http://www.puimula.org/htp/testing/%%{name}-%%{version}rc2.tar.gz
# https://github.com/voikko/libreoffice-voikko/pull/12
Patch0:         0001-make-install-unpacked-flattens-the-python-hierarchy-.patch

BuildRequires:    python3-devel
BuildRequires: make
Requires:         python3-libvoikko
Requires:         libreoffice-core%{?_isa}
Requires:         libreoffice-pyuno%{?_isa}

%description
This package contains a Finnish spell-checking and hyphenation component for
LibreOffice. The actual spell-checking and hyphenation functionality is
provided by the Voikko library.


%prep
%setup -q
%patch -P0 -p1 -b .fix.install-unpacked

%build
make extension-files %{?_smp_mflags}

%install
make install-unpacked DESTDIR=$RPM_BUILD_ROOT%{voikkoext}
%py_byte_compile %{__python3} %{buildroot}%{voikkoext}


%files
%{voikkoext}
%doc ChangeLog COPYING README

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0-23
- Prepare for Oreon 11 (RP1)
