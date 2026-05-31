%global source0_hash bb0d4c54bac2990e1bdf8132f2c9477ae752859d523e141e72b3b11a12c26e7b

Name:           chrpath
Version:        0.16
Release:        28%{?dist}
Summary:        Modify rpath of compiled programs

License:        GPL-2.0-or-later
URL:            https://salsa.debian.org/debian/chrpath
Source0:        https://alioth.debian.org/frs/download.php/file/3979/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make


%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
