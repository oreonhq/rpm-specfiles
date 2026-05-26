# =============================================================================

Name:             poppler-data
Summary:          Encoding files for use with poppler
Version:          0.4.11
Release:          11%{?dist}

# NOTE: The licensing details are explained in COPYING file in source archive.
# Makefile is HPND-sell-variant but is not included in binary package
License:          (GPL-2.0-only OR GPL-3.0-only) AND BSD-3-Clause

URL:              https://poppler.freedesktop.org/
Source:           https://poppler.freedesktop.org/poppler-data-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 2cec05cd1bb03af98a8b06a1e22f6e6e1a65b1e2f3816cb3069bb0874825f08c
%global source0_file poppler-data-0.4.11.tar.gz
# oreon url source checksums end

BuildArch:        noarch
BuildRequires: make
BuildRequires:    git

# =============================================================================

# NOTE: 'autosetup' macro (below) uses 'git' for applying the patches:
#       ->> All the patches should be provided in 'git format-patch' format.
#       ->> Auxiliary repository will be created during 'fedpkg prep', you
#           can see all the applied patches there via 'git log'.

# Upstream patches -- official upstream patches released by upstream since the
# ----------------    last rebase that are necessary for any reason:
#Patch000: example000.patch


# Downstream patches -- these should be always included when doing rebase:
# ------------------
#Patch100: example100.patch


# Downstream patches for RHEL -- patches that we keep only in RHEL for various
# ---------------------------    reasons, but are not enabled in Fedora:
%if %{defined rhel} || %{defined centos}
#Patch200: example200.patch
%endif


# Patches to be removed -- deprecated functionality which shall be removed at
# ---------------------    some point in the future:


%description
This package consists of encoding files for use with poppler. The encoding
files are optional and poppler will automatically read them if they are present.

When installed, the encoding files enables poppler to correctly render both CJK
and Cyrrilic characters properly.

# === SUBPACKAGES =============================================================

%package          devel
Summary:          Devel files for %{name}

Requires:         %{name} = %{version}-%{release}
BuildRequires:    pkgconfig

%description devel
This sub-package currently contains only pkgconfig file, which can be used with
pkgconfig utility allowing your software to be build with poppler-data.

# === BUILD INSTRUCTIONS ======================================================

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/poppler-data-0.4.11.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2cec05cd1bb03af98a8b06a1e22f6e6e1a65b1e2f3816cb3069bb0874825f08c" || { echo "oreon: Source0 SHA256 mismatch for poppler-data-0.4.11.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git

# NOTE: Nothing to do here - we are packaging the content only.
%build

%install
%make_install prefix=%{_prefix}

# === PACKAGING INSTRUCTIONS ==================================================

%files
%license COPYING COPYING.adobe COPYING.gpl2
%{_datadir}/poppler/

%files devel
%{_datadir}/pkgconfig/poppler-data.pc

# =============================================================================

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.11-11
- Prepare for Oreon 11 (RP1)
