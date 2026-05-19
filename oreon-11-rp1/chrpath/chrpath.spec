Name:           chrpath
Version:        0.16
Release:        28%{?dist}
Summary:        Modify rpath of compiled programs

License:        GPL-2.0-or-later
URL:            https://salsa.debian.org/debian/chrpath
Source0:        https://deb.debian.org/debian/pool/main/c/chrpath/chrpath_%{version}.orig.tar.gz

BuildRequires:  gcc
BuildRequires:  make


%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
%autosetup -p1

%build
%configure
%make_build

%check
make check

%install
%make_install
rm -fr %{buildroot}/usr/doc


%files
%doc AUTHORS README NEWS ChangeLog*
%license COPYING
%{_bindir}/chrpath
%{_mandir}/man1/chrpath.1*



%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16-28
- Prepare for Oreon 11 (RP1)
