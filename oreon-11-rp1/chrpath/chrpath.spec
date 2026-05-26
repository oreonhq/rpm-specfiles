# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 bb0d4c54bac2990e1bdf8132f2c9477ae752859d523e141e72b3b11a12c26e7b
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
