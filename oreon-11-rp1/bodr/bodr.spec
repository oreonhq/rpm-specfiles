%global source0_hash 738a0f0e263cdc088581d0a67a0ea16ec586ceb424704d0ff73bdb5da5d4ee81

Name:           bodr
Version:        10
Release:        28%{?dist}
Summary:        Blue Obelisk Data Repository

License:        CC0-1.0
URL:            http://www.blueobelisk.org
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  perl(diagnostics)
BuildRequires:  make
Requires:       pkgconfig

%description
The Blue Obelisk Data Repository lists many important chemoinformatics data
such as element and isotope properties, atomic radii, etc. including
references to original literature. Developers can use this repository to make
their software interoperable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

#make docs nicer
mv $RPM_BUILD_ROOT%{_docdir}/bodr DOC

%files
%doc DOC/* NEWS TODO
%{_datadir}/bodr
%{_datadir}/pkgconfig/bodr.pc

%changelog
%autochangelog
