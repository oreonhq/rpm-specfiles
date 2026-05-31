%global source0_hash c65f8e2ba5522c896df2eb7256852bf0a5855109deec0f874379474ef76c1c1c

Summary: Utility to create fonts.scale files for truetype fonts
Name: ttmkfdir
Version: 3.0.9
Release: 74%{?dist}
# Only licensing attribution is in README, no version.
License: LGPL-2.0-or-later
# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
Source0: %{name}-%{version}.tar.bz2
Patch: ttmkfdir-3.0.9-cpp.patch
Patch1: ttmkfdir-3.0.9-zlib.patch
Patch2: ttmkfdir-3.0.9-fix-freetype217.patch
Patch3: ttmkfdir-3.0.9-namespace.patch
Patch4: ttmkfdir-3.0.9-fix-crash.patch
Patch5: ttmkfdir-3.0.9-warnings.patch
Patch6: ttmkfdir-3.0.9-segfaults.patch
Patch7: ttmkfdir-3.0.9-encoding-dir.patch
Patch8: ttmkfdir-3.0.9-font-scale.patch
Patch9: ttmkfdir-3.0.9-bug434301.patch
Patch10:ttmkfdir-3.0.9-freetype-header-fix2.patch
Patch11:ttmkfdir-3.0.9-fedora-ldflags.patch
Patch12:ttmkfdir-3.0.9-tag.patch
Source10: ttmkfdir.1

BuildRequires: make
BuildRequires: freetype-devel >= 2.0
BuildRequires: flex libtool
BuildRequires: bzip2-devel
BuildRequires: zlib-devel
BuildRequires: gcc-c++

%description
ttmkfdir is a utility used to create fonts.scale files in
TrueType font directories in order to prepare them for use
by the font server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%{make_build} OPTFLAGS="$RPM_OPT_FLAGS" RPM_LD_FLAGS="$RPM_LD_FLAGS -pie"

%install
%{make_install} PREFIX="%{_prefix}"
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p %{SOURCE10} %{buildroot}%{_mandir}/man1/

%files
%doc README
%{_bindir}/ttmkfdir
%{_mandir}/man1/ttmkfdir.1*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.9-74
- Import
