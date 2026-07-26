%global source0_hash e632ced994333fa7e1de7ae8a5259ad69aa4718b27e1387153461cefb119f4d5

%global svn_revision 3674
%global svn_date 20250422

Name:           kBuild
Version:        0.1.9998%{?svn_revision:.r%{svn_revision}}
Release:        3%{?svn_date:.%{svn_date}}%{?dist}
Summary:        A cross-platform build environment

# Automatically converted from old format: BSD and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later
# most tools are from NetBSD, some are from FreeBSD,
# and make and sed are from GNU
URL:            http://svn.netlabs.org/kbuild
#Generated with kBuild-snapshot.sh
Source0:        kBuild-r%{svn_revision}.%{svn_date}.tar.gz
Patch0:         kBuild-0.1.3-escape.patch
Patch1:         kBuild-pthread.patch
Patch6:         kbuild-dummy_noreturn.diff
Patch8:         kBuild-0.1.9998-portme.patch
Patch10:        assert.patch
Patch11:        relax_automake_version.patch
Patch14:        changeset_3572.diff
Patch15:        changeset_trunk_3566.diff
Patch16:        kBuild-c23.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  flex
BuildRequires:  libacl-devel
BuildRequires:  texinfo
BuildRequires:  byacc

%description
This is a GNU make fork with a set of scripts to simplify
complex tasks and portable versions of various UNIX tools to
ensure cross-platform portability.

It is used mainly to build VirtualBox packages for RPM Fusion
repository.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%dnl %setup -q -n %{name}-%{version}%{?patchlevel:-%{patchlevel}}
%setup -q -n %{name}
%patch -P0 -p1 -b .escape
%patch -P1 -p1 -b .pthreads
%patch -P6 -p1 -b .dummy_noreturn
%ifarch ppc64
%if 0%{?rhel} && 0%{?rhel} < 7
# Found the reason why compile fails in detection of powerpc64 in centos 6
# kBuild/src/lib/kStuff/include/k/kDefs.h:356:4: error: #error "Port Me or define K_ENDIAN."
# hack for gcc < 4.6 and ppc64 only
# https://stackoverflow.com/a/40675229/778517
%patch -P8 -p1 -b .portme
%endif
%endif
%patch -P10 -p1 -b .portme3
%if 0%{?rhel} && 0%{?rhel} <= 7
%patch -P11 -p1
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
# we need revert this 2 commits to build VBox 6 on el7
%patch -P14 -p1 -R -b .revert
%patch -P15 -p1 -R -b .revert2
%endif
%patch -P16 -p1

%build
echo KBUILD_SVN_URL := http://svn.netlabs.org/repos/kbuild/trunk  >  SvnInfo.kmk
echo KBUILD_SVN_REV := %{svn_revision} >>  SvnInfo.kmk

%define bootstrap_mflags %{_smp_mflags} \\\
        CFLAGS="%{optflags}"            \\\
        KBUILD_VERBOSE=2                \\\
        KBUILD_VERSION_PATCH=9998

%define mflags %{bootstrap_mflags}      \\\
        NIX_INSTALL_DIR=%{_prefix}      \\\
        BUILD_TYPE=release              \\\
        MY_INST_MODE=0644               \\\
        MY_INST_BIN_MODE=0755

# The bootstrap would probably not be needed if we depended on ourselves,
# yet it is not guarranteed that new versions are compilable with older
# kmk versions, so with this we are on a safer side
find -name config.log -delete
kBuild/env.sh --full make -f bootstrap.gmk %{bootstrap_mflags}
kBuild/env.sh kmk %{mflags} rebuild

%install
export KBUILD_VERBOSE=2
kBuild/env.sh kmk %{mflags} PATH_INS=%{buildroot} install
# These are included later in files section
rm -r %{buildroot}%{_docdir}
mkdir -p %{buildroot}/%{_mandir}/man1
pod2man -c 'kBuild for Fedora/EPEL GNU/Linux' \
  -r kBuild-%{version} ./dist/debian/kmk.pod > %{buildroot}/%{_mandir}/man1/kmk.1

%files
%doc ChangeLog kBuild/doc/QuickReference*
%license COPYING kBuild/doc/COPYING-FDL-1.3
%{_bindir}/*
%{_datadir}/kBuild
%{_mandir}/man1/*

%changelog
%autochangelog
