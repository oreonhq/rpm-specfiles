Name:           chrpath
Version:        0.16
Release:        28%{?dist}
Summary:        Modify rpath of compiled programs

License:        GPL-2.0-or-later
URL:            https://salsa.debian.org/debian/chrpath
Source0:        https://deb.debian.org/debian/pool/main/c/chrpath/chrpath_%{version}.orig.tar.gz
# oreon url source checksums begin
%global source0_sha256 bb0d4c54bac2990e1bdf8132f2c9477ae752859d523e141e72b3b11a12c26e7b
%global source0_file chrpath_0.16.orig.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  make


%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/chrpath_0.16.orig.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bb0d4c54bac2990e1bdf8132f2c9477ae752859d523e141e72b3b11a12c26e7b" || { echo "oreon: Source0 SHA256 mismatch for chrpath_0.16.orig.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
