%global source0_hash 4c9daa7b4c07c5408b0dbc429c13153f45ec5de3d6aed083d2deafd333ba89e8

Name: sane-frontends
Version: 1.0.14
Release: 54%{?dist}
Summary: Graphical frontend to SANE
URL: http://www.sane-project.org

# Repacked the upstream source to remove bundled glibc functions
# reported here https://gitlab.com/sane-project/frontends/-/merge_requests/11
#Source0: https://ftp.sane-project.org/pub/sane/%%{name}-%%{version}/%%{name}-%%{version}.tar.gz
Source0: %{name}-%{version}-repacked.tar.gz

# Fix array subscript out of bounds errors (#133121).
# Upstream commit 5113e3de39846a8226909088ad5c1aa4969f3030 and commit
# 7336b064653026171a715dfaf803693b638c67a5 (partial)
Patch0: sane-frontends-1.0.14-array-out-of-bounds.patch
# Fix building with sane-backends >= 1.0.20.
# Upstream commit 5e96223e497538d06e18d8e84b774c4a35f654b4 (partial) and commit
# c554cfce37e37a33f94a9051afe2062c4759072b
Patch1: sane-frontends-1.0.14-sane-backends-1.0.20.patch
# Describe correct option names in xcam man page.
# Upstream commit 7e079e377174826453a1041719fb347d69d3ba5f
Patch2: sane-frontends-1.0.14-xcam-man.patch
# 1837961 - [abrt] sane-frontends: operator delete(): scanadf killed by SIGSEGV
# original PR https://gitlab.com/sane-project/frontends/-/merge_requests/1 (bz1837961)
# updated PR https://gitlab.com/sane-project/frontends/-/merge_requests/7 (bz2133813)
Patch3: frontends-scanadf-segv.patch
Patch4: sane-frontends-configure-c99.patch
Patch5: sane-frontends-c99.patch
# 2225209 - scanadf crashes when showing help for specific device
# https://gitlab.com/sane-project/frontends/-/merge_requests/12
Patch6: 0001-src-scanadf.c-Fix-segfault-when-scanadf-h-d-device.patch

License: GPL-2.0-or-later AND GPL-2.0-or-later WITH SANE-exception
# for autoconf to update configure
BuildRequires: autoconf
# gcc is no longer in buildroot by default
BuildRequires: gcc
# use for autosetup
BuildRequires: git-core
# uses make
BuildRequires: make

BuildRequires: gtk2-devel
BuildRequires: sane-backends-devel >= 1.0.19-15

%description
This packages includes the scanadf and xcam programs.

%prep
_repacked="%{name}-%{version}-repacked.tar.gz"
if test ! -f "$_repacked"; then
  curl -sfL -o _up.tar.gz "https://gitlab.com/sane-project/frontends/-/archive/%{version}/frontends-%{version}.tar.gz"
  rm -rf _sf _out && mkdir _sf _out
  tar xf _up.tar.gz -C _sf --strip-components=1
  rm -f _sf/lstat.c _sf/lstat.h _sf/mkdir.c _sf/mkdir.h _sf/readlink.c _sf/readlink.h
  ( cd _sf && tar czf "../$_repacked" . )
  rm -rf _sf _up.tar.gz
fi

test "%{source0_hash}" = "none" || { f="$_repacked"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}

%build
# have to regenerate configure, the old one caused f.e.:
# https://bugzilla.redhat.com/show_bug.cgi?id=2341321
autoconf

# added --disable-gimp - configure script was failing due missing gimp, but did not fail the build for some reason
%configure --with-gnu-ld --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --mandir=%{_mandir} --disable-gimp
%make_build

%install
%make_install

# Not xscanimage; use xsane instead.
rm -f %{buildroot}%{_bindir}/xscanimage
rm -f %{buildroot}%{_mandir}/man1/xscanimage*
rm -f %{buildroot}%{_datadir}/sane/sane-style.rc

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/scanadf
%{_bindir}/xcam
%{_mandir}/man1/scanadf.1.gz
%{_mandir}/man1/xcam.1.gz
# there is no desktop file for xcam because while it is a GUI program it is
# intended to be used from the command line

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.14-54
- Import
